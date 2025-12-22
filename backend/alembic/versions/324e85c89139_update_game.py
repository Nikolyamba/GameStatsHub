"""update Game

Revision ID: 324e85c89139
Revises: 18808690fbf3
Create Date: 2025-12-09 11:52:06.719025

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '324e85c89139'
down_revision: Union[str, Sequence[str], None] = '18808690fbf3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
