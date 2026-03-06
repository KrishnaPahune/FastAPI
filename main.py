from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Dear"}

@app.get("/about")
def root():
    return {"Hi there"}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"name: {payload['name']} roll: {payload['roll']}"}