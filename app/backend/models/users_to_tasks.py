from db.engine import Base

from sqlalchemy import ForeignKey, BIGINT
from sqlalchemy.orm import Mapped, mapped_column


class UserToTaskModel(Base):
    __tablename__ = "users_to_tasks"

    user_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
    task_id: Mapped[int] = mapped_column(
        ForeignKey("tasks.id", ondelete="CASCADE"), primary_key=True
    )

    def __repr__(self) -> str:
        return f"{self.user_id} - {self.task_id}"
