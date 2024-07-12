"""

Revision ID: 17164a7d1c2e
Revises: cc0e3906ecfb
Create Date: 2017-09-28 19:53:27.500788
"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "17164a7d1c2e"
down_revision = "cc0e3906ecfb"


def upgrade():
    op.create_table(
        "project_members",
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("project_id", sa.Integer(), nullable=True),
        sa.Column("date_joined", sa.DateTime(), nullable=True),
        sa.Column("is_lead", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(["project_id"], ["projects.id"]),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
    )
    op.create_index(
        op.f("ix_project_members_is_lead"), "project_members", ["is_lead"], unique=False
    )
    op.create_table(
        "project_uploads",
        sa.Column("synced_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=True),
        sa.Column("version", sa.Text(), nullable=True),
        sa.Column("path", sa.Text(), nullable=True),
        sa.Column("filename", sa.Text(), nullable=True),
        sa.Column("signature", sa.Text(), nullable=False),
        sa.Column("size", sa.Integer(), nullable=True),
        sa.Column("md5_digest", sa.Text(), nullable=False),
        sa.Column("sha256_digest", sa.Text(), nullable=False),
        sa.Column("blake2_256_digest", sa.Text(), nullable=False),
        sa.Column("upload_time", sa.DateTime(), nullable=True),
        sa.CheckConstraint("blake2_256_digest ~* '^[A-F0-9]{64}$'"),
        sa.CheckConstraint("sha256_digest ~* '^[A-F0-9]{64}$'"),
        sa.ForeignKeyConstraint(["project_id"], ["projects.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("blake2_256_digest"),
        sa.UniqueConstraint("md5_digest"),
        sa.UniqueConstraint("sha256_digest"),
        sa.UniqueConstraint("signature"),
    )
    op.create_index(
        op.f("ix_project_uploads_filename"),
        "project_uploads",
        ["filename"],
        unique=True,
    )
    op.create_index(
        op.f("ix_project_uploads_path"), "project_uploads", ["path"], unique=True
    )
    op.create_index(
        op.f("ix_project_uploads_version"), "project_uploads", ["version"], unique=False
    )
    op.create_index(
        "project_uploads_project_version",
        "project_uploads",
        ["project_id", "version"],
        unique=False,
    )
    op.add_column(
        "projects", sa.Column("client_id", postgresql.UUID(as_uuid=True), nullable=True)
    )
    op.add_column(
        "projects",
        sa.Column("secret_key", postgresql.UUID(as_uuid=True), nullable=True),
    )
    op.create_index("release_name_idx", "projects", ["name"], unique=False)
    op.create_index(
        "release_name_is_active_idx", "projects", ["name", "is_active"], unique=False
    )


def downgrade():
    op.drop_index("release_name_is_active_idx", table_name="projects")
    op.drop_index("release_name_idx", table_name="projects")
    op.drop_column("projects", "secret_key")
    op.drop_column("projects", "client_id")
    op.drop_index("project_uploads_project_version", table_name="project_uploads")
    op.drop_index(op.f("ix_project_uploads_version"), table_name="project_uploads")
    op.drop_index(op.f("ix_project_uploads_path"), table_name="project_uploads")
    op.drop_index(op.f("ix_project_uploads_filename"), table_name="project_uploads")
    op.drop_table("project_uploads")
    op.drop_index(op.f("ix_project_members_is_lead"), table_name="project_members")
    op.drop_table("project_members")
