from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from ..db.models import Base

class Role(Base):
    # Define the table name for SQLAlchemy
    __tablename__ = 'roles'

    # Define columns for the roles table
    id = Column(Integer, primary_key=True)
    character_name = Column(String)
    # Set up one-to-many relationship with Audition model
    auditions = relationship('Audition', back_populates='role')

    def actors(self):
        # Returns a list of all actor names who auditioned for this role
        return [audition.actor for audition in self.auditions]

    def locations(self):
        # Returns a list of all locations where auditions were held for this role
        return [audition.location for audition in self.auditions]

    def lead(self):
        # Gets the first hired actor for this role
        # Returns a message if no actor has been hired
        hired_auditions = [a for a in self.auditions if a.hired]
        return hired_auditions[0] if hired_auditions else 'no actor has been hired for this role'

    def understudy(self):
        # Gets the second hired actor (understudy) for this role
        # Returns a message if no understudy has been hired
        hired_auditions = [a for a in self.auditions if a.hired]
        return hired_auditions[1] if len(hired_auditions) > 1 else 'no actor has been hired for understudy for this role'