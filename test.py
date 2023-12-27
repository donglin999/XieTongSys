# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
author: Xiuxiang
creation_time: 2023/12/27 16:51
file: test.py
"""
from sqlalchemy.orm import Session
from models.Devices import Device   # 确保 Device 模型中的 name 字段有指定长度
from database import SessionLocal, engine, Base

# 创建表（如果尚未创建）
Base.metadata.create_all(bind=engine)

# 插入测试数据
def create_test_device():
    db = SessionLocal()
    new_device = Device(name="Test Device")  # 确保这里的 name 字段与模型定义一致
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    return new_device.id

# 查询测试数据
def get_test_device(device_id):
    db = SessionLocal()
    device = db.query(Device).filter(Device.id == device_id).first()
    db.close()  # 关闭 session
    return device

# 测试函数
def test_db():
    print("Creating a test device...")
    device_id = create_test_device()
    print("Created device with ID:", device_id)

    print("Querying the test device...")
    device = get_test_device(device_id)
    if device:
        print("Retrieved device:", device.name)
    else:
        print("No device found with ID:", device_id)

if __name__ == "__main__":
    test_db()
