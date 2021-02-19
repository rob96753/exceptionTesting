import pytest
import sys


SYS_ARGV = 'sys.argv'
cli_values = [pytest, '--config', '../config.json']

sys.path.insert(1, '../src')
import exception

def raiseMyException():
    location = "raiseMyException"
    value = "exception raised here"
    raise exception.myException(location, value)

class TestClass:
    @pytest.fixture(autouse=False)
    def setup(self, monkeypatch):
        monkeypatch.setattr(SYS_ARGV, cli_values)


    def test_custom_exception(self, setup):
        with pytest.raises(exception.myException):


