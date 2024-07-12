"""

Revision ID: b72321d58252
Revises: 9cbd7c1a6757
Create Date: 2018-12-21 10:48:52.299292
"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b72321d58252"
down_revision = "9cbd7c1a6757"


def upgrade():
    op.add_column(
        "project_uploads", sa.Column("notified_at", sa.DateTime(), nullable=True)
    )
    op.add_column("project_uploads", sa.Column("ordering", sa.Integer(), nullable=True))
    op.create_index(
        op.f("ix_project_uploads_notified_at"),
        "project_uploads",
        ["notified_at"],
        unique=False,
    )


def downgrade():
    op.drop_index(op.f("ix_project_uploads_notified_at"), table_name="project_uploads")
    op.drop_column("project_uploads", "ordering")
    op.drop_column("project_uploads", "notified_at")
