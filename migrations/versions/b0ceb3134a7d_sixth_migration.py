"""Sixth migration

Revision ID: b0ceb3134a7d
Revises: f293121ec9a4
Create Date: 2019-04-21 20:33:39.105282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0ceb3134a7d'
down_revision = 'f293121ec9a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('author', sa.String(length=250), nullable=True))
    op.add_column('pitches', sa.Column('title', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'title')
    op.drop_column('pitches', 'author')
    # ### end Alembic commands ###
