"""empty message

Revision ID: 65ec6912bc6a
Revises: d533d084fa74
Create Date: 2020-05-12 20:06:12.706451

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '65ec6912bc6a'
down_revision = 'd533d084fa74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_games_cricket_player1', table_name='games_cricket')
    op.drop_index('ix_games_cricket_player2', table_name='games_cricket')
    op.drop_index('ix_games_cricket_status', table_name='games_cricket')
    op.drop_table('games_cricket')
    op.drop_index('ix_games_player1', table_name='games')
    op.drop_index('ix_games_player2', table_name='games')
    op.drop_index('ix_games_status', table_name='games')
    op.drop_table('games')
    op.add_column('games_all', sa.Column('jitsi_public_server', sa.Boolean(), nullable=True))
    op.add_column('webcam_settings', sa.Column('jitsi_public_server', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('webcam_settings', 'jitsi_public_server')
    op.drop_column('games_all', 'jitsi_public_server')
    op.create_table('games',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('hashid', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('player1', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('player2', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('bo_sets', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('bo_legs', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('p1_sets', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('p2_sets', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('p1_legs', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('p2_legs', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('p1_score', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('p2_score', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('p1_next_turn', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('type', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('match_json', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('in_mode', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('out_mode', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('begin', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('end', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('closest_to_bull', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('closest_to_bull_json', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('opponent_type', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('two_clear_legs', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('public_challenge', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('tournament', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('score_input_delay', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('jitsi_hashid', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('webcam', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('variant', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('tournament_round_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tournament_stage_game_bracket_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tournament_stage_game_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['player1'], ['users.id'], name='games_player1_fkey'),
    sa.ForeignKeyConstraint(['player2'], ['users.id'], name='games_player2_fkey'),
    sa.ForeignKeyConstraint(['tournament'], ['tournaments.hashid'], name='fk_games_tournament_tournaments'),
    sa.ForeignKeyConstraint(['tournament_round_id'], ['tournament_stage_rounds.id'], name='fk_games_tournament_round_id_tournament_stage_rounds'),
    sa.PrimaryKeyConstraint('id', name='games_pkey'),
    sa.UniqueConstraint('hashid', name='uq_games_hashid'),
    sa.UniqueConstraint('jitsi_hashid', name='uq_games_jitsi_hashid')
    )
    op.create_index('ix_games_status', 'games', ['status'], unique=False)
    op.create_index('ix_games_player2', 'games', ['player2'], unique=False)
    op.create_index('ix_games_player1', 'games', ['player1'], unique=False)
    op.create_table('games_cricket',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('hashid', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('bo_sets', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('bo_legs', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('two_clear_legs', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('p1_sets', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('p2_sets', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('p1_legs', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('p2_legs', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('p1_next_turn', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('closest_to_bull', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('closest_to_bull_json', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('match_json', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('begin', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('end', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('opponent_type', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('public_challenge', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('score_input_delay', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('webcam', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('jitsi_hashid', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('tournament', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('player1', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('player2', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('variant', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('p1_score', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('p2_score', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('confirmation_needed', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('undo_possible', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('tournament_round_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tournament_stage_game_bracket_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tournament_stage_game_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['player1'], ['users.id'], name='fk_games_cricket_player1_users'),
    sa.ForeignKeyConstraint(['player2'], ['users.id'], name='fk_games_cricket_player2_users'),
    sa.ForeignKeyConstraint(['tournament'], ['tournaments.hashid'], name='fk_games_cricket_tournament_tournaments'),
    sa.ForeignKeyConstraint(['tournament_round_id'], ['tournament_stage_rounds.id'], name='fk_games_cricket_tournament_round_id_tournament_stage_rounds'),
    sa.PrimaryKeyConstraint('id', name='pk_games_cricket'),
    sa.UniqueConstraint('hashid', name='uq_games_cricket_hashid'),
    sa.UniqueConstraint('jitsi_hashid', name='uq_games_cricket_jitsi_hashid')
    )
    op.create_index('ix_games_cricket_status', 'games_cricket', ['status'], unique=False)
    op.create_index('ix_games_cricket_player2', 'games_cricket', ['player2'], unique=False)
    op.create_index('ix_games_cricket_player1', 'games_cricket', ['player1'], unique=False)
    # ### end Alembic commands ###