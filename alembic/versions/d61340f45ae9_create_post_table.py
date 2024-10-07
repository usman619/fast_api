"""create post table

Revision ID: d61340f45ae9
Revises: 
Create Date: 2024-10-07 18:51:42.616692

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd61340f45ae9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.INTEGER(), nullable=False, primary_key=True),
                    sa.Column('title',sa.String(), nullable=False),
                    sa.Column('content',sa.String(), nullable=False),
                    sa.Column('published',sa.Boolean(), nullable=False, server_default='True'),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
