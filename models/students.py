from db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    group_id: Mapped[int] = mapped_column(Integer, ForeignKey("groups.id"))
    email: Mapped[str] = mapped_column(String(50))
    group: Mapped["Group"] = relationship("Group", back_populates="students")
    marks: Mapped[list["Mark"]] = relationship("Mark", back_populates="student")
