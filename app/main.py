from fastapi import FastAPI

from app.posts import routes as posts_routes

app = FastAPI(
    title="Posts API",
    description="API для работы c публикациями",
    version="0.0.1",
    openapi_tags=[{"name": "Posts", "description": "Работа с публикациями"}],
)

app.include_router(posts_routes.router)
