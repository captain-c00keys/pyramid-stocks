
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime
)

from .meta import Base


class Entry(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    symbol = Column(Text, nullable=False)
    companyName = Column(Text)
    exchange = Column(Text)
    website = Column(Text)
    CEO = Column(Text)
    industry = Column(Text)
    sector = Column(Text)
    issueType = Column(Text)
    description = Column(Text)
    

Index('my_index', Entry.id, unique=True, mysql_length=255)
