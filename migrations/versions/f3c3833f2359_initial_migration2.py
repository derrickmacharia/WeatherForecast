"""Initial Migration2

<<<<<<< HEAD:migrations/versions/f3c3833f2359_initial_migration2.py
Revision ID: f3c3833f2359
Revises: 
Create Date: 2021-11-17 17:11:18.650306
=======
Revision ID: c576ff46569b
Revises: 
Create Date: 2021-11-18 10:09:46.399159
>>>>>>> 30a3e4b947d931a7f2f03217e565c3528ae6c28a:migrations/versions/c576ff46569b_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<< HEAD:migrations/versions/f3c3833f2359_initial_migration2.py
revision = 'f3c3833f2359'
=======
revision = 'c576ff46569b'
>>>>>>> 30a3e4b947d931a7f2f03217e565c3528ae6c28a:migrations/versions/c576ff46569b_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('pass_secure', sa.String(length=255), nullable=True),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('profile_pic_path', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
