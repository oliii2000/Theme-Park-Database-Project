"""changed dtype of supplies id and vendor id in parent and child tables.

Revision ID: 534ad65d83ab
Revises: 1117a731154a
Create Date: 2024-10-23 10:11:39.982176

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '534ad65d83ab'
down_revision: Union[str, None] = '1117a731154a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Drop foreign key constraints
    op.drop_constraint('items_ibfk_1', 'items', type_='foreignkey')
    # op.drop_constraint('orderdetails_ibfk_1', 'orderdetails', type_='foreignkey')
    # op.drop_constraint('orderdetails_ibfk_2', 'orderdetails', type_='foreignkey')
    # op.drop_constraint('purchaseorders_ibfk_1', 'purchaseorders', type_='foreignkey')
    # op.drop_constraint('supplies_ibfk_1', 'supplies', type_='foreignkey')
    # op.drop_constraint('vendor_payments_ibfk_1', 'vendor_payments', type_='foreignkey')
    # op.drop_constraint('vendors_ibfk_1', 'vendors', type_='foreignkey')

    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('items', 'vendor_id',
               existing_type=mysql.INTEGER(),
               type_=mysql.VARCHAR(length=12),
               existing_comment='Foreign key linking to the VendorID from the vendors table',
               existing_nullable=False)
    op.alter_column('orderdetails', 'order_details_id',
               existing_type=mysql.INTEGER(),
               type_=mysql.VARCHAR(length=12),
               existing_comment='Unique ID for each order detail',
               existing_nullable=False)
    op.alter_column('orderdetails', 'supply_id',
               existing_type=mysql.INTEGER(),
               type_=mysql.VARCHAR(length=12),
               existing_comment='ID of the related supply',
               existing_nullable=False)
    op.alter_column('purchaseorders', 'vendor_id',
               existing_type=mysql.INTEGER(),
               type_=mysql.VARCHAR(length=12),
               existing_comment='ID of the vendor that created the order',
               existing_nullable=False)
    op.alter_column('supplies', 'supply_id',
               existing_type=mysql.INTEGER(),
               type_=mysql.VARCHAR(length=12),
               existing_comment='Unique identifier for each supply item',
               existing_nullable=False)
    op.alter_column('supplies', 'vendor_id',
               existing_type=mysql.INTEGER(),
               type_=mysql.VARCHAR(length=12),
               existing_comment='Foreign key linking supply to the vendor providing it',
               existing_nullable=False)
    op.alter_column('vendor_payments', 'vendor_id',
               existing_type=mysql.INTEGER(),
               type_=mysql.VARCHAR(length=12),
               existing_comment='Foreign key linking to the Vendor receiving the payment',
               existing_nullable=False)
    op.alter_column('vendors', 'vendor_id',
               existing_type=mysql.INTEGER(),
               type_=mysql.VARCHAR(length=12),
               existing_comment='Unique identifier for the vendor',
               existing_nullable=False)
    # ### end Alembic commands ###

    # Recreate foreign key constraints
    op.create_foreign_key('items_ibfk_1', 'items', 'vendors', ['vendor_id'], ['vendor_id'])
    op.create_foreign_key('orderdetails_ibfk_1', 'orderdetails', 'purchaseorders', ['order_id'], ['order_id'])
    op.create_foreign_key('orderdetails_ibfk_2', 'orderdetails', 'supplies', ['supply_id'], ['supply_id'])
    op.create_foreign_key('purchaseorders_ibfk_1', 'purchaseorders', 'vendors', ['vendor_id'], ['vendor_id'])
    op.create_foreign_key('supplies_ibfk_1', 'supplies', 'vendors', ['vendor_id'], ['vendor_id'])
    op.create_foreign_key('vendor_payments_ibfk_1', 'vendor_payments', 'vendors', ['vendor_id'], ['vendor_id'])
    # Add any additional foreign key constraints as necessary


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vendors', 'vendor_id',
               existing_type=mysql.VARCHAR(length=12),
               type_=mysql.INTEGER(),
               existing_comment='Unique identifier for the vendor',
               existing_nullable=False)
    op.alter_column('vendor_payments', 'vendor_id',
               existing_type=mysql.VARCHAR(length=12),
               type_=mysql.INTEGER(),
               existing_comment='Foreign key linking to the Vendor receiving the payment',
               existing_nullable=False)
    op.alter_column('supplies', 'vendor_id',
               existing_type=mysql.VARCHAR(length=12),
               type_=mysql.INTEGER(),
               existing_comment='Foreign key linking supply to the vendor providing it',
               existing_nullable=False)
    op.alter_column('supplies', 'supply_id',
               existing_type=mysql.VARCHAR(length=12),
               type_=mysql.INTEGER(),
               existing_comment='Unique identifier for each supply item',
               existing_nullable=False)
    op.alter_column('purchaseorders', 'vendor_id',
               existing_type=mysql.VARCHAR(length=12),
               type_=mysql.INTEGER(),
               existing_comment='ID of the vendor that created the order',
               existing_nullable=False)
    op.alter_column('orderdetails', 'supply_id',
               existing_type=mysql.VARCHAR(length=12),
               type_=mysql.INTEGER(),
               existing_comment='ID of the related supply',
               existing_nullable=False)
    op.alter_column('orderdetails', 'order_details_id',
               existing_type=mysql.VARCHAR(length=12),
               type_=mysql.INTEGER(),
               existing_comment='Unique ID for each order detail',
               existing_nullable=False)
    op.alter_column('items', 'vendor_id',
               existing_type=mysql.VARCHAR(length=12),
               type_=mysql.INTEGER(),
               existing_comment='Foreign key linking to the VendorID from the vendors table',
               existing_nullable=False)
    # ### end Alembic commands ###
