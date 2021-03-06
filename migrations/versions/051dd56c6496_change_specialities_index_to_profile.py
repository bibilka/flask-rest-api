"""change specialities index to profile

Revision ID: 051dd56c6496
Revises: bb9f8e008b53
Create Date: 2022-05-13 21:15:13.109332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '051dd56c6496'
down_revision = 'bb9f8e008b53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_speciality_name', table_name='speciality')
    op.create_index(op.f('ix_speciality_profile'), 'speciality', ['profile'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_speciality_profile'), table_name='speciality')
    op.create_index('ix_speciality_name', 'speciality', ['name'], unique=False)
    # ### end Alembic commands ###
