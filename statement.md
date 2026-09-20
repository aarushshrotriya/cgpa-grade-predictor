# Project Statement & Scope

## 1. Problem Statement
VIT University students often struggle to maintain an accurate real-time understanding of their academic performance due to complex grading distributions and strict attendance policies. Specifically:
- **Weighted Internal Calculations:** Calculating overall course marks manually across CAT1, CAT2, TEE, Teacher Internals, and Attendance marks can lead to errors.
- **Attendance Compliance Thresholds:** VIT mandates a 75% attendance rule. Students lack a simple tool to calculate how many consecutive classes they must attend to recover from a shortfall or to identify medical condonation eligibility.
- **Goal-Oriented Exam Planning:** Before appearing for Terminal End Examinations (TEE), students need to calculate the exact exam score required to achieve their desired target final grade.

This project addresses these challenges by offering a lightweight, test-driven, and offline-capable Python CLI application.

---

## 2. Scope of the Project

### In-Scope:
- **Weighted Course Total Calculation:** Computing final course scores out of 100 using VIT's weightage formula (CAT1 30%, CAT2 30%, TEE 40%, Internals up to 25, Attendance up to 5).
- **Attendance Eligibility & Recovery:** Calculating exact attendance percentages, identifying eligibility status, and computing mandatory recovery classes to reach 75%.
- **Target TEE Grade Predictor:** Forecasting minimum required TEE scores to hit specific target grades based on pre-TEE internal aggregates.
- **Local Data Persistence:** Saving, loading, and viewing semester course records locally using structured JSON storage (`data/courses.json`).
- **Test-Driven Verification:** Unit testing core logic using Python's `unittest` framework to ensure formula correctness.

### Out-of-Scope:
- Direct API integration with the VTOP (VIT Online Portal) server.
- Multi-user authentication/cloud database hosting.
- Graphical User Interface (GUI) or mobile app interface (strictly CLI-based).

---

## 3. Target Users
- **VIT University Undergraduate & Postgraduate Students:** Students seeking an offline tool to track academic progress, plan exam targets, and monitor attendance compliance.
- **Academic Mentors & Advisors:** Faculty advisors looking for a fast mechanism to guide students on attendance recovery requirements and grade targets.

---

## 4. High-Level Features
- **Calculations Engine:** Accurate mathematical modeling for continuous assessment tests, internals, and final exam scaling.
- **Compliance & Recovery Modeling:** Dynamic calculations for missing classes needed to satisfy the 75% threshold.
- **Grade Predictor Engine:** Goal-oriented target score forecasting for TEE examinations.
- **JSON Storage Handler:** File-based data persistence for course history management across CLI sessions.
- **Automated Test Suite:** Comprehensive unit tests validating calculation accuracy and edge-case handling.