from db.engine import Base

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped


class TaskModel(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False)
    coast: Mapped[int] = mapped_column(nullable=False)
    users: Mapped[list["UserModel"]] = relationship(
        back_populates="tasks", secondary="users_to_tasks"
    )
    category: Mapped["CategoryModel"] = mapped_column(
        ForeignKey("categories.id"), nullable=False
    )

    def __repr__(self) -> str:
        return f"{self.id}"
