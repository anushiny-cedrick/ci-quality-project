# Continuous Integration (CI) Pipeline with Quality Gates (SonarQube)

## 1. Introduction

This project demonstrates the implementation of a **robust Continuous Integration (CI) pipeline** that enforces **quality gates** using automated build, unit testing, test coverage, and **static code analysis with SonarQube**. The goal is to improve **software reliability, maintainability, and early defect detection** by ensuring that only high‑quality code is accepted into the main branch.

The pipeline is implemented using **GitHub Actions** and is automatically triggered on every push or pull request to the `main` branch.

---

## 2. Objectives

The main objectives of this project are to:

* Automate the build and validation process
* Run unit tests on every code change
* Enforce a minimum test coverage threshold (≥ 80%)
* Perform static code analysis using SonarQube
* Apply quality gates to block low‑quality code
* Demonstrate CI reliability benefits

---

## 3. Tools and Technologies

* **Version Control:** Git & GitHub
* **CI Tool:** GitHub Actions
* **Programming Language:** Python
* **Testing Framework:** Pytest
* **Coverage Tool:** Pytest‑Cov
* **Static Analysis & Quality Gates:** SonarQube / SonarCloud

---

## 4. Project Structure

The project follows an industry‑standard folder structure:

```
ci-quality-project/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_main.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
├── sonar-project.properties
├── README.md
└── .gitignore
```

### Folder Description

* **app/**: Contains the main application source code
* **tests/**: Contains unit tests for the application
* **.github/workflows/**: Contains CI pipeline configuration
* **requirements.txt**: Lists project and CI dependencies
* **sonar-project.properties**: SonarQube configuration file

---

## 5. Application Code (Example)

**File:** `app/main.py`

```python
def add(a, b):
    return a + b
```

---

## 6. Unit Tests

**File:** `tests/test_main.py`

```python
from app.main import add

def test_add():
    assert add(2, 3) == 5
```

### Explanation

Unit tests verify individual components of the application in isolation. They ensure correctness and prevent regressions when new code is added.

---

## 7. Requirements File

**File:** `requirements.txt`

```txt
pytest
pytest-cov
sonar-scanner-cli
```

### Purpose

* Ensures consistent dependency installation
* Allows CI to recreate the same environment automatically

---

## 8. SonarQube Configuration

**File:** `sonar-project.properties`

```properties
sonar.projectKey=ci-quality-project
sonar.projectName=CI Quality Project
sonar.projectVersion=1.0

sonar.sources=app
sonar.tests=tests
sonar.python.coverage.reportPaths=coverage.xml
sonar.sourceEncoding=UTF-8
```

### Explanation

This file defines how SonarQube analyzes the project, including source code location, test files, and coverage report paths.

---

## 9. CI Pipeline Configuration

**File:** `.github/workflows/ci.yml`

```yaml
name: CI Pipeline with SonarQube Quality Gates

on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build-test-analyze:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run unit tests with coverage
      run: |
        pytest --cov=app --cov-report=xml --cov-fail-under=80

    - name: SonarQube Scan
      uses: SonarSource/sonarqube-scan-action@v2
      env:
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
        SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
```

---

## 10. Quality Gates

The CI pipeline enforces the following quality gates:

| Quality Gate    | Condition         |
| --------------- | ----------------- |
| Build           | Must succeed      |
| Test Coverage   | ≥ 80%             |
| Bugs            | 0 critical bugs   |
| Vulnerabilities | 0 security issues |
| Code Smells     | Within threshold  |

If any quality gate fails, the pipeline fails automatically.

---

## 11. Pipeline Execution Flow

1. Developer pushes code to GitHub
2. GitHub Actions triggers the CI pipeline
3. Dependencies are installed
4. Unit tests are executed
5. Coverage is calculated
6. SonarQube performs static analysis
7. Quality gates are evaluated
8. Pipeline passes or fails

---

## 12. Expected Results

* Green pipeline when all quality gates pass
* Red pipeline when coverage or quality rules fail
* SonarQube dashboard showing analysis results

---

## 13. Reliability Benefits

Implementing CI with quality gates improves software reliability by:

* Detecting errors early
* Preventing faulty code from being merged
* Enforcing consistent coding standards
* Improving maintainability and security
* Reducing debugging and maintenance costs

---

## 14. Conclusion

This project demonstrates a complete CI pipeline that integrates automated testing and static analysis with SonarQube quality gates. The approach ensures high‑quality, reliable, and maintainable software development practices.

---

## 15. One‑Line Summary (For Presentation)

> “This CI pipeline enforces automated testing and SonarQube quality gates to ensure reliable and high‑quality software delivery.”
