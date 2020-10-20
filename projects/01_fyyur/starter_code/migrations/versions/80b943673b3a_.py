"""empty message

Revision ID: 80b943673b3a
Revises: 1b56f53f50d6
Create Date: 2020-10-20 23:20:21.053401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80b943673b3a'
down_revision = '1b56f53f50d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'Show', 'Venue', ['Venueid'], ['id'])
    op.create_foreign_key(None, 'Show', 'Artist', ['Artistid'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_constraint(None, 'Show', type_='foreignkey')
    # ### end Alembic commands ###