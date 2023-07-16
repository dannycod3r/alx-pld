#!/usr/bin/python3
"""city module"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class

    Attributes:
        state_id(string): id of the state
        name(string): name of the state
    """
    state_id = ""
    name = ""
