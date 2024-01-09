# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
author ： Xiuxiang
creation_time : 2024/1/9 10:28
file : PointsModels.py
"""
# models/PointsModels.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base

class Point(Base):
    __tablename__ = "points"  # Add this line

    id = Column(Integer, primary_key=True, index=True)
    point_name = Column(String(255))
    node = Column(String(255), ForeignKey('devices.node'))
    device_name = Column(String(255), ForeignKey('devices.device_name'))
    station_id = Column(String(255))
    leaf = Column(String(255))
    pnVal = Column(String(255))
