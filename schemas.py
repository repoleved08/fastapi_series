from datetime import date
from enum import Enum
from pydantic import BaseModel


class GenreURLChoices(Enum):
    POP = 'pop'
    HIP_HOP = 'hip-hop'


class Album(BaseModel):
    title: str
    release_date: date


class Band(BaseModel):
    id: int
    name: str
    genre: str
    song: str
    album: list[Album] = []
