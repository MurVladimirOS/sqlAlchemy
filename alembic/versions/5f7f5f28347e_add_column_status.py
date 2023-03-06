"""add_column_status

Revision ID: 5f7f5f28347e
Revises: e46e9bea4af3
Create Date: 2023-03-06 20:13:27.077695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f7f5f28347e'
down_revision = 'e46e9bea4af3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('analysis_sqlalchemy', sa.Column('status', sa.Integer()))


def downgrade() -> None:
    op.drop_column('analysis_sqlalchemy', 'status')
