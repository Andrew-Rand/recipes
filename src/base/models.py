from uuid import uuid4

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID

from src.base.utils.db.constants import Base


class BaseModel(Base):
    __abstract__ = True
    map_datetime_formats_to_return = {}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    date = Column(DateTime)

    class Meta:
        fields = ()
