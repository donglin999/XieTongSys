# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
author ： Xiuxiang
creation_time : 2023/12/27 15:21
file : Devices.py
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    # data_points = relationship("DataPoint", back_populates="device")
    # collection_methods = relationship("CollectionMethod", back_populates="device")
