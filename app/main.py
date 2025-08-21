from fastapi import FastAPI
import uvicorn as uv
from app.manager import Manager

app = FastAPI()

manager = Manager()

@app.get("/newdata")
def update_soldier():
    return manager.load_and_process()

# if __name__ == "__main__":
#     uv.run("main:app", host="localhost", port=8050, reload=True)

