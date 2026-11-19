from typing import Annotated

from pydantic import BaseModel, Field, StringConstraints


class PostPath(BaseModel):
    post_id: int = Field(gt=0)


Content = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class PostCreateRequest(BaseModel):
    content: Content


class PostUpdateRequest(BaseModel):
    content: Content | None = None


class PostCreateResponse(BaseModel):
    id: int
    content: str


class PostGetResponse(BaseModel):
    id: int
    content: str


class PostUpdateResponse(BaseModel):
    id: int
    content: str | None = None
