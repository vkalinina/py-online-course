from __future__ import annotations


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        result = days // 7
        return result if days % 7 == 0 else result + 1

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=OnlineCourse.days_to_weeks(course_dict["days"])
        )
