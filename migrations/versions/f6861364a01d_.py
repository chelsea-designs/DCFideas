"""empty message

Revision ID: f6861364a01d
Revises: 
Create Date: 2022-07-07 12:35:38.855349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6861364a01d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'id',
               existing_type=sa.INTEGER(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('users', 'username',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('users', 'password',
               existing_type=sa.TEXT(),
               nullable=False)
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.alter_column('users', 'password',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('users', 'username',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('users', 'id',
               existing_type=sa.INTEGER(),
               server_default=sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###