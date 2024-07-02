import pytest
from datetime import datetime
from src.widget import convert_date


def test_convert_date_valid(date_strings):
    assert convert_date(date_strings['valid']) == '11.07.2018'


def test_convert_date_invalid(date_strings):
    with pytest.raises(ValueError):
        convert_date(date_strings['invalid'])