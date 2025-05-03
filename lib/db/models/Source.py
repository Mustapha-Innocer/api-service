from time import time

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from lib.db.session import Base


class Source(Base):
    __tablename__ = "source"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    country = Column(String, index=True, nullable=False)
    country_code = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(Integer, default=time(), nullable=False)
    stories = relationship("Story", back_populates="source")

    def __repr__(self):
        return "Source(id={}, name={}, country={}, country_code={}, created_at={})".format(
            self.id,
            self.name,
            self.country,
            self.country_code,
            self.created_at,
        )
