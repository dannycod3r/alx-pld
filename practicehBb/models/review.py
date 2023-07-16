#!/usr/bin/python3
"""review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class

    Attributes:
        place_id: id of place
        user_id: user id
        test: the review text
    """
    place_id = ""
    user_id = ""
    text = ""
