# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
author ： Xiuxiang
creation_time : 2023/12/29 10:06
file : Devices.py
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Devices as models
from database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_device(device: dict, db: Session):
    db_device = models.Device(**device)
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

def get_device(device_number: str, db: Session):
    db_device = db.query(models.Device).filter(models.Device.device_number == device_number).first()
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return db_device

def update_device(device_number: str, device: dict, db: Session):
    db_device = db.query(models.Device).filter(models.Device.device_number == device_number).first()
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    for key, value in device.items():
        setattr(db_device, key, value)
    db.commit()
    return db_device

def delete_device(device_number: str, db: Session):
    db_device = db.query(models.Device).filter(models.Device.device_number == device_number).first()
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    db.delete(db_device)
    db.commit()