
from fastapi import APIRouter, Depends

from app.posts.schema import PostCreateRequest, PostCreateResponse, PostPath, PostUpdateRequest, PostUpdateResponse

router = APIRouter(
    prefix="/posts",
)

@router.get("/{post_id}")
def get_post(path: PostPath = Depends(PostPath)):
    return PostCreateResponse(
        id = path.post_id,
        content = "Post content"
    )

@router.post("/", response_model=PostCreateResponse)
async def create_post(data: PostCreateRequest):
    return PostCreateResponse(
        id = 1,
        content = data.content
    )

@router.patch("/{post_id}", response_model=PostUpdateResponse)
def update_post(data: PostUpdateRequest,
                path: PostPath = Depends(PostPath)):
    return PostUpdateResponse(
        id = path.post_id,
        content = data.content
    )

@router.delete("/{post_id}")
def delete_post(path: PostPath = Depends(PostPath)):
    return f"Deleted Post with ID: {path.post_id}"
