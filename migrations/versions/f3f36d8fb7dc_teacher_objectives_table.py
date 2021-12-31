"""teacher objectives table

Revision ID: f3f36d8fb7dc
Revises: 
Create Date: 2021-12-31 17:53:51.867236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3f36d8fb7dc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teacher_objectives',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teacher_objective_1', sa.String(length=100), nullable=True),
    sa.Column('teacher_objective_2', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teacher_objectives')
    # ### end Alembic commands ###
