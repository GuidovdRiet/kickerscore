"""empty message

Revision ID: 4fbec16ea6e8
Revises: 315a1a496373
Create Date: 2018-08-13 20:29:23.158637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fbec16ea6e8'
down_revision = '315a1a496373'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('match', sa.Column('blue_defense_player_skill_gain_defense', sa.Float(), nullable=True))
    op.add_column('match', sa.Column('blue_defense_player_skill_gain_overall', sa.Float(), nullable=True))
    op.add_column('match', sa.Column('blue_offense_player_skill_gain_offense', sa.Float(), nullable=True))
    op.add_column('match', sa.Column('blue_offense_player_skill_gain_overall', sa.Float(), nullable=True))
    op.add_column('match', sa.Column('red_defense_player_skill_gain_defense', sa.Float(), nullable=True))
    op.add_column('match', sa.Column('red_defense_player_skill_gain_overall', sa.Float(), nullable=True))
    op.add_column('match', sa.Column('red_offense_player_skill_gain_offense', sa.Float(), nullable=True))
    op.add_column('match', sa.Column('red_offense_player_skill_gain_overall', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('match', 'red_offense_player_skill_gain_overall')
    op.drop_column('match', 'red_offense_player_skill_gain_offense')
    op.drop_column('match', 'red_defense_player_skill_gain_overall')
    op.drop_column('match', 'red_defense_player_skill_gain_defense')
    op.drop_column('match', 'blue_offense_player_skill_gain_overall')
    op.drop_column('match', 'blue_offense_player_skill_gain_offense')
    op.drop_column('match', 'blue_defense_player_skill_gain_overall')
    op.drop_column('match', 'blue_defense_player_skill_gain_defense')
    # ### end Alembic commands ###
