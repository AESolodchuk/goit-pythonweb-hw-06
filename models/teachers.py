from db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String


class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    subjects = relationship("Subject", back_populates="teachers")
