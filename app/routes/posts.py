from app.queries.posts import (
    get_all_films,
    get_film_by_id,
    create_post
    )
from app.schemas.posts import PostCreateSchema
from fastapi import APIRouter

router = APIRouter()

@router.get('/posts')
def get_films() -> None:
    return get_all_films()

@router.post('/create-post')
def create_film(film: PostCreateSchema) -> None:
    return create_post(film)


# TODO: Dopisat CRUD u ostalnuh 
# TODO: Dopisat vse ostalnoe 
