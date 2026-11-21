from typing import Annotated

from fastapi import Depends


class PostRepository:
    def get_by_id(self, project_id: int) -> int:
        return project_id


def get_post_repository() -> PostRepository:
    return PostRepository()


PostRepositoryDeps = Annotated[PostRepository, Depends(get_post_repository)]
