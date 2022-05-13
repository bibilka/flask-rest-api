"""Models

Revision ID: c682ee480abd
Revises: 2c5fe10f680f
Create Date: 2022-05-13 14:44:09.971184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c682ee480abd'
down_revision = '2c5fe10f680f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('education_form',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_education_form_name'), 'education_form', ['name'], unique=True)
    op.create_table('qualification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_qualification_name'), 'qualification', ['name'], unique=True)
    op.create_table('speciality',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('profile', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_speciality_name'), 'speciality', ['name'], unique=True)
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('faculty', sa.String(length=150), nullable=True),
    sa.Column('course', sa.Integer(), nullable=True),
    sa.Column('students_count', sa.Integer(), nullable=True),
    sa.Column('subgroups_count', sa.Integer(), nullable=True),
    sa.Column('speciality_id', sa.Integer(), nullable=True),
    sa.Column('qualification_id', sa.Integer(), nullable=True),
    sa.Column('education_form_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['education_form_id'], ['education_form.id'], ),
    sa.ForeignKeyConstraint(['qualification_id'], ['qualification.id'], ),
    sa.ForeignKeyConstraint(['speciality_id'], ['speciality.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_group_name'), 'group', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_group_name'), table_name='group')
    op.drop_table('group')
    op.drop_index(op.f('ix_speciality_name'), table_name='speciality')
    op.drop_table('speciality')
    op.drop_index(op.f('ix_qualification_name'), table_name='qualification')
    op.drop_table('qualification')
    op.drop_index(op.f('ix_education_form_name'), table_name='education_form')
    op.drop_table('education_form')
    # ### end Alembic commands ###