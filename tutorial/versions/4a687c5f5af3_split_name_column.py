"""split name column

Revision ID: 4a687c5f5af3
Revises: 65c136abff91
Create Date: 2020-01-12 18:35:50.911206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a687c5f5af3'
down_revision = '65c136abff91'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('names', 'name', nullable=True, schema='tutorial')
    op.add_column('names',
        sa.Column('first_name', sa.String(), nullable=True),
        schema='tutorial')
    op.add_column('names',
        sa.Column('last_name', sa.String(), nullable=True),
        schema='tutorial'
)


def downgrade():
    op.drop_column('names', 'last_name', schema='tutorial')
    op.drop_column('names', 'first_name', schema='tutorial')
