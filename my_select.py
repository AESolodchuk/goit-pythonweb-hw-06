from sqlalchemy import func
from db import session
from random import choice, randint
from faker import Faker
from models.groups import Group
from models.students import Student
from models.teachers import Teacher
from models.marks import Mark
from models.subjects import Subject
from datetime import date


def select_1():
    result = (
        session.query(Student.name, func.avg(Mark.mark))
        .join(Mark, Student.id == Mark.student_id)
        .group_by(Student.name)
        .order_by(func.avg(Mark.mark).desc())
        .limit(5)
        .all()
    )

    return result


if __name__ == "__main__":
    print(select_1())
