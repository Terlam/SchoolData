"""Second Migration

Revision ID: 795bde6252df
Revises: 64b2c4731024
Create Date: 2020-12-04 06:34:47.529148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '795bde6252df'
down_revision = '64b2c4731024'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=300), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'school', ['rctds'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'school', type_='unique')
    op.drop_table('post')
    # ### end Alembic commands ###