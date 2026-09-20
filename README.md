# VIT Grade & Attendance Predictor

A modular, test-driven Python command-line application built to streamline academic tracking for VIT University students. It automates weighted score calculations, evaluates attendance recovery options, predicts required exam marks for target grades, and provides offline data persistence using JSON.

---

## Table of Contents
- [Problem Statement](#problem-statement)
- [Objective](#objective)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [Running Unit Tests](#running-unit-tests)

---

## Problem Statement
VIT University students lack an integrated, offline-capable tool to track their weighted internal performance, verify attendance eligibility against university compliance thresholds, and forecast required TEE marks needed to hit target final grades.

## Objective
To develop a modular, test-driven Python CLI application that automates weighted academic score calculations, models attendance recovery paths, predicts target TEE requirements, and persists student records locally using JSON.

---

## Key Features

* **Weighted Score Calculation:** Computes course scores out of 100 based on CAT1 (30%), CAT2 (30%), TEE (40%), Internals (max 25), and Attendance (max 5).
* **Attendance Eligibility & Recovery:** Assesses the 75% attendance rule, calculates needed recovery classes, and displays medical condonation thresholds.
* **TEE Mark Prediction:** Determines the minimum exam score required on the TEE to achieve a desired overall course grade.
* **Local Data Management:** Saves and retrieves student course records offline using structured JSON storage.

---

## Tech Stack

* **Core Language:** Python 3.10+ (Object-Oriented Programming)
* **Testing Framework:** `unittest`
* **Data Layer:** JSON (`data/courses.json`)
* **UML & Diagrams:** Mermaid.js (Architecture, Class, Sequence, Use Case Diagrams)

---

## Project Architecture

```text
vit-grade-predictor/
├── data/
│   └── courses.json          # Persistent JSON storage for saved courses
├── docs/
│   ├── architecture.png      # System architecture diagram
│   ├── class_diagram.png     # Class diagram
│   ├── sequence_diagram.png  # Sequence diagram
│   └── usecase_diagram.png   # Use case diagram
├── src/
│   ├── __init__.py
│   ├── calculator.py         # Grade & attendance logic
│   ├── predictor.py          # Target TEE calculation engine
│   └── storage.py            # File read/write handler
├── tests/
│   ├── __init__.py
│   └── test_calculator.py    # Unit test suite
├── main.py                   # CLI entry point
└── README.md
```

---

## Installation & Setup

**1.Clone the repository:**

```bash
git clone [https://github.com/aarushshrotriya/cgpa-grade-predictor.git](https://github.com/aarushshrotriya/cgpa-grade-predictor.git)
cd cgpa-grade-predictor
```
**2.Verify Python installation:**
Ensure you have Python 3.10 or higher installed:

```bash
python --version
```

---

## Usage Guide
Run the main application from your terminal:

```bash
python main.py
```

---

## Interactive Options:

**1.Calculate Course Score & Check Attendance:** Enter continuous assessment scores and attendance numbers to compute your final weighted total out of 100.

**2.Attendance Recovery Check:** Verify if you satisfy the 75% threshold or see how many consecutive classes you need to attend to regain eligibility.

**3.Predict Required TEE Marks:** Enter your current internal aggregate and your target course grade to find out what score you must secure in TEE.

**4.View Saved Records:** Review previously calculated course scores stored in data/courses.json.

---

## Running Unit Tests
To run the automated unit test suite and verify calculations:

```bash
python -m unittest discover -s tests
```
