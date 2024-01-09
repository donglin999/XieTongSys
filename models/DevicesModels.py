# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
author ： Xiuxiang
creation_time : 2023/12/27 15:21
file : Devices.py
"""
# Devices.py
from sqlalchemy import Column, Integer, String, JSON, Boolean
from database import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    device_number = Column(String(255), unique=True)
    device_name = Column(String(255), unique=True)  # Unique
    data_source = Column(String(255))
    node = Column(String(255), unique=True, nullable=True)  # Unique
    is_collection_device = Column(Boolean)
    other_description = Column(JSON)


