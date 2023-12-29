# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
author ： Xiuxiang
creation_time : 2023/12/27 15:21
file : Devices.py
"""
# Devices.py
from sqlalchemy import Column, Integer, String, JSON
from database import Base, get_db

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    device_number = Column(String(255), unique=True)
    device_name = Column(String(255))
    data_source = Column(String(255))
    other_description = Column(JSON)

def create_device(device: dict):
    db = next(get_db())
    db_device = Device(**device)
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

# 同样地，你可以添加其他的数据库操作函数，如get_device, update_device, delete_device等