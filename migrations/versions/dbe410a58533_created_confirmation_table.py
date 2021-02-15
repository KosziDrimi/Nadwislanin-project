"""created confirmation table

Revision ID: dbe410a58533
Revises: 2ebc3bd75440
Create Date: 2021-02-06 16:47:49.936025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbe410a58533'
down_revision = '2ebc3bd75440'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('confirmation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('confirmation', sa.Text(), nullable=True),
    sa.Column('res_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['res_id'], ['reservation.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('confirmation')
    # ### end Alembic commands ###
