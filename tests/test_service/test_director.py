from unittest.mock import MagicMock

import pytest

from project.dao.director import DirectorDAO
from project.dao.model.director import Director
from project.service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name='First Director')
    d2 = Director(id=2, name='Second Director')
    d3 = Director(id=3, name='Third Director')

    directors = {1: d1, 2: d2, 3: d3}

    director_dao.get_one = MagicMock(side_effect=directors.get)
    director_dao.get_all = MagicMock(return_value=directors.values())
    director_dao.create = MagicMock(return_value=Director(id=1, name='First Director'))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director != None
        assert director.id != None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert directors != None
        assert len(directors) > 0

    def test_create(self):
        d1 = {'name': 'First Director'}
        director = self.director_service.create(d1)
        assert director != None
        assert director.id != None

    def test_update(self):
        d1 = {'id': 1, 'name': 'New Name'}
        self.director_service.update(d1)

    def test_partial_update(self):
        d1 = {'id': 1, 'name': 'New Name'}
        self.director_service.update(d1)

    def test_delete(self):
        self.director_service.delete(1)
