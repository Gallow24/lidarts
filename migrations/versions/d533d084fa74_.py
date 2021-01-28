"""empty message

Revision ID: d533d084fa74
Revises: 532096580f7b
Create Date: 2020-05-11 17:00:29.194479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd533d084fa74'
down_revision = '532096580f7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games_all',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('variant', sa.String(length=50), nullable=True),
    sa.Column('hashid', sa.String(length=10), nullable=True),
    sa.Column('bo_sets', sa.Integer(), nullable=False),
    sa.Column('bo_legs', sa.Integer(), nullable=False),
    sa.Column('two_clear_legs', sa.Boolean(), nullable=True),
    sa.Column('p1_sets', sa.Integer(), nullable=True),
    sa.Column('p2_sets', sa.Integer(), nullable=True),
    sa.Column('p1_legs', sa.Integer(), nullable=True),
    sa.Column('p2_legs', sa.Integer(), nullable=True),
    sa.Column('p1_score', sa.Integer(), nullable=True),
    sa.Column('p2_score', sa.Integer(), nullable=True),
    sa.Column('p1_next_turn', sa.Boolean(), nullable=True),
    sa.Column('closest_to_bull', sa.Boolean(), nullable=True),
    sa.Column('closest_to_bull_json', sa.JSON(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('match_json', sa.JSON(), nullable=True),
    sa.Column('begin', sa.DateTime(), nullable=True),
    sa.Column('end', sa.DateTime(), nullable=True),
    sa.Column('opponent_type', sa.String(length=10), nullable=True),
    sa.Column('public_challenge', sa.Boolean(), nullable=True),
    sa.Column('score_input_delay', sa.Integer(), nullable=True),
    sa.Column('webcam', sa.Boolean(), nullable=True),
    sa.Column('jitsi_hashid', sa.String(length=10), nullable=True),
    sa.Column('tournament_stage_game_id', sa.Integer(), nullable=True),
    sa.Column('tournament_stage_game_bracket_id', sa.Integer(), nullable=True),
    sa.Column('tournament', sa.String(length=10), nullable=True),
    sa.Column('tournament_round_id', sa.Integer(), nullable=True),
    sa.Column('player1', sa.Integer(), nullable=True),
    sa.Column('player2', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player1'], ['users.id'], name=op.f('fk_games_all_player1_users')),
    sa.ForeignKeyConstraint(['player2'], ['users.id'], name=op.f('fk_games_all_player2_users')),
    sa.ForeignKeyConstraint(['tournament'], ['tournaments.hashid'], name=op.f('fk_games_all_tournament_tournaments')),
    sa.ForeignKeyConstraint(['tournament_round_id'], ['tournament_stage_rounds.id'], name=op.f('fk_games_all_tournament_round_id_tournament_stage_rounds')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_games_all')),
    sa.UniqueConstraint('hashid', name=op.f('uq_games_all_hashid')),
    sa.UniqueConstraint('jitsi_hashid', name=op.f('uq_games_all_jitsi_hashid'))
    )
    op.create_index(op.f('ix_games_all_player1'), 'games_all', ['player1'], unique=False)
    op.create_index(op.f('ix_games_all_player2'), 'games_all', ['player2'], unique=False)
    op.create_index(op.f('ix_games_all_status'), 'games_all', ['status'], unique=False)
    op.create_table('games_cricket_new',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('confirmation_needed', sa.Boolean(), nullable=True),
    sa.Column('undo_possible', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['games_all.id'], name=op.f('fk_games_cricket_new_id_games_all')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_games_cricket_new'))
    )
    op.create_table('games_x01',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('in_mode', sa.String(length=15), nullable=True),
    sa.Column('out_mode', sa.String(length=15), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['games_all.id'], name=op.f('fk_games_x01_id_games_all')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_games_x01'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('games_x01')
    op.drop_table('games_cricket_new')
    op.drop_index(op.f('ix_games_all_status'), table_name='games_all')
    op.drop_index(op.f('ix_games_all_player2'), table_name='games_all')
    op.drop_index(op.f('ix_games_all_player1'), table_name='games_all')
    op.drop_table('games_all')
    # ### end Alembic commands ###