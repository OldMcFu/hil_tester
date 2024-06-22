import os
import pytest

@pytest.mark.skipif(os.os.environ.get('container') != None, reason="This test should only run on the real hardware!")
class TestCaseNameForHwTests:
    def test_prepare(self):
        "will not be setup or run under 'win32' platform"
    
    def test_execute(self):
        pass

    def test_validate(self):
        pass

    def test_clean(self):
        pass