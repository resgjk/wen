from db.engine import Base

from sqlalchemy.orm import mapped_column, Mapped


class CategoryModel(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"{self.id}"
