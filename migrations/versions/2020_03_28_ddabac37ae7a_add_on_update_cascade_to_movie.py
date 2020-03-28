"""Add on update cascade to movie

Revision ID: ddabac37ae7a
Revises: 20b585387c32
Create Date: 2020-03-28 12:21:47.985895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddabac37ae7a'
down_revision = '20b585387c32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user', 'movie', type_='foreignkey')
    op.create_foreign_key('user', 'movie', 'user', ['user_key'], ['key'], onupdate='cascade', ondelete='cascade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user', 'movie', type_='foreignkey')
    op.create_foreign_key('user', 'movie', 'user', ['user_key'], ['key'], ondelete='CASCADE')
    # ### end Alembic commands ###
