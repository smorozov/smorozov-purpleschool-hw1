from typing import Annotated

from fastapi import Depends

from app.posts.repository import PostRepository, PostRepositoryDeps


class PostService:
    def __init__(self, repository: PostRepository):
        self.repository = repository

    def get_post_by_id(self, post_id: int) -> int:
        return self.repository.get_by_id(post_id)


def get_post_service(repository: PostRepositoryDeps) -> PostService:
    return PostService(repository)


PostServiceDeps = Annotated[PostService, Depends(get_post_service)]
