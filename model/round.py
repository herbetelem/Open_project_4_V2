from datetime import datetime

from . import Player as model_player
from . import SQL_function as model_sql


# create class round
class Round:

    def __init__(self, players, id_tournament):
        """ Class to manage the round

        Args:
            players (list): list of all players by id
            id_tournament (int): the id of the tournament
        """

        self.name = ""
        self.sql = model_sql()
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
        players = self.get_players_info(players)
        for player in players:
            self.players.append(
                model_player(player[0], player[2], player[1], player[3]))
        self.settings = False