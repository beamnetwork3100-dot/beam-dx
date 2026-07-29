from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.get("/")
def auth_home():
    return {
        "message": "Beam Dx Authentication API"
    }

@router.get("/status")
def auth_status():
    return {
        "status": "Authentication service is running"
    }
