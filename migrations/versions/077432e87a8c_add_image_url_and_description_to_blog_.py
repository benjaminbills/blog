"""add image url and description to blog model

Revision ID: 077432e87a8c
Revises: 4a2a008b978d
Create Date: 2021-05-03 02:39:56.412499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '077432e87a8c'
down_revision = '4a2a008b978d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('description', sa.String(), nullable=True))
    op.add_column('blogs', sa.Column('urlToImage', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'urlToImage')
    op.drop_column('blogs', 'description')
    # ### end Alembic commands ###
