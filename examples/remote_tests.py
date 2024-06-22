import os
import pytest

@pytest.mark.skipif(os.environ.get('container') == None, reason="This test should only run within a container!")
class TestPosixCalls:
    def test_prepare(self):
        "will not be setup or run under 'win32' platform"
    
    def test_execute(self):
        pass

    def test_validate(self):
        pass

    def test_clean(self):
        pass