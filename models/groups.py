from db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    students: Mapped[list["Student"]] = relationship("Student", back_populates="group")
