import uuid
from datetime import UTC, datetime

from sqlalchemy import CheckConstraint, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class Event(Base):
    __tablename__ = "events"
    __table_args__ = (CheckConstraint("impact >= -10 AND impact <= 10", name="impact_range"),)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    date = Column(DateTime(timezone=True), nullable=False)
    mood = Column(String, nullable=True)
    impact = Column(Integer, nullable=True)

    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC))

    user = relationship("User", back_populates="events")


class EventRelation(Base):
    __tablename__ = "event_relations"
    __table_args__ = (CheckConstraint("strength >= 1 AND strength <= 5", name="strength_range"),)

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)

    from_event_id = Column(UUID(as_uuid=True), ForeignKey("events.id", ondelete="CASCADE"), nullable=False)
    to_event_id = Column(UUID(as_uuid=True), ForeignKey("events.id", ondelete="CASCADE"), nullable=False)

    description = Column(String, nullable=True)
    strength = Column(Integer, nullable=True)

    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    from_event = relationship("Event", foreign_keys=[from_event_id])
    to_event = relationship("Event", foreign_keys=[to_event_id])
