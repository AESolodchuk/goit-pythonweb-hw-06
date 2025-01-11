from db import Base
from models.teachers import Teacher
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"), nullable=False)
    teachers: Mapped["Teacher"] = relationship("Teacher", back_populates="subjects")

    marks: Mapped[list["Mark"]] = relationship("Mark", back_populates="subject")
