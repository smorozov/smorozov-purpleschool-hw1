from typing import Annotated

from pydantic import BaseModel, Field, StringConstraints


class PostPath(BaseModel):
    post_id: int = Field(gt=0, description="Идентификатор публикации", examples=[1])


Content = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=1),
    Field(
        description="Текст публикации.",
    ),
]


class PostCreateRequest(BaseModel):
    content: Content


class PostUpdateRequest(BaseModel):
    content: Content | None = None


class PostCreateResponse(BaseModel):
    id: int = Field(description="Идентификатор публикации", examples=[1])
    content: str


class PostGetResponse(BaseModel):
    id: int = Field(description="Идентификатор публикации", examples=[1])
    content: str


class PostUpdateResponse(BaseModel):
    id: int = Field(description="Идентификатор публикации", examples=[1])
    content: str | None = None
