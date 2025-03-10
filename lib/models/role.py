from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from ..db.models import Base

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    character_name = Column(String)
    auditions = relationship('Audition', back_populates='role')

    def actors(self):
        return [audition.actor for audition in self.auditions]

    def locations(self):
        return [audition.location for audition in self.auditions]

    def lead(self):
        hired_auditions = [a for a in self.auditions if a.hired]
        return hired_auditions[0] if hired_auditions else 'no actor has been hired for this role'

    def understudy(self):
        hired_auditions = [a for a in self.auditions if a.hired]
        return hired_auditions[1] if len(hired_auditions) > 1 else 'no actor has been hired for understudy for this role'