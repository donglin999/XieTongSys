# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
author ： Xiuxiang
creation_time : 2023/12/27 16:37
file : database.py
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import redis

DATABASE_URL = "mysql+pymysql://root:dmx12593@localhost/xietongsys"
r = redis.Redis(host='localhost', port=6379, db=0)
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)
