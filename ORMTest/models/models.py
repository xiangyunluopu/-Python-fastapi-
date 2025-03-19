from tortoise import Model, fields
from dataclasses import dataclass

class Clazz(Model):
    class_id = fields.IntField(pk=True)
    class_name = fields.CharField(max_length=20, unique=True, description="班级名称")

class Teacher(Model):
    teacher_id = fields.IntField(pk=True)
    teacher_name = fields.CharField(max_length=64, description="教师名称")
    teacher_no = fields.CharField(max_length=12, description="工号")
    teacher_password = fields.CharField(max_length=128, description="教师密码")

@dataclass
class Student(Model):
    student_id = fields.IntField(pk=True)
    student_name = fields.CharField(max_length=64, description="学生姓名")
    student_no = fields.IntField(description="学号")
    student_pwd = fields.CharField(max_length=128, description="学生密码")
    student_class = fields.ForeignKeyField("models.Clazz", related_name="students")
    student_courses = fields.ManyToManyField("models.Course", related_name="students")
    student_description = fields.TextField(description="学生描述")

class Course(Model):
    course_id = fields.IntField(pk=True)
    course_name = fields.CharField(max_length=64, description="课程名称")
    course_teacher = fields.ForeignKeyField("models.Teacher", related_name="courses")
    course_student = fields.ManyToManyField("models.Student", related_name="courses")