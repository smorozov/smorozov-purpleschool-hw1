import logging
from typing import Annotated

from fastapi import APIRouter, Depends

from app.posts.schema import (
    PostCreateRequest,
    PostCreateResponse,
    PostGetResponse,
    PostPath,
    PostUpdateRequest,
    PostUpdateResponse,
    TaskPathDeps,
)
from app.posts.service import PostServiceDeps

router = APIRouter(prefix="/v1/posts", tags=["Posts"])
logger = logging.getLogger(__name__)


@router.get(
    "/{post_id}",
    response_model=PostGetResponse,
    responses={404: {"description": "Публикация не найдена"}},
    summary="Получает публикацию по ID",
    description="Получает детали публикации по ID. Если публикация не найдена, возвращает ошибку.",
)
def get_post(service: PostServiceDeps, path: TaskPathDeps):
    res = service.get_post_by_id(path.post_id)
    logger.info("Найдена публикация: ", extra={"post_id": res})
    return PostGetResponse(id=res, content="Post content")


@router.post(
    "/",
    response_model=PostCreateResponse,
    status_code=201,
    summary="Создаёт публикацию",
    description="Сохраняет запись в БД с деталями публикации.",
)
async def create_post(data: PostCreateRequest):
    return PostCreateResponse(id=1, content=data.content)


@router.patch(
    "/{post_id}",
    response_model=PostUpdateResponse,
    responses={404: {"description": "Публикация не найдена"}},
    summary="Обновляет публикацию",
    description="Обновляет содержание публикации и сохраняет в БД. Если публикация не найдена, возвращает ошибку.",
)
def update_post(data: PostUpdateRequest, path: Annotated[PostPath, Depends(PostPath)]):
    return PostUpdateResponse(id=path.post_id, content=data.content)


@router.delete(
    "/{post_id}",
    status_code=204,
    responses={404: {"description": "Публикация не найдена"}},
    summary="Удаляет публикацию",
    description="Находит и удаляет из БД запись публикации по ID. Если публикация не найдена, возвращает ошибку.",
)
def delete_post(path: Annotated[PostPath, Depends(PostPath)]):
    return
