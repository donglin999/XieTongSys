# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
author ： Xiuxiang
creation_time : 2024/1/9 10:18
file : Device.py
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from modules import Device

router = APIRouter()

@router.post("/device/")
def create_device(device: dict, db: Session = Depends(get_db)):
    return Device.create_device(device, db)

@router.get("/device/{device_number}")
def read_device(device_number: str, db: Session = Depends(get_db)):
    return Device.get_device(device_number, db)

@router.put("/device/{device_number}")
def update_device(device_number: str, device: dict, db: Session = Depends(get_db)):
    return Device.update_device(device_number, device, db)

@router.delete("/device/{device_number}")
def delete_device(device_number: str, db: Session = Depends(get_db)):
    return Device.delete_device(device_number, db)