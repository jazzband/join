"""

Revision ID: 0bc7f15b1164
Revises: 7f447c94347a
Create Date: 2017-11-19 22:22:16.026133
"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0bc7f15b1164"
down_revision = "7f447c94347a"


def upgrade():
    op.add_column("project_uploads", sa.Column("remote_addr", sa.Text(), nullable=True))
    op.add_column("project_uploads", sa.Column("user_agent", sa.Text(), nullable=True))


def downgrade():
    op.drop_column("project_uploads", "user_agent")
    op.drop_column("project_uploads", "remote_addr")
