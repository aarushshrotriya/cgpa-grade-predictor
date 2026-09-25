class VITPredictor:
    @staticmethod
    def predict_required_tee_marks(
        current_earned_weightage: float,
        target_total_marks: float
    ) -> dict:
        
        needed_weightage = target_total_marks - current_earned_weightage
        if needed_weightage <= 0:
            return{
                "achievable": True,
                "required_tee_marks": 0.0,
                "message": "Target already achieved!"
            }
        
        required_raw_tee = (needed_weightage / 40.0) * 100.0
        if required_raw_tee > 100.0:
            return {
                "achievable": False,
                "required_tee": round(required_raw_tee, 2),
                "message": f"Target unachievable. You need {round(required_raw_tee, 2)}/100 in TEE."
            }
        return{
            "achievable": True,
            "required_tee": round(required_raw_tee, 2),
            "message": f"You need at least {round(required_raw_tee, 2)}/100 in TEE to achieve {target_total_marks} total marks."
        }
    @staticmethod
    def get_medical_guidance_steps() -> list:
        """Returns the official procedure for attendance relaxation via medical request."""
        return [
            "Write a formal application requesting attendance condonation.",
            "Attach the original hardcopy of your medical consultation/documents.",
            "Obtain your respective Proctor's recommendation signature on the application.",
            "Submit the signed application and documents to the Parent Engagement and Academic Counselling Office for verification."
        ]