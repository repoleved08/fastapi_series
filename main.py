from fastapi import FastAPI, HTTPException
from enum import Enum
from schemas import GenreURLChoices, BandBase, BandCreate, BandWithId

app = FastAPI()


BAND = [
    {'id': 1, 'name': "Westlife", 'genre': 'pop', 'song': 'soledad'},
    {'id': 2, 'name': "Kendrick", 'genre': 'hip-hop', 'song': 'money trees', 'album': [
        {'title': 'GNX', 'release_date': '2024-11-21'}
    ]},
    {'id': 3, 'name': "Dax", 'genre': 'hip-hop', 'song': 'Alcohol'}
]


@app.get('/bands')
async def index(genre: GenreURLChoices | None = None, has_albums: bool = False) -> list[BandWithId]:
    band_list = [BandWithId(**b) for b in BAND]

    if genre:
        band_list = [
            b for b in band_list if b.genre.lower() == genre.value
        ]
    if has_albums:
        band_list = [b for b in band_list if len(b.album) > 0]
    return band_list


@app.get('/band/{band_id}')
async def band(band_id: int) -> BandWithId:
    band = next((BandWithId(**b) for b in BAND if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(
            status_code=404, detail="Band Not Found")
    return band


@app.get('/band/genre/{genre}')
async def band_by_genre(genre: GenreURLChoices) -> list[BandWithId]:
    return [
        BandWithId(**b) for b in BAND if b['genre'].lower() == genre.value
    ]


@app.get('/about')
async def about() -> str:
    return "Techxtrasol is the best solution company!"


@app.post('/bands')
async def create_band(band_data: BandCreate) -> BandWithId:
    id = BAND[-1]['id'] + 1
    band = BandWithId(id=id, **band_data.model_dump())
    BAND.append(band.model_dump())
    return band
