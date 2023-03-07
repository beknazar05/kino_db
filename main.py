from app.models.posts.post_model import Genre, PostGenres,Post
from app.models.basemodel import db_connection,db 
from app.queries.genres import create_genre,delete_genre,get_genres
from app.queries.posts import create_post,get_all_films,get_film_by_id
from app.schemas.posts import PostCreateSchema
from app.routes.posts import router 

from fastapi import FastAPI


@db
def create_tables() -> None:
    db_connection.create_tables([Genre, Post, PostGenres])

create_tables()
    
app = FastAPI()
app.include_router(router)

# create_genre('Detective')
# create_genre('Horror')
# delete_genre('piski')
# print(get_genres())

# create_post('Sherlock','some_desc','2008','England',['Detective','Horror'])

# create_post('fast furios','desc','2000','U.S.A',['Gonki'])

# create_post(
#     'Elita',
#     'some_description',
#     '2018',
#     'europe',
#     ['Detective']
# )
# print(get_all_films())
# print(get_film_by_id(10))
# from datetime import date 
# create_post(PostCreateSchema(title='',description='Film about zombi',year=date(2020,1,1),country='USA',genre=['Detective']))

