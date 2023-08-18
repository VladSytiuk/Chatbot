from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

X_API_KEY_TOKEN = settings.X_API_KEY_TOKEN


def api_key_auth(api_key: str = Depends(oauth2_scheme)):
    if X_API_KEY_TOKEN != api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Forbidden"
        )
