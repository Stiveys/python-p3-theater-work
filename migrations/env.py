# Add this at the top of the file
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Import your models
from lib.db.models import Base
from lib.models.role import Role
from lib.models.audition import Audition

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# ... rest of the file ...