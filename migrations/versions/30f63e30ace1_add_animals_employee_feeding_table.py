"""add animals,employee, feeding table

Revision ID: 30f63e30ace1
Revises: 
Create Date: 2024-02-22 22:00:57.157319

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '30f63e30ace1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('animals', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.BIGINT(),
               server_default=None,
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
        batch_op.alter_column('kingdom_class',
               existing_type=sa.VARCHAR(),
               nullable=False,
               comment=None,
               existing_comment='class of animals')
        batch_op.alter_column('type_of_food',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.drop_table_comment(
        existing_comment='this is table for project zoo '
    )
        batch_op.drop_column('conservation_at')

    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.BIGINT(),
               server_default=None,
               existing_nullable=False,
               autoincrement=True)
        batch_op.alter_column('age',
               existing_type=sa.SMALLINT(),
               type_=sa.Integer(),
               existing_nullable=False)
        batch_op.alter_column('section_operation',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.drop_table_comment(
        existing_comment='zoo Employee table'
    )
        batch_op.drop_column('join_at')

    with op.batch_alter_table('feeding_schedule', schema=None) as batch_op:
        batch_op.alter_column('no',
               existing_type=sa.BIGINT(),
               server_default=None,
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
        batch_op.alter_column('animal_id',
               existing_type=sa.BIGINT(),
               type_=sa.Integer(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feeding_schedule', schema=None) as batch_op:
        batch_op.alter_column('animal_id',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=False)
        batch_op.alter_column('no',
               existing_type=sa.Integer(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1),
               type_=sa.BIGINT(),
               existing_nullable=False,
               autoincrement=True)

    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.add_column(sa.Column('join_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False))
        batch_op.create_table_comment(
        'zoo Employee table',
        existing_comment=None
    )
        batch_op.alter_column('section_operation',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('age',
               existing_type=sa.Integer(),
               type_=sa.SMALLINT(),
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.BIGINT(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1),
               existing_nullable=False,
               autoincrement=True)

    with op.batch_alter_table('animals', schema=None) as batch_op:
        batch_op.add_column(sa.Column('conservation_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False))
        batch_op.create_table_comment(
        'this is table for project zoo ',
        existing_comment=None
    )
        batch_op.alter_column('type_of_food',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('kingdom_class',
               existing_type=sa.VARCHAR(),
               nullable=True,
               comment='class of animals')
        batch_op.alter_column('id',
               existing_type=sa.Integer(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1),
               type_=sa.BIGINT(),
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###
