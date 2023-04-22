from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


TRUE_VALUE = 1


class CRUDProjects(CRUDBase):
    async def get_projects_by_name(
        self,
        name: str,
        session: AsyncSession
    ):
        return await session.scalar(
            select(CharityProject).where(
                CharityProject.name == name
            )
        )

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> list[dict[str, int]]:
        projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested == TRUE_VALUE
            )
        )
        return projects.scalars().all()


projects_crud = CRUDProjects(CharityProject)
