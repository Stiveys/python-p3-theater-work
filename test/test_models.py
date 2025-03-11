import pytest
import warnings
from sqlalchemy import exc as sa_exc

# Suppress SQLAlchemy warnings
warnings.filterwarnings('ignore', category=sa_exc.SAWarning)

from lib.db.models import Base, engine, session
from lib.models.role import Role
from lib.models.audition import Audition
from sqlalchemy import Integer

@pytest.fixture
def setup_database():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

def test_role_creation(setup_database):
    role = Role(character_name="Hamlet")
    session.add(role)
    session.commit()
    assert role.character_name == "Hamlet"

def test_audition_creation(setup_database):
    role = Role(character_name="Hamlet")
    session.add(role)
    session.commit()

    audition = Audition(
        actor="John Doe",
        location="New York",
        phone=1234567890,
        role=role
    )
    session.add(audition)
    session.commit()

    assert audition.actor == "John Doe"
    assert audition.role.character_name == "Hamlet"

def test_callback_functionality(setup_database):
    role = Role(character_name="Hamlet")
    audition = Audition(
        actor="John Doe",
        location="New York",
        phone=1234567890,
        role=role
    )
    session.add_all([role, audition])
    session.commit()

    audition.call_back()
    session.commit()
    assert audition.hired == True

def test_role_methods(setup_database):
    role = Role(character_name="Hamlet")
    audition1 = Audition(
        actor="John Doe",
        location="New York",
        phone=1234567890,
        role=role
    )
    audition2 = Audition(
        actor="Jane Smith",
        location="Los Angeles",
        phone=9876543210,
        role=role
    )
    session.add_all([role, audition1, audition2])
    session.commit()

    assert "John Doe" in role.actors()
    assert "Jane Smith" in role.actors()
    assert "New York" in role.locations()
    assert "Los Angeles" in role.locations()

    # Test lead and understudy
    assert role.lead() == "no actor has been hired for this role"
    audition1.call_back()
    session.commit()
    assert role.lead() == audition1
    assert role.understudy() == "no actor has been hired for understudy for this role"

    audition2.call_back()
    session.commit()
    assert role.understudy() == audition2