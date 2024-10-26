"""fixed cascade relationship with so/so detail.

Revision ID: c91663711da6
Revises: a6dc30d18933
Create Date: 2024-10-25 17:27:16.008752

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c91663711da6'
down_revision: Union[str, None] = 'a6dc30d18933'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('sales_orders_ibfk_2', 'sales_orders', type_='foreignkey')
    op.create_foreign_key(None, 'sales_orders', 'sales_order_details', ['detail_id'], ['detail_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('sales_orders_ibfk_2', 'sales_orders', type_='foreignkey')
    op.create_foreign_key('sales_orders_ibfk_2', 'sales_orders', 'sales_order_details', ['detail_id'], ['detail_id'], ondelete='CASCADE')
    # ### end Alembic commands ###
