"""changed max length for poid in po items.

Revision ID: 1117a731154a
Revises: f511399e0929
Create Date: 2024-10-23 09:40:56.998926

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '1117a731154a'
down_revision: Union[str, None] = 'f511399e0929'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('purchaseorderitems', 'poid',
               existing_type=mysql.VARCHAR(length=10),
               type_=mysql.VARCHAR(length=12),
               existing_comment='Foreign key to the Purchase Order table.',
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('purchaseorderitems', 'poid',
               existing_type=mysql.VARCHAR(length=12),
               type_=mysql.VARCHAR(length=10),
               existing_comment='Foreign key to the Purchase Order table.',
               existing_nullable=False)
    # ### end Alembic commands ###
