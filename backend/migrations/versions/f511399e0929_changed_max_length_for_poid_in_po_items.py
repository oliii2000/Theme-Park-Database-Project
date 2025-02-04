"""added poitems/items relationship.

Revision ID: f511399e0929
Revises: b9465fcb48ad
Create Date: 2024-10-23 09:38:01.690810

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f511399e0929'
down_revision: Union[str, None] = 'b9465fcb48ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'purchaseorderitems', 'items', ['item_id'], ['sku'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'purchaseorderitems', type_='foreignkey')
    # ### end Alembic commands ###
