import logging
from typing import Annotated

from fastapi import Depends

from app.core.db import DbSessionDeps
from app.posts.model import Post

logger = logging.getLogger(__name__)

class PostRepository:
    def __init__(self, session: DbSessionDeps):
        self.session = session

    def get_by_id(self, post_id: int):
        return post_id

    async def create(self):
        post = Post(
            title="Новая публикация",
            created_at="PurpleSchool"
        )
        self.session.add(post)
        await self.session.commit()
        await self.session.refresh(post)
        logger.info(f"Post '{post.title}' is created")

def get_post_repository(session: DbSessionDeps) -> PostRepository:
    return PostRepository(session)


PostRepositoryDeps = Annotated[PostRepository, Depends(get_post_repository)]
