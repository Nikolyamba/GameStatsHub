import uvicorn
from fastapi import FastAPI

from backend.api.user_api import u_router
from frontend.main import start_ui

app = FastAPI()

app.include_router(u_router, prefix='/api')

start_ui(app)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level='info', reload=True)
