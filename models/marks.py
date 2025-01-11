from db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, Date


class Mark(Base):
    __tablename__ = "marks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[Date] = mapped_column(Date)
    mark: Mapped[int] = mapped_column(Integer)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("students.id"))
    student: Mapped["Student"] = relationship("Student", back_populates="marks")

    subject_id: Mapped[int] = mapped_column(Integer, ForeignKey("subjects.id"))
    subject: Mapped["Subject"] = relationship("Subject", back_populates="marks")
