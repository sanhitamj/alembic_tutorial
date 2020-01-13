"""create name table

Revision ID: 65c136abff91
Revises:
Create Date: 2020-01-12 18:29:05.106135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65c136abff91'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        "create schema tutorial"
    )
    op.create_table(
        'names',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        schema='tutorial'
    )

def downgrade():
    op.drop_table('account')
    op.execute("drop schema tutorial")
