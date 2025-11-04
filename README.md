@'
# 🧠 MLOps Lab 1 – Automated Testing & Continuous Integration Pipeline

This repository implements a **complete testing and CI/CD pipeline** that combines both `unittest` and `pytest` frameworks — ensuring full validation, modularity, and reproducibility.  
Unlike a simple one-script submission, this lab mirrors **real-world MLOps practices** with structured automation, GitHub Actions integration, and clean code versioning.

---

## 🚀 Key Highlights

| Feature | Description |
|----------|--------------|
| 🧩 **Dual Testing Frameworks** | Uses both `unittest` (for functional tests) and `pytest` (for parameterized, expressive tests). |
| ⚙️ **Automated CI/CD Pipeline** | GitHub Actions automatically runs both frameworks on each push or pull request. |
| 🧱 **Structured Project Layout** | Organized `src/` and `test/` directories follow industry-standard MLOps design. |
| 🔁 **Reproducible Setup** | `requirements.txt` ensures identical environments across local and cloud runs. |
| 🧮 **Validation Pipeline** | Custom `validate_pipeline.py` script performs result integrity checks and logs statistics. |
| 🧰 **Cross-Version Testing** | Verified on Python 3.10 → 3.12 for compatibility and future-proofing. |

---

## 🧩 Project Structure
MLOps_Lab1/
│── src/  
│   ├── calculator.py                 → core computation logic  
│   ├── validate_pipeline.py          → verifies and logs computed results  
│── test/  
│   ├── test_pytest.py                → parameterized tests using pytest  
│   ├── test_unittest.py              → functional tests using unittest  
│── .github/workflows/  
│   ├── pytest_action.yml             → CI workflow for pytest validation  
│   ├── unittest_action.yml           → CI workflow for unittest validation  
│── data/results.csv                  → sample output data  
│── requirements.txt                  → dependency file  
│── README.md                         → documentation  

---

## ⚙️ Setup & Local Execution

```bash
# Clone repository
git clone https://github.com/Lochan9/MLOps_Lab1.git
cd MLOps_Lab1

# Create and activate environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run all tests
python -m pytest -v
python -m unittest discover -s test -p "test_*.py" -v
