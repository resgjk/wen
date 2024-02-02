from datetime import date

from db.engine import Base

from sqlalchemy import BIGINT
from sqlalchemy.orm import relationship, mapped_column, Mapped


class WalletModel(Base):
    __tablename__ = "wallets"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False)
    address: Mapped[str] = mapped_column(unique=True, nullable=False)
    rank: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"{self.id}"
