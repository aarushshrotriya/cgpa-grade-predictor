import json
import os

class Assessment:
    def __init__(
            self,
            name: str,
            weightage: float,
            scored_marks: float,
            max_marks: float
    ):
        """
        Represents an individual assessment (e.g., Midterm Exam).
        - weightage: Percentage contribution to overall course grade (e.g., 30 for 30%).
        - scored_marks: Marks achieved by the student.
        - max_marks: Total possible marks for this assessment.
        """
        self.name = name
        self.weightage = weightage
        self.scored_marks = scored_marks
        self.max_marks = max_marks

    def get_weighted_score(self) -> float:
        """Calculates the weighted percentage contribution of this assessment."""
        if self.max_marks ==0:
            return 0.0
        return (self.scored_marks / self.max_marks) * self.weightage

    def to_dict(self) -> dict:
        """Converts the object to a dictionary for JSON serialization."""
        return{
            "name": self.name,
            "weightage": self.weightage,
            "scored_marks": self.scored_marks,
            "max_marks": self.max_marks,
        }

    @staticmethod
    def from_dict(data: dict):
        """Creates an Assessment instance from a dictionary."""
        return Assessment(
            data["name"],
            data["weightage"],
            data["scored_marks"],
            data["max_marks"]
        )

class Course:
    def __init__(
            self,
            course_code: str,
            course_name: str,
            credits: str
    ):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.assesments = []

    def add_assessment(self, assessment: Assessment):
        self.assesments.append(assessment)

    def get_total_weightage_logges(self) -> float:
        return sum(assessment.weightage for assessment in self.assesments)

    def get_current_weighted_percentage(self) -> float:
        return sum(assesment.get_weighted_score() for assesment in self.assessments) 

    def to_dict(self) -> dict:
        return {
            "course_code" : self.course_code,
            "course_name" : self.course_name,
            "credits" : self.credits,
            "assessments" : [assessment.to_dict() for assessment in self.assesments]
        }

    @staticmethod
    def from_dict(data: dict):
        course = Course(
            data["course_code"],
            data["course_name"],
            data["credits"]
        )
        for assessment_data in data.get("assessments", []):
            course.add_assessment(Assessment.from_dict(assessment_data))
        return course

class StorageManager:
    def __init__(self, filepath: str = "data.json"):
        self.filepath = filepath

    def save_data(self, courses: list):
        data = [course.to_dict() for course in courses]
        with open(self.filepath, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self) -> list:
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
                return [Course.from_dict(course_data) for course_data in data]
        except (json.JSONDecodeError, KeyError):
            return []
        