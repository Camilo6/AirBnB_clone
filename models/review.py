#!/usr/bin/python3
""" New state class """

from models.base_model import BaseModel


class Review(BaseModel):
    """ New review inherits """

    place_id = ""
    user_id = ""
    text = ""
