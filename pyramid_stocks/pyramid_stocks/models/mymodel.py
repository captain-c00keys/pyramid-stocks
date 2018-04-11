
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    symbol = Column(Text, nullable=False, unique=True)
    companyName = Column(Text)
    exchange = Column(Text)
    website = Column(Text)
    CEO = Column(Text)
    industry = Column(Text)
    sector = Column(Text)
    issueType = Column(Text)
    description = Column(Text)
    

Index('my_index', MyModel.name, unique=True, mysql_length=255)
