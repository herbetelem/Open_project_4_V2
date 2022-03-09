from datetime import datetime

from models.players import Player as m_player



class Round:

    def __init__(self, c_main, players):
        self.c_main = c_main
        players = self.get_players_info(players)
        for player in players:
            self.c_main.m_round.players.append(
                m_player(player[0], player[2], player[1], player[3]))

    def get_players_info(self, players):
        """ method to get the players information about their global_rankd

        Args:
            players (list): list of players

        Returns:
            [type]: list of players with their rank
        """
        if self.c_main.m_round.nb_turn == 0:
            players = self.c_main.m_sql.get_players_rank(players)
            return players
        else:
            return

    def generate_round(self):
        """ Methode to generate the round """

        self.c_main.m_round.name = f"Round: {self.c_main.m_round.nb_turn+1}"
        index_match = 0
        self.c_main.m_round.date_start[self.c_main.m_round.nb_turn] = datetime.now(
        ).strftime('%Y-%m-%d')
        self.c_main.m_round.hour_start[self.c_main.m_round.nb_turn] = datetime.now(
        ).strftime('%H-%M')
        self.c_main.m_round.match = [[1, 2, False], [3, 4, False],
                                     [5, 6, False], [7, 8, False]]
        self.sort_by_rank()
        # set up all false cause for the new round no one have an adv for now
        list_adv = [False, False, False, False, False, False, False, False]
        list_order = [4, 5, 6, 7, 3, 2, 1, 0]
        for player in self.c_main.m_round.players:
            is_player_choosed = False
            for match in self.c_main.m_round.match:
                if player in match:
                    is_player_choosed = True

            if not is_player_choosed and index_match < 4:
                found = False
                for order in list_order:
                    if self.c_main.m_round.players[order] not in player.matched and not list_adv[order] and not found:
                        self.c_main.m_round.match[index_match][0] = player
                        self.c_main.m_round.match[index_match][1] = self.c_main.m_round.players[order]
                        list_adv[order] = True
                        is_player_choosed = True
                        found = True
                index_match += 1

    def validate_round(self, results):
        """ Method to save the match

        Args:
            results (list): list of result of the match
        """

        score = {
            3: [1, 1],
            1: [2, 0],
            2: [0, 2],
        }
        self.c_main.m_round.date_end[self.c_main.m_round.nb_turn] = datetime.now(
        ).strftime('%Y-%m-%d')
        self.c_main.m_round.hour_end[self.c_main.m_round.nb_turn] = datetime.now(
        ).strftime('%H-%M')
        for match in self.c_main.m_round.match:
            self.c_main.m_sql.save_round((self.c_main.m_tournament.id, match[0].id, match[1].id, match[2], self.c_main.m_round.name, self.c_main.m_round.date_start[self.c_main.m_round.nb_turn],
                                self.c_main.m_round.date_end[self.c_main.m_round.nb_turn], self.c_main.m_round.hour_start[self.c_main.m_round.nb_turn], self.c_main.m_round.hour_end[self.c_main.m_round.nb_turn]))
        for index in range(4):
            # attribution of score
            self.c_main.m_round.match[index][0].score += score[results[index]][0]
            self.c_main.m_round.match[index][1].score += score[results[index]][1]

            # add in the history of player their match
            self.c_main.m_round.match[index][0].matched.append(
                self.c_main.m_round.match[index][1])
            self.c_main.m_round.match[index][1].matched.append(
                self.c_main.m_round.match[index][0])
        self.c_main.m_round.match = [[1, 2, False], [3, 4, False],
                                     [5, 6, False], [7, 8, False]]
        self.c_main.m_round.nb_turn += 1
        for player in self.c_main.m_round.players:
            player.choosed = False

    def sort_by_rank(self):
        """ Method to sort the players first by their score, then by their global rank """
        self.c_main.m_round.players.sort(key=lambda x: (
            x.score, -x.global_rank), reverse=True)
        for i in range(8):
            self.c_main.m_round.players[i].pool_rank = i
