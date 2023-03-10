"""initial6

Revision ID: e46e9bea4af3
Revises: 
Create Date: 2023-03-06 19:35:03.397145

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e46e9bea4af3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('analysis_sqlalchemy',
    sa.Column('an_id', sa.Integer(), nullable=False),
    sa.Column('an_name', sa.String(length=80), nullable=True),
    sa.Column('an_cost', sa.Float(), nullable=True),
    sa.Column('an_price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('an_id')
    )
    op.create_table('orders_sqlalchemy',
    sa.Column('ord_id', sa.Integer(), nullable=False),
    sa.Column('ord_datetime', sa.DateTime(), nullable=True),
    sa.Column('ord_an', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ord_an'], ['analysis_sqlalchemy.an_id'], ),
    sa.PrimaryKeyConstraint('ord_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders_sqlalchemy')
    op.drop_table('analysis_sqlalchemy')
    # ### end Alembic commands ###
