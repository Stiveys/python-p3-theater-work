from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..db.models import Base

class Audition(Base):
    # Define the table name for SQLAlchemy
    __tablename__ = 'auditions'

    # Define columns for the auditions table
    id = Column(Integer, primary_key=True)
    actor = Column(String)
    location = Column(String)
    phone = Column(Integer)
    hired = Column(Boolean, default=False)
    # Foreign key to link audition with a role
    role_id = Column(Integer, ForeignKey('roles.id'))

    # Set up many-to-one relationship with Role model
    role = relationship('Role', back_populates='auditions')

    def call_back(self):
        # Method to mark an actor as hired for a role
        self.hired = True