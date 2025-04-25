import hmac
import os

from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader

load_dotenv()

API_KEY = os.getenv("API_KEY")
input_key = APIKeyHeader(name="X-API-Key")

def secret(key: str = Depends(input_key)):
    if not hmac.compare_digest(key, API_KEY):
        raise HTTPException(status_code=403, detail="Access denied")

    return key