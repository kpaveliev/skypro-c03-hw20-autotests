from unittest.mock import MagicMock

import pytest

from project.dao.genre import GenreDAO
from project.dao.model.genre import Genre
from project.service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    g1 = Genre(id=1, name='First Genre')
    g2 = Genre(id=2, name='Second Genre')
    g3 = Genre(id=3, name='Third Genre')

    genres = {1: g1, 2: g2, 3: g3}

    genre_dao.get_one = MagicMock(side_effect=genres.get)
    genre_dao.get_all = MagicMock(return_value=genres.values())
    genre_dao.create = MagicMock(return_value=Genre(id=1, name='First Genre'))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre != None
        assert genre.id != None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert genres != None
        assert len(genres) > 0

    def test_create(self):
        g1 = {'name': 'First Genre'}
        genre = self.genre_service.create(g1)
        assert genre != None
        assert genre.id != None

    def test_update(self):
        g1 = {'id': 1, 'name': 'New Name'}
        self.genre_service.update(g1)

    def test_partial_update(self):
        g1 = {'id': 1, 'name': 'New Name'}
        self.genre_service.update(g1)

    def test_delete(self):
        self.genre_service.delete(1)
