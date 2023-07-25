"""empty message

Revision ID: 8442fa316dde
Revises: ff94f73acacf
Create Date: 2023-07-24 18:47:12.171173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8442fa316dde'
down_revision = 'ff94f73acacf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
