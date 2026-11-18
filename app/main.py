from fastapi import FastAPI

from app.posts import routes as posts_routes

app = FastAPI()

app.include_router(posts_routes.router)
