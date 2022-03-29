"""add analytics model

Revision ID: be1f942eba28
Revises: 4bb882a7f9b5
Create Date: 2022-03-17 18:50:15.961217+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be1f942eba28'
down_revision = '4bb882a7f9b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('analytics',
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('type', sa.Enum('vulnerabilities_per_host', 'vulnerabilities_per_status', 'vulnerabilities_per_severity', 'top_ten_most_affected_hosts', 'top_ten_most_repeated_vulns', 'month_evolution_by_status', 'month_evolution_by_severity', name='analytics_types'), nullable=False),
    sa.Column('filters', sa.JSON(), nullable=False),
    sa.Column('workspaces', sa.JSON(), nullable=False),
    sa.Column('hosts', sa.JSON(), nullable=False),
    sa.Column('data', sa.JSON(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.Column('update_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['creator_id'], ['faraday_user.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['update_user_id'], ['faraday_user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('analytics')
    op.execute("DROP TYPE analytics_types")
    # ### end Alembic commands ###
