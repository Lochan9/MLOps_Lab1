@'
# 🧠 MLOps Lab 1 – Automated Testing & Continuous Integration Pipeline

This repository showcases a **fully automated testing and CI/CD pipeline** integrating both `unittest` and `pytest` frameworks.  
It mirrors **real-world MLOps practices** by combining structured project organization, logging, validation, and continuous integration via GitHub Actions.

---

## 🚀 Key Highlights

| Feature | Description |
|----------|-------------|
| 🧩 **Dual Testing Frameworks** | Implements both `unittest` (for deterministic tests) and `pytest` (for parameterized validation). |
| ⚙️ **Automated CI/CD Pipeline** | GitHub Actions automatically runs both frameworks on each push or pull request to `main`. |
| 🧱 **Structured Repository Design** | Clean separation of source (`src/`), tests (`test/`), and automation (`.github/workflows/`). |
| 🧮 **Validation Layer** | Includes a `validate_pipeline.py` that verifies results and logs status with timestamps. |
| 🔁 **Reproducible Setup** | `requirements.txt` ensures deterministic environment setup. |
| 🧰 **Cross-Version Compatibility** | CI validated on Python 3.10, 3.11, and 3.12. |
| 📈 **End-to-End MLOps Workflow** | Combines local testing, CI validation, and result tracking under a single repository. |

---

## 🧩 Project Structure

MLOps_Lab1/  
│── src/  
│   ├── calculator.py                 → Core computation logic (add, subtract, multiply, aggregate)  
│   ├── validate_pipeline.py          → Logs, validates, and ensures data integrity  
│── test/  
│   ├── test_pytest.py                → Parameterized tests using pytest  
│   ├── test_unittest.py              → Functional tests using unittest  
│── .github/workflows/  
│   ├── pytest_action.yml             → CI workflow for pytest (multi-Python matrix)  
│   ├── unittest_action.yml           → CI workflow for unittest validation  
│── data/results.csv                  → Sample generated outputs  
│── requirements.txt                  → Dependency list  
│── README.md                         → Documentation file  

---

## ⚙️ Setup & Local Execution

```bash
# Clone the repository
git clone https://github.com/Lochan9/MLOps_Lab1.git
cd MLOps_Lab1

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run all local tests
python -m pytest -v
python -m unittest discover -s test -p "test_*.py" -v
