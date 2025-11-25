import runpy


def test_main_exists():
    """Ensure `main` exists in `src/data_cleaning.py`."""
    mod = runpy.run_path("src/data_cleaning.py")
    assert "main" in mod
