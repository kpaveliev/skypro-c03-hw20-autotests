from unittest.mock import MagicMock

import pytest

from project.dao.movie import MovieDAO
from project.dao.model.movie import Movie
from project.service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title='First Movie', description='Description',
               trailer='link', year=2000, rating=10.0, genre_id=1, director_id=1)
    m2 = Movie(id=2, title='Second Movie', description='Description',
               trailer='link', year=2000, rating=10.0, genre_id=1, director_id=1)
    m3 = Movie(id=3, title='Third Movie', description='Description',
               trailer='link', year=2000, rating=10.0, genre_id=1, director_id=1)

    movies = {1: m1, 2: m2, 3: m3}

    movie_dao.get_one = MagicMock(side_effect=movies.get)
    movie_dao.get_all = MagicMock(return_value=movies.values())
    movie_dao.create = MagicMock(return_value=Movie(id=1, title='First Movie'))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie != None
        assert movie.id != None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert movies != None
        assert len(movies) > 0

    def test_create(self):
        m1 = {
            'title': 'First Movie',
            'description': 'Description',
            'trailer': 'link',
            'year': 2000,
            'rating': 10.0,
            'genre_id': 1,
            'director_id': 1
              }
        movie = self.movie_service.create(m1)
        assert movie != None
        assert movie.id != None

    def test_update(self):
        m1 = {
            'id': 1,
            'title': 'First Movie',
            'description': 'Description',
            'trailer': 'link',
            'year': 2000,
            'rating': 10.0,
            'genre_id': 1,
            'director_id': 1
              }
        self.movie_service.update(m1)

    def test_partial_update(self):
        m1 = {
            'id': 1,
            'title': 'New Name'
        }
        self.movie_service.update(m1)

    def test_delete(self):
        self.movie_service.delete(1)
