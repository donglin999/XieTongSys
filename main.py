from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from modules import Device
from database import init_db

app = FastAPI()
init_db()


@app.post("/device/")
def create_device(device: dict, db: Session = Depends(get_db)):
    return Device.create_device(device, db)

@app.get("/device/{device_number}")
def read_device(device_number: str, db: Session = Depends(get_db)):
    return Device.get_device(device_number, db)

@app.put("/device/{device_number}")
def update_device(device_number: str, device: dict, db: Session = Depends(get_db)):
    return Device.update_device(device_number, device, db)

@app.delete("/device/{device_number}")
def delete_device(device_number: str, db: Session = Depends(get_db)):
    return Device.delete_device(device_number, db)