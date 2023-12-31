"""more tables

Revision ID: ec6b8bc29cf6
Revises: f7394e257030
Create Date: 2023-10-27 08:40:27.712890

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec6b8bc29cf6'
down_revision: Union[str, None] = 'f7394e257030'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_status_id'), 'status', ['id'], unique=False)
    op.create_table('interventions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('statusid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['statusid'], ['status.id'], ),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_interventions_id'), 'interventions', ['id'], unique=False)
    op.create_table('redflag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('incident_type', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('additional_details', sa.String(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('statusid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['statusid'], ['status.id'], ),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_redflag_id'), 'redflag', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_redflag_id'), table_name='redflag')
    op.drop_table('redflag')
    op.drop_index(op.f('ix_interventions_id'), table_name='interventions')
    op.drop_table('interventions')
    op.drop_index(op.f('ix_status_id'), table_name='status')
    op.drop_table('status')
    # ### end Alembic commands ###
