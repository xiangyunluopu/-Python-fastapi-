from fastapi import APIRouter

from models.models import *
# from ORMTest.models.models import *

from models.base_models import *

student_api = APIRouter()


@student_api.get("/")
async def get_students():
    students = await Student.all()
    print(students)
    print(type(students))
    return {"students": students}


@student_api.get("/{student_id}")
async def get_student(student_id: int):
    exclude_fields = ["student_pwd", 'student_id']
    student = await Student.get(student_id=student_id)
    student.student_pwd = None
    print(student)
    print(type(student))
    return student

