from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    userId : int
    userNickName : str | None = None


@app.post("/sample")
async def sample(user:User):
    if user is not None:
        return {"data":user}
    return {"data":"missing ...."}

