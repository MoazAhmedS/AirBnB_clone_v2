#!/usr/bin/python3
"""city class"""
from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ 
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
