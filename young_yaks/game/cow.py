import arcade
import enum


class CowBreedType(enum.Enum):
    meat = 0
    milk = 1
    burp = 2


class Cow(arcade.Sprite):
    """ Represents a cow"""
    def __init__(self, type):
        pass
