from datetime import date
from enum import Enum
from pydantic import BaseModel


class GenreURLChoices(Enum):
    POP = 'pop'
    HIP_HOP = 'hip-hop'

class GenreChoices(Enum):
    POP = 'Pop'
    HIP_HOP = 'Hip-Hop'

class Album(BaseModel):
    title: str
    release_date: date


class BandBase(BaseModel):
    name: str
    genre: GenreChoices
    song: str
    album: list[Album] = []


class BandCreate(BandBase):
    pass


class BandWithId(BandBase):
    id: int
