"""auto generate payment id and updated attribute types to nullable=False

Revision ID: d5c3fe172407
Revises: d29a8ed8bb02
Create Date: 2024-10-26 09:58:16.027013

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'd5c3fe172407'
down_revision: Union[str, None] = 'd29a8ed8bb02'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vendor_payments', 'vendor_payment_id',
               existing_type=mysql.INTEGER(),
               type_=mysql.VARCHAR(length=12),
               existing_comment='Unique identifier for each vendor payment',
               existing_nullable=False)
    op.alter_column('vendor_payments', 'payment_date',
               existing_type=sa.DATE(),
               nullable=False,
               existing_comment='Date when the payment was made')
    op.alter_column('vendor_payments', 'payment_amount',
               existing_type=mysql.DECIMAL(precision=7, scale=2),
               nullable=False,
               existing_comment='Amount paid to the vendor')
    op.alter_column('vendor_payments', 'payment_method_id',
               existing_type=mysql.INTEGER(),
               nullable=False,
               existing_comment='Foreign key linking to the payment method used')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vendor_payments', 'payment_method_id',
               existing_type=mysql.INTEGER(),
               nullable=True,
               existing_comment='Foreign key linking to the payment method used')
    op.alter_column('vendor_payments', 'payment_amount',
               existing_type=mysql.DECIMAL(precision=7, scale=2),
               nullable=True,
               existing_comment='Amount paid to the vendor')
    op.alter_column('vendor_payments', 'payment_date',
               existing_type=sa.DATE(),
               nullable=True,
               existing_comment='Date when the payment was made')
    op.alter_column('vendor_payments', 'vendor_payment_id',
               existing_type=mysql.VARCHAR(length=12),
               type_=mysql.INTEGER(),
               existing_comment='Unique identifier for each vendor payment',
               existing_nullable=False)
    # ### end Alembic commands ###
