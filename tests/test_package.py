import steamctypes


def test_version() -> None:
    assert isinstance(steamctypes.__version__, str)
    assert steamctypes.__version__
