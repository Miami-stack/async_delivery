from sqlalchemy import Column, Integer, String, create_engine, Sequence
from sqlalchemy.ext.declarative import declarative_base
import config


Base = declarative_base()
metadata = Base.metadata


class Goods(Base):
    __tablename__ = "goods"

    id = Column(
        Integer,
        Sequence('goods_id_seq'),
        primary_key=True,
        comment="Идентификатор.",
    )

    identificator = Column(
        String,
        nullable=False,
        comment="идентификатор товара"
    )
    status = Column(
        String,
        nullable=False,
        unique=True,
        comment="статус доставки"
    )


engine = create_engine(config.ENGINE_STRING)
Base.metadata.create_all(engine)
del engine


