from fastapi import FastAPI
import service

app = FastAPI()

app.include_router(service.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)