class VITCalculator:

    @staticmethod
    def calculate_attendance_score(attendance_percentage: float) -> int:
        """Return 5 Marks if attendance >= 75%, otherwise give 0."""
        return 5 if attendance_percentage >= 75.0 else 0

    @staticmethod
    def calculate_course_total(
        cat1: float,
        cat2: float,
        tee: float,
        internal: float,
        attendance_pct: float,
    ) -> float:
        """
            Calculates total final score out of 100 based on VIT grading system:
            - CAT 1: 30% of raw score (Max 50 raw -> 15 weight)
            - CAT 2: 30% of raw score (Max 50 raw -> 15 weight)
            - TEE: 40% of raw score (Max 100 raw -> 40 weight)
            - Teacher Internals: out of 25 weight
            - Attendance: 5 marks if >= 75%, else 0
        """
        # Compress CAT 1 & 2 by taking 30% of the raw score out of 50
        w_cat1 = min(cat1, 50.0) * 0.30
        w_cat2 = min(cat2, 50.0) * 0.30
        # Compress TEE by taking 40% of the raw score out of 100
        w_tee = min(tee, 100) * 0.40
        w_internal = min(internal, 25.0)
        w_att = VITCalculator.calculate_attendance_score(attendance_pct)
        return round(w_cat1 + w_cat2 + w_tee + w_internal + w_att, 2)

    @staticmethod
    def check_attendance_eligibility(
        attended_classes: int,
        total_classes_held: int,
        remaining_classes: int,
    ) -> dict:
        """Evaluates attendance eligibility and recovery options."""
        current_pct = (attended_classes / total_classes_held * 100) if total_classes_held > 0 else 0.0
        if current_pct >= 75.0:
            return {
                "eligible": True,
                "current_pct": round(current_pct, 2),
                "message": "Eligible to write the upcoming exam",
            }

        # Check if 75% is achievable by attending all remaining classes
        max_possible_attended = attended_classes + remaining_classes
        max_possible_total = total_classes_held + remaining_classes
        max_possible_pct = (max_possible_attended / max_possible_total * 100) if max_possible_total > 0 else 0.0
        if max_possible_pct >= 75.0:
            # Calculate minimum extra classes needed
            classes_needed = 0
            for extra in range(1, remaining_classes + 1):
                pct = ((attended_classes + extra) / (total_classes_held + extra)) * 100
                if pct >= 75.0:
                    classes_needed = extra
                    break
            return {
                "eligible": False,
                "can_recover": True,
                "current_pct": round(current_pct, 2),
                "classes_needed": classes_needed,
                "message": f"Debarred currently. You must attend at least {classes_needed} out of {remaining_classes} remaining classes to reach 75%.",
            }

        return {
            "eligible": False,
            "current_pct": round(current_pct, 2),
            "max_possible_pct": round(max_possible_pct, 2),
            "message": "Debarred. Even with 100% attendance in remaining classes, you cannot reach 75%.",
        }