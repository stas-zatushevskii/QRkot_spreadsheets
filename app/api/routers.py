from fastapi import APIRouter

from app.api.endpoints.donations import router as donations_router
from app.api.endpoints.projects import router as projects_router
from app.api.endpoints.user import router as user_router
from app.api.endpoints.google_api import router as google_api_router

main_router = APIRouter()
main_router.include_router(
    donations_router, prefix='/donation', tags=['Donations']
)
main_router.include_router(
    projects_router, prefix='/charity_project', tags=['Projects']
)
main_router.include_router(
    google_api_router, prefix='/google', tags=['Google']
)
main_router.include_router(user_router)
