# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
author ： Xiuxiang
creation_time : 2023/12/29 10:06
file : Devices.py
"""
import time

from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import DevicesModels as models
from database import SessionLocal
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, create_engine




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# modules/Device.py




def create_device_table(device_name: str, db: Session):
    meta = MetaData()
    table = Table(
        device_name,
        meta,
        Column('id', Integer, primary_key=True, index=True),
        Column('point_name', String(255)),
        Column('node', String(255)),  # 外键引用
        Column('device_name', String(255)),  # 外键引用
        Column('station_id', String(255)),
        Column('leaf', String(255), unique=True),
        Column('pnVal', String(255)),
    )
    meta.create_all(db.bind)
def create_device(device: dict, db: Session):
    db_device = models.Device(**device)
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    time.sleep(2)
    if device.get('is_collection_device'):
        create_device_table(device['device_name'], db)
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