import pytest
from unittest.mock import patch
import unittest.mock as mock
from src.controllers.receipecontroller import ReceipeController

# add your test case implementation here
@pytest.fixture
def sut():
    mocked_dao = mock.MagicMock()
    controller = ReceipeController(mocked_dao)
    return controller

@pytest.mark.unit
@pytest.mark.parametrize('recepie, available_items, diet', [({'diets': []}, {}, mock.MagicMock(name='vegan'))])
def test_diet_not_available(recepie, available_items, diet, sut):
    diet.name = 'vegan'
    assert sut.get_receipe_readiness(recepie, available_items, diet) is None

@pytest.mark.unit
@pytest.mark.parametrize('recepie, available_items, diet', [({'diets': ['vegan']}, {}, mock.MagicMock(name='vegan'))])
def test_readiness_eq(recepie, available_items, diet, sut):
    diet.name = 'vegan'
    with patch('src.controllers.receipecontroller.calculate_readiness') as mocked_calculator:
        mocked_calculator.return_value = 0.1
        assert sut.get_receipe_readiness(recepie, available_items, diet) == 0.1

@pytest.mark.unit
@pytest.mark.parametrize('recepie, available_items, diet', [({'diets': ['vegan']}, {}, mock.MagicMock(name='vegan'))])
def test_readiness_lt(recepie, available_items, diet, sut):
    diet.name = 'vegan'
    with patch('src.controllers.receipecontroller.calculate_readiness') as mocked_calculator:
        mocked_calculator.return_value = 0.0
        assert sut.get_receipe_readiness(recepie, available_items, diet) is None

@pytest.mark.unit
@pytest.mark.parametrize('recepie, available_items, diet', [({'diets': ['vegan']}, {}, mock.MagicMock(name='vegan'))])
def test_readiness_gt(recepie, available_items, diet, sut):
    diet.name = 'vegan'
    with patch('src.controllers.receipecontroller.calculate_readiness') as mocked_calculator:
        mocked_calculator.return_value = 0.2
        assert sut.get_receipe_readiness(recepie, available_items, diet) == 0.2