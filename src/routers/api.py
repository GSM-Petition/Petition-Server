from fastapi import APIRouter

from .petitions import petitions
from .admin import admin

router = APIRouter()

@router.post("/test")
def test():
    return "petition"


router.include_router(
    petitions,
    prefix="/petitions",
    tags=["api", "petitions"],
    responses={404: {"description": "Not found"}},
)
router.include_router(
    admin,
    prefix="/admin",
    tags=["api", "admin"],
    responses={404: {"description": "Not found"}},
)