#!/usr/bin/python3
""" Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits from main class """
    place_id = ""
    user_id = ""
    text = ""
