"""added logic to generate random employee id.

Revision ID: 54ec4dbdd41b
Revises: d382a385b924
Create Date: 2024-10-23 06:49:17.955450

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '54ec4dbdd41b'
down_revision: Union[str, None] = 'd382a385b924'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employees', 'employee_id',
               existing_type=mysql.VARCHAR(length=7),
               type_=mysql.VARCHAR(length=8),
               existing_comment='Unique employee id (primary key)',
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employees', 'employee_id',
               existing_type=mysql.VARCHAR(length=8),
               type_=mysql.VARCHAR(length=7),
               existing_comment='Unique employee id (primary key)',
               existing_nullable=False)
    # ### end Alembic commands ###
