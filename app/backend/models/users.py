from datetime import date

from db.engine import Base

from sqlalchemy import BIGINT
from sqlalchemy.orm import relationship, mapped_column, Mapped


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False)
    x_name: Mapped[str] = mapped_column(unique=True, nullable=False)
    wallet_addres: Mapped[str] = mapped_column(unique=True, nullable=False)
    wen_balance: Mapped[int] = mapped_column(nullable=False, default=0)
    tasks = Mapped[list["TaskModel"]] = relationship(
        back_populates="users", secondary="users_to_tasks"
    )
    ref_link: Mapped[str] = mapped_column(unique=True, nullable=True, default=None)

    def __repr__(self) -> str:
        return f"{self.id}"
