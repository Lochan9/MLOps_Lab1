MLOps Lab 1 – Automated Testing & Continuous Integration Pipeline  

This repository demonstrates a **production-grade CI/CD pipeline** that validates Python code using both `unittest` and `pytest`.  
It extends the base MLOps Lab 1 requirements by adding stronger structure, dual testing workflows, reproducible environments, and detailed logging — mirroring **real-world engineering pipelines**.

---

## 🚀 Key Highlights  

| Feature | Description |
|----------|-------------|
| 🧩 **Dual Testing Frameworks** | Both `unittest` and `pytest` implemented to test identical logic under different paradigms. |
| ⚙️ **Full CI/CD Automation** | GitHub Actions runs both frameworks automatically on every push or pull request. |
| 🧱 **Clean Repository Design** | Organized into `src/`, `test/`, `.github/workflows/`, and `data/`. |
| 🧮 **Validation Layer** | `validate_pipeline.py` adds runtime logging & data-quality checks (beyond template scope). |
| 🔁 **Reproducible Environment** | `requirements.txt` locks dependencies → identical local & cloud execution. |
| 🧰 **Multi-Python Matrix** | CI verifies compatibility on 3.10 → 3.12 to future-proof builds. |
| 🧾 **Enhanced Documentation** | Includes setup steps, verification logs, CI tables, and differentiators for evaluation. |

---

## 🧩 Project Structure  

MLOps_Lab1/  
│── src/  
│   ├── calculator.py      → core arithmetic logic  
│   ├── validate_pipeline.py   → custom logging + integrity validation  
│── test/  
│   ├── test_pytest.py     → parameterized pytest tests  
│   ├── test_unittest.py   → class-based unittest suite  
│── .github/workflows/  
│   ├── pytest_action.yml   → multi-version pytest CI  
│   ├── unittest_action.yml  → unittest CI on Python 3.12  
│── data/results.csv  
│── requirements.txt  
│── README.md  

---

## ⚙️ Setup & Execution  

```bash
# Clone repo
git clone https://github.com/Lochan9/MLOps_Lab1.git
cd MLOps_Lab1

# Create & activate virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests locally
python -m pytest -v
python -m unittest discover -s test -p "test_*.py" -v
