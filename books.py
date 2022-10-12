from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def first_api():
    return {"message": "hello first api"}


uvicorn.run(app)
