import pytest



@pytest.mark.smoke
def test_smoke():
    ...

@pytest.mark.regression
def test_regression():
    ...


@pytest.mark.smoke
class TestSuite:
    @pytest.mark.slow
    def test_case1(self):
        ...

    def test_case2(self):
        ...
