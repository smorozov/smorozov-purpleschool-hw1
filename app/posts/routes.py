from typing import Annotated

from fastapi import APIRouter, Depends

from app.posts.schema import (
    PostCreateRequest,
    PostCreateResponse,
    PostGetResponse,
    PostPath,
    PostUpdateRequest,
    PostUpdateResponse,
)

router = APIRouter(
    prefix="/posts", tags=["Posts"]
)


@router.get("/{post_id}", response_model=PostGetResponse, summary="Получает публикацию по ID",
            description="Получает детали публикации по ID. Если публикация не найдена, возвращает ошибку.")
def get_post(path: Annotated[PostPath,  Depends(PostPath)]):
    return PostGetResponse(id=path.post_id, content="Post content")


@router.post("/", response_model=PostCreateResponse, summary="Создаёт публикацию",
            description="Сохраняет запись в БД с деталями публикации.")
async def create_post(data: PostCreateRequest):
    return PostCreateResponse(id=1, content=data.content)


@router.patch("/{post_id}", response_model=PostUpdateResponse, summary="Обновляет публикацию",
            description="Обновляет содержание публикации и сохраняет в БД.")
def update_post(data: PostUpdateRequest, path: Annotated[PostPath,  Depends(PostPath)]):
    return PostUpdateResponse(id=path.post_id, content=data.content)


@router.delete("/{post_id}", summary="Удаляет публикацию",
            description="Находит и удаляет из БД запись публикации по ID. Если публикация не найдена, возвращает ошибку.")
def delete_post(path: Annotated[PostPath,  Depends(PostPath)]):
    return f"Deleted Post with ID: {path.post_id}"
