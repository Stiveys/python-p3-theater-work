import pytest
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