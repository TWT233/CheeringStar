from sqlalchemy import Column, Integer

from .init import Base


class Binding(Base):
    __tablename__ = 'binding'

    discord_id = Column(Integer, primary_key=True)
    t1_1 = Column(Integer)
    t1_2 = Column(Integer)
    t2_1 = Column(Integer)
    t2_2 = Column(Integer)
    t3_1 = Column(Integer)
    t3_2 = Column(Integer)
    t4_1 = Column(Integer)
    t4_2 = Column(Integer)
