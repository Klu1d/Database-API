import os
import hmac
from fastapi import HTTPException, Request
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def secret(request: Request):
    api_key = request.headers.get("X-API-Key")
    
    if not api_key or not hmac.compare_digest(api_key, API_KEY):
        raise HTTPException(status_code=403, detail="Access denied")
    
    return api_key