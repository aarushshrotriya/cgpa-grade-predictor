# Problem Statement & System Requirements

## 1. Problem Statement
VIT university conducts a weighted relative evaluation with a mandatory 75% attendance or more for appearing for exams. Students often find it hard to calculate their aggregate internals, determine what marks they require in exams to get a certain target score, and assess their options for recovery if their attendance falls below the required threshold.

The proposed solution is a set of command line utilities to estimate grades, estimate required TEE scores, and suggest possible options of recovery and medical condonation for attendance.
---

## 2. Functional Requirements
- FR1: Calculate course score: Aggregate CAT1 (30%), CAT2 (30%), TEE (40%), teacher internas (25 max), and attendance (5 marks if ≥75%).
- FR2: Determine attendance eligibility and recovery: Check if attendance is is ≥75%; calculate minimum number of classes needed to attend if debarred but can recover attendance; help the user through medical condonation if the attendance is not recoverable.
- FR3: Determine score: Calculate raw score needed in TEE to get a certain target score.
- FR4: Storage of course records: Store and retrieve records of courses using local JSON storage.
---

## 3. Non-Functional Requirements
- NFR1: Usability: Provide a simple interface which makes use of numbered menus and interactive dialogues.
- NFR2: Maintainability: Be well factored into separate modules for storage (`storage.py`), calculation (`calculator.py`, `predictor.py`) and interface (main.py) so that changes in one part do not directly affect the others.
- NFR3: Robustness: Make sure that invalid inputs are properly handled. This includes invalid numbers, string inputs where numbers are expected, and unexpected system errors while reading/writing files.
- NFR4: Efficiency: Do not use excessive resources and have fast runtimes (ideally using standard libraries only). No single operation should take more than 50 MSC to complete.