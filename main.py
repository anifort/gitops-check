from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/about-us")
async def root():
    return {"message": "About us: We are a company that sells products"}
