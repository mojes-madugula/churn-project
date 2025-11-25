# churn-project

Basic data science project scaffold for churn prediction.

Project layout

- `data/`
	- `raw/` - raw datasets (do not commit large files here)
	- `processed/` - cleaned and engineered datasets
- `notebooks/` - exploratory and feature notebooks
- `src/` - Python source code (data cleaning, feature engineering, training, prediction)
- `models/` - saved models
- `reports/figures` - figures and report assets
- `tests/` - unit tests

Setup

1. Create a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install requirements:

```powershell
pip install -r requirements.txt
```

Run tests

```powershell
pytest -q
```

Notes

- Keep raw data out of version control. Put raw files into `data/raw/` locally and keep `data/processed/` for cleaned artifacts.
- Fill the `src/` modules with real implementations as you proceed.