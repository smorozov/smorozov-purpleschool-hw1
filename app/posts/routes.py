
from fastapi import APIRouter, Body

router = APIRouter(
    prefix="/posts",
)

@router.get("/{post_id}")
def get_post(post_id: int):
    return f"Found Post with ID: {post_id}"

@router.post("/")
async def create_post(body: dict = Body()):
    post_id = body["post_id"]
    return f"Created Post with ID: {post_id}"

@router.patch("/{post_id}")
def update_post(post_id: int):
    return f"Updated Post with ID: {post_id}"

@router.delete("/{post_id}")
def delete_post(post_id: int):
    return f"Deleted Post with ID: {post_id}"
