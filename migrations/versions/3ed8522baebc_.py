"""empty message

Revision ID: 3ed8522baebc
Revises: 7f881f2ca3f2
Create Date: 2020-04-24 19:50:44.422864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ed8522baebc'
down_revision = '7f881f2ca3f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stream_game', sa.Column('jitsi_hashid', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stream_game', 'jitsi_hashid')
    # ### end Alembic commands ###
