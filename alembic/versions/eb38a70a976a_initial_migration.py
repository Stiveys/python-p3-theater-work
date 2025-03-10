"""Initial migration

Revision ID: eb38a70a976a
Revises: 8fba589c887b
Create Date: 2025-03-10 12:03:54.462599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb38a70a976a'
down_revision: Union[str, None] = '8fba589c887b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
