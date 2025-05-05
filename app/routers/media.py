import os
from pathlib import Path

from auth import secret
from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from fastapi.responses import FileResponse


router = APIRouter()

ALLOWED_IMAGE_TYPES = set(os.getenv("ALLOWED_IMAGE_TYPES", "image/jpeg,image/jpg,image/png").split(","))
ALLOWED_VIDEO_TYPES = set(os.getenv("ALLOWED_VIDEO_TYPES", "video/mp4,video/quicktime,video/x-msvideo").split(","))
ALLOWED_TYPES = ALLOWED_IMAGE_TYPES.union(ALLOWED_VIDEO_TYPES)
MEDIA_PATH = Path(os.getenv("MEDIA_PATH", "media")).resolve()

upload_description = f"""
Upload an image or video file to the server.

- Supported image types: **{ALLOWED_IMAGE_TYPES}**
- Supported video types: **{ALLOWED_VIDEO_TYPES}**
- File will be stored in either `media/image/` or `media/video/` folder.
- ⚠️ It is **strongly recommended** to avoid using spaces in filenames. Any spaces will be replaced with underscores (`_`) automatically.
"""

download_description = """
Download an uploaded image or video file by its filename.

- Spaces in the filename are automatically replaced with underscores (`_`) when looking for the file.
- Returns the file with the correct media type.
"""


@router.post("/upload", description=upload_description)
async def upload(file: UploadFile = File(...), api_key: str = Depends(secret)) -> dict:
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type - {file.content_type}",
        )

    if file.content_type in ALLOWED_IMAGE_TYPES:
        folder = "image"
    elif file.content_type in ALLOWED_VIDEO_TYPES:
        folder = "video"

    safe_filename = file.filename.replace(" ", "_")
    file_path = MEDIA_PATH / folder / safe_filename
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "wb+") as f:
        content = await file.read()
        f.write(content)

    return {"filename": safe_filename, "type": file.content_type}


@router.get("/download/{filename}", response_class=FileResponse, description=download_description)
async def download(filename: str, api_key: str = Depends(secret)) -> FileResponse:
    safe_filename = filename.replace(" ", "_")
    image_path = MEDIA_PATH / "image" / safe_filename
    video_path = MEDIA_PATH / "video" / safe_filename

    if image_path.exists():
        return FileResponse(image_path, media_type="image/jpeg", filename=filename)
    elif video_path.exists():
        return FileResponse(video_path, media_type="application/octet-stream", filename=filename)
    else:
        raise HTTPException(status_code=404, detail="File not found")
