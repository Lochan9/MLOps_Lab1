# 🧪 MLOps Lab 1 – Testing & CI/CD Automation

**Course:** IE-7374 – Machine Learning Operations (MLOps)  
**Student:** Lochan Enugula  
**University:** Northeastern University (Boston)  

---

## 📘 Overview
This lab demonstrates key MLOps principles through a complete testing and automation pipeline.  
It includes:  
- Virtual environment setup and structured folders  
- Core modules (`calculator.py`, `validate_pipeline.py`)  
- Tests with **Pytest** and **Unittest**  
- CI/CD via **GitHub Actions**  
- Multi-version build matrix (Python 3.10 → 3.12)

---

## 🗂️ Project Structure
MLOps_Lab1/
│
├── src/
│   ├── calculator.py
│   └── validate_pipeline.py
│
├── test/
│   ├── test_pytest.py
│   └── test_unittest.py
│
├── .github/workflows/
│   ├── pytest_action.yml
│   └── unittest_action.yml
│
├── data/results.csv
├── requirements.txt
└── README.md

---

## ⚙️ Setup & Execution
git clone https://github.com/Lochan9/MLOps_Lab1.git
cd MLOps_Lab1
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

Run tests:
python -m pytest -v
python -m unittest discover -s test -p "test_*.py" -v

Expected output:
7 passed in 0.2 s
OK

---

## 🤖 CI/CD Summary
- `pytest_action.yml` → runs Pytest on Python 3.10 / 3.11 / 3.12  
- `unittest_action.yml` → runs Unittest on Python 3.12  
- Triggered automatically on push or pull request to `main`

---

## ✅ Verification
| Check | Status | Details |
|-------|--------|----------|
| Local Pytest | ✅ Passed | 3 parameterized tests successful |
| Local Unittest | ✅ Passed | 4 class-based tests successful |
| GitHub Actions (Pytest) | ✅ Passed | Multi-version matrix OK |
| GitHub Actions (Unittest) | ✅ Passed | CI pipeline OK |

---

### 💬 Author
**Lochan Enugula**  
📧 enugula.l@northeastern.edu  
🔗 [GitHub: Lochan9](https://github.com/Lochan9)
