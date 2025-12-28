from fastapi import FastAPI
from database import engine
import models
import service

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(service.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)