from fastapi import FastAPI
from database import init_db
from router import DeviceRouter

app = FastAPI()
init_db()



app = FastAPI()
init_db()

app.include_router(DeviceRouter.router)