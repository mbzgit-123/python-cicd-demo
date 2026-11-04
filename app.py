from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello CI/CD CB!", "version": "1.0"}


@app.get("/hello")
def hello():
    return {"message": "Hello Agent!"}
