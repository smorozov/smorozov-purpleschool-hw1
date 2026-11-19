from fastapi import HTTPException
from pydantic import BaseModel, Field, field_validator

class PostPath(BaseModel):
    post_id: int = Field(gt=0)

class PostCreateRequest(BaseModel):
    content: str

    @field_validator("content")
    @classmethod
    def content_not_empty(cls, value):
        if not value.strip():
            raise HTTPException(status_code=400, detail="Content cannot be empty")
        return value

class PostUpdateRequest(BaseModel):
    content: str | None = None


class PostCreateResponse(BaseModel):
    id: int
    content: str

class PostUpdateResponse(BaseModel):
    id: int
    content: str | None = None
