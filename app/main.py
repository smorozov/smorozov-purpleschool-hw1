from fastapi import FastAPI

app = FastAPI()

counter = 1

@app.get("/")
def root():
    global counter
    counter += 1
    return {"Counter": counter}