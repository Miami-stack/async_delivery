from sqlalchemy import Column, Integer, String, create_engine, Sequence, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
import config


Base = declarative_base()
metadata = Base.metadata


class Goods(Base):
    __tablename__ = "goods"

    identificator = Column(
        VARCHAR,
        Sequence('goods_id_seq'),
        nullable=False,
        primary_key=True,
        comment="Идентификатор.",
    )

    status = Column(
        VARCHAR,
        nullable=False,
        comment="статус доставки"
    )


engine = create_engine(config.ENGINE_STRING)
Base.metadata.create_all(engine)
del engine


