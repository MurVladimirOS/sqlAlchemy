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
    # sa.Column('status', sa.Integer(), nullable=False)
    # op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))
    op.add_column('tmp', sa.Column('status', sa.Integer()))


def downgrade() -> None:
    op.drop_column('tmp', 'status')
