import enum
from datetime import date

from sqlalchemy import Date, String
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column

from ..data.database import Base


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
    location: Mapped[str] = mapped_column(String(20))
