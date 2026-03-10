from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.config import API_BEARER_TOKEN

security = HTTPBearer()


def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials

    if token != API_BEARER_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing token"
        )

    return token