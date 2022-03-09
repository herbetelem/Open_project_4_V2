from datetime import datetime

from models.players import Player as m_player
from models.sql_function import SqlFunction as m_sql
from controllers.round import Round as c_round


# create class round
class Round:

    def __init__(self, id_tournament):
        """ Class to manage the round

        Args:
            players (list): list of all players by id
            id_tournament (int): the id of the tournament
        """
        self.name = ""
        self.sql = m_sql()
        self.players = []
        self.date_start = [0, 0, 0, 0, 0, 0, 0]
        self.date_end = [0, 0, 0, 0, 0, 0, 0]
        self.hour_start = [0, 0, 0, 0, 0, 0, 0]
        self.hour_end = [0, 0, 0, 0, 0, 0, 0]
        self.id_tournament = id_tournament
        self.match = [[1, 2, False], [3, 4, False],
                      [5, 6, False], [7, 8, False]]
        self.match_done = []
        self.nb_turn = 0
        self.settings = False
