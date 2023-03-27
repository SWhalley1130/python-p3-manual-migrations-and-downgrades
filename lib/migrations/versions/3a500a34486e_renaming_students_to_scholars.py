"""Renaming students to scholars

Revision ID: 3a500a34486e
Revises: 791279dd0760
Create Date: 2023-03-27 14:23:28.670699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a500a34486e'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
