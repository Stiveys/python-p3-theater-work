import warnings
from sqlalchemy import exc as sa_exc

# Suppress SQLAlchemy warnings
warnings.filterwarnings('ignore', category=sa_exc.SAWarning)

from lib.db.models import Base, engine, session
from lib.models.role import Role
from lib.models.audition import Audition

# Create tables
Base.metadata.create_all(engine)

# Clear existing data
session.query(Audition).delete()
session.query(Role).delete()
session.commit()

# Create roles
hamlet = Role(character_name="Hamlet")
ophelia = Role(character_name="Ophelia")
session.add_all([hamlet, ophelia])
session.commit()

# Create auditions
audition1 = Audition(actor="John Doe", location="New York", phone=1234567890, role=hamlet)
audition2 = Audition(actor="Jane Smith", location="Los Angeles", phone=9876543210, role=hamlet)
audition3 = Audition(actor="Emily Johnson", location="Chicago", phone=5551234567, role=ophelia)
audition4 = Audition(actor="Michael Brown", location="Boston", phone=7778889999, role=ophelia)
session.add_all([audition1, audition2, audition3, audition4])
session.commit()

# Test callback functionality
audition1.call_back()
audition3.call_back()
audition4.call_back()
session.commit()

# Display data
print("\n=== ROLES ===")
for role in session.query(Role).all():
    print(f"Role: {role.character_name}")
    print(f"  Actors: {role.actors()}")
    print(f"  Locations: {role.locations()}")
    print(f"  Lead: {role.lead()}")
    print(f"  Understudy: {role.understudy()}")
    print()

print("=== AUDITIONS ===")
for audition in session.query(Audition).all():
    print(f"Actor: {audition.actor}")
    print(f"  Role: {audition.role.character_name}")
    print(f"  Location: {audition.location}")
    print(f"  Hired: {audition.hired}")
    print()