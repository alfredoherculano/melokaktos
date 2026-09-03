import enum
from datetime import date

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .data.database import Base


class Discipline(enum.Enum):
    SPORT = "sport"
    BOULDER = "boulder"


class Send_Type(enum.Enum):
    ONSIGHT = "onsight"
    FLASH = "flash"
    REDPOINT = "redpoint"
    ATTEMPT = "attempt"


class Climb(Base):
    __tablename__ = "climb_entry"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    discipline: Mapped[Discipline] = mapped_column(SqlEnum(Discipline))
    send_type: Mapped[Send_Type] = mapped_column(SqlEnum(Send_Type))
    send_date: Mapped[date] = mapped_column(Date)

    location_id: Mapped[int] = mapped_column(ForeignKey("location.id"))

    location: Mapped["Location"] = relationship(back_populates="climbs")

    def __repr__(self):
        return f"Climb(id={self.id!r}, name={self.name!r}, discipline={self.discipline}, send_type={self.send_type}, send_date={self.send_date!r})"


class Location(Base):
    __tablename__ = "location"

    id: Mapped[int] = mapped_column(primary_key=True)
    country: Mapped[str] = mapped_column(String(20))
    city: Mapped[str] = mapped_column(String(20))
    climbs: Mapped[list[Climb]] = relationship(back_populates="location")

    def __repr__(self):
        return f"Location(id={self.id!r}, country={self.country!r}, city={self.city!r})"
