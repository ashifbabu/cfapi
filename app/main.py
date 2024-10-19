from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import Redis
from loguru import logger
from .utils import combined_flight_search
from .models.flight_search_models import FlightSearchRequest
from jose import JWTError, jwt
from .config import settings

# FastAPI Application Initialization
app = FastAPI(
    title="Enterprise Flight API",
    description="API for searching and booking flights.",
    version="1.0.0"
)

# Configuration for OAuth2 and Rate Limiting
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
limiter = Limiter(key_func=get_remote_address)

# JWT Configuration
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"

# Application Startup Event
@app.on_event("startup")
async def startup():
    # Initialize Redis for caching
    redis_client = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")
    
    # Configure logging
    logger.add("file.log", rotation="500 MB", level="INFO")

# Function to create JWT access tokens
def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

# Dependency to get the current user from the token
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = payload.get("sub")
        if user is None:
            raise HTTPException(status_code=400, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate token")
    return user

# Flight search endpoint with rate limiting
@app.post("/v1/flights/search/")
@limiter.limit("10/minute")  # Rate limiting to 10 requests per minute
async def flight_search(request: FlightSearchRequest, token: str = Depends(oauth2_scheme)):
    logger.info(f"Flight search called: {request.origin} to {request.destination}")
    result = await combined_flight_search(request.origin, request.destination, request.date)
    return result

# Health check endpoint
@app.get("/v1/healthcheck")
async def health_check():
    return {"status": "OK"}
