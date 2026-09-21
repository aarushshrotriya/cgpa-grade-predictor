import sys
from src.calculator import VITCalculator
from src.predictor import VITPredictor
from src.storage import Course, StorageManager

def display_menu():
    print("\n" + "=" * 45)
    print("  VIT ACADEMIC GRADE & ATTENDANCE TRACKER  ")
    print("=" * 45)
    print("1. Calculate Course Total Score")
    print("2. Check Attendance Eligibility & Recovery")
    print("3. Predict Required TEE Score for Target Grade")
    print("4. View Saved Courses")
    print("5. Exit")
    print("=" * 45)

def get_float_input(prompt: str, max_val: float) -> float:
    while True:
        try:
            val = float(input(prompt))
            if 0 <= val <= max_val:
                return val
            print(f"Invalid input. Value must be between 0 and {max_val}.")
        except ValueError:
            print("Invalid entry. Please enter a valid number.")

def handle_course_calculation(storage: StorageManager):
    print("\n--- Course Total Calculation ---")
    code = input("Enter Course Code (e.g., CSE1001): ").strip().upper()
    cat1 = get_float_input("Enter CAT 1 Marks (out of 50): ", 50.0)
    cat2 = get_float_input("Enter CAT 2 Marks (out of 50): ", 50.0)
    tee = get_float_input("Enter TEE Marks (out of 100): ", 100.0)
    internal = get_float_input("Enter Teacher Internal Marks (out of 25): ", 25.0)
    att_pct = get_float_input("Enter Attendance Percentage (%): ", 100.0)

    total = VITCalculator.calculate_course_total(cat1, cat2, tee, internal, att_pct)
    print(f"\n>> Final Score for {code}: {total} / 100")

    courses = storage.load_data()
    course = Course(code, code, 4)
    storage.save_data(courses + [course])
    print("Course record saved successfully.")

def handle_attendance_check():
    print("\n--- Attendance Eligibility Check ---")
    attended = int(get_float_input("Enter classes attended so far: ", 200))
    held = int(get_float_input("Enter total classes held so far: ", 200))
    remaining = int(get_float_input("Enter remaining classes before exam: ", 100))

    result = VITCalculator.check_attendance_eligibility(attended, held, remaining)
    print(f"\nCurrent Attendance: {result['current_pct']}%")
    print(f"Status: {result['message']}")

    if not result["eligible"]:
        if not result.get("can_recover", False):
            illness = input("\nWere you absent due to medical reasons/illness? (yes/no): ").strip().lower()
            if illness == "yes":
                print("\n--- Medical Condonation Application Steps ---")
                steps = VITPredictor.get_medical_guidance_steps()
                for idx, step in enumerate(steps, 1):
                    print(f"{idx}. {step}")
            else:
                print("Debarred, and medical condonation is not applicable. You cannot appear for the exam.")

def handle_target_prediction():
    print("\n--- TEE Target Score Predictor ---")
    earned = get_float_input("Enter total earned weightage so far (CAT1 + CAT2 + Internals + Attendance): ", 60.0)
    target = get_float_input("Enter your target total score (out of 100): ", 100.0)

    result = VITPredictor.predict_required_tee_marks(earned, target)
    print(f"\nResult: {result['message']}")

def main():
    storage = StorageManager()
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()
        if choice == "1":
            handle_course_calculation(storage)
        elif choice == "2":
            handle_attendance_check()
        elif choice == "3":
            handle_target_prediction()
        elif choice == "4":
            courses = storage.load_data()
            print(f"\nSaved Courses Count: {len(courses)}")
            for c in courses:
                print(f"- {c.course_code}")
        elif choice == "5":
            print("Exiting application. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()



