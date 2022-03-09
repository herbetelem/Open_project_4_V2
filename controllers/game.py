# import python
import pygame
from turtle import pd

# import model
from models.game import Game as m_game
from models.players import Player as m_player
from models.round import Round as m_round
from models.sql_function import SqlFunction as m_sql
from models.tournament import Tournament as m_tournament
from models.load_a_tournament import LoadATournament as m_load_tourn

# import view
from vues.vue import VueBasic as v_vue_basic

# import controller
from controllers.event_mouse import EventMouse as c_event_mouse
from controllers.event_key import EventKey as c_event_key
from controllers.round import Round as c_round
from controllers.tournament import Tournament as c_tournament


# create class game

class Game:
    """Object Who will manage the game
    """

    def __init__(self, c_main):
        self.c_main = c_main

    #  Method to manage all
    def update(self):

        # load the histry of tournament
        if self.c_main.m_game.load:
            self.c_main.v_basic.manage_view(self.c_main.m_game.background_3, (0, 0))
            self.show_prev_matchs()
        # load the tournament
        elif self.c_main.m_tournament.created:
            # app the background
            self.c_main.v_basic.manage_view(self.c_main.m_game.background_2, (0, 0))
            if self.c_main.m_round.settings:
                self.show_settings()
            elif self.c_main.m_game.game_statut:
                self.show_match()
            else:
                self.show_result()
        # load the creation of the tournament
        else:
            # app the background
            self.c_main.v_basic.manage_view(self.c_main.m_game.background, (0, 0))
            # if we want to create a tournament
            self.c_main.c_tournament.create_tournament()

    # Method about the tournament
    def show_match(self):
        """ Method who will show the match of the actual round """

        self.c_main.v_basic.print_sentence(
            f"Round match list n°{self.c_main.m_round.nb_turn + 1}", self.c_main.m_game.font, (400, 50))

        # match 1
        self.c_main.v_basic.print_sentence(
            f"{self.c_main.m_round.match[0][0].last_name[0]}.{self.c_main.m_round.match[0][0].name[:5]}", self.c_main.m_game.font, (50, 190))
        self.c_main.v_basic.print_sentence(
            f"{self.c_main.m_round.match[0][1].last_name[0]}.{self.c_main.m_round.match[0][1].name[:5]}", self.c_main.m_game.font, (450, 190))
        self.c_main.v_basic.manage_view(self.c_main.m_game.deck_1, self.c_main.m_game.deck_1_rect)
        self.c_main.v_basic.manage_view(self.c_main.m_game.area_rect_win_1, self.c_main.m_game.area_win_1)
        self.c_main.v_basic.manage_view(self.c_main.m_game.area_rect_win_2, self.c_main.m_game.area_win_2)

        # match 2
        self.c_main.v_basic.print_sentence(
            f"{self.c_main.m_round.match[1][0].last_name[0]}.{self.c_main.m_round.match[1][0].name[:5]}", self.c_main.m_game.font, (50, 490))
        self.c_main.v_basic.print_sentence(
            f"{self.c_main.m_round.match[1][1].last_name[0]}.{self.c_main.m_round.match[1][1].name[:5]}", self.c_main.m_game.font, (450, 490))
        self.c_main.v_basic.manage_view(self.c_main.m_game.deck_2, self.c_main.m_game.deck_2_rect)
        self.c_main.v_basic.manage_view(self.c_main.m_game.area_rect_win_3, self.c_main.m_game.area_win_3)
        self.c_main.v_basic.manage_view(self.c_main.m_game.area_rect_win_4, self.c_main.m_game.area_win_4)

        # match 3
        self.c_main.v_basic.print_sentence(
            f"{self.c_main.m_round.match[2][0].last_name[0]}.{self.c_main.m_round.match[2][0].name[:5]}", self.c_main.m_game.font, (650, 190))
        self.c_main.v_basic.print_sentence(
            f"{self.c_main.m_round.match[2][1].last_name[0]}.{self.c_main.m_round.match[2][1].name[:5]}", self.c_main.m_game.font, (1050, 190))
        self.c_main.v_basic.manage_view(self.c_main.m_game.deck_3, self.c_main.m_game.deck_3_rect)
        self.c_main.v_basic.manage_view(self.c_main.m_game.area_rect_win_5, self.c_main.m_game.area_win_5)
        self.c_main.v_basic.manage_view(self.c_main.m_game.area_rect_win_6, self.c_main.m_game.area_win_6)

        # match 4
        self.c_main.v_basic.print_sentence(
            f"{self.c_main.m_round.match[3][0].last_name[0]}.{self.c_main.m_round.match[3][0].name[:5]}", self.c_main.m_game.font, (650, 490))
        self.c_main.v_basic.print_sentence(
            f"{self.c_main.m_round.match[3][1].last_name[0]}.{self.c_main.m_round.match[3][1].name[:5]}", self.c_main.m_game.font, (1050, 490))
        self.c_main.v_basic.manage_view(self.c_main.m_game.deck_4, self.c_main.m_game.deck_4_rect)
        self.c_main.v_basic.manage_view(self.c_main.m_game.area_rect_win_7, self.c_main.m_game.area_win_7)
        self.c_main.v_basic.manage_view(self.c_main.m_game.area_rect_win_8, self.c_main.m_game.area_win_8)

        # button validate and settings
        self.c_main.v_basic.manage_view(self.c_main.m_game.update_score, self.c_main.m_game.update_score_rect)
        tmp_check = True
        for match in self.c_main.m_round.match:
            if match[2] < 1:
                tmp_check = False

        if tmp_check:
            self.c_main.v_basic.manage_view(self.c_main.m_game.validate, self.c_main.m_game.validate_rect)

    def show_result(self):
        """ Method to show the result of the tournament
        """
        self.c_main.c_round.sort_by_rank()
        x = 40
        y = 40
        for index in range(1, 9):
            self.c_main.v_basic.print_sentence(
                f"Place {index}: {self.c_main.m_round.players[index-1].name} {self.c_main.m_round.players[index-1].last_name}, score = {self.c_main.m_round.players[index-1].score}", self.c_main.m_game.font, (x, y))
            y += 70
        self.c_main.v_basic.manage_view(self.save, self.save_rect)

    def show_settings(self):
        """ Method for show the score during a tournament and edit it """

        self.c_main.c_round.sort_by_rank()
        x = 40
        y = 40
        for index in range(1, 9):
            self.c_main.v_basic.print_sentence(
                f"Place {index}: {self.c_main.m_round.players[index-1].name} {self.c_main.m_round.players[index-1].last_name}, score = {self.c_main.m_round.players[index-1].score}", self.c_main.m_game.font, (x, y))
            y += 70
        self.c_main.v_basic.manage_view(self.c_main.m_game.validate, self.c_main.m_game.validate_rect)
        x = 900
        y = 40
        for player in self.c_main.m_round.players:
            player.rect = self.c_main.v_basic.set_an_image_rec(player.img, x, y)
            self.c_main.v_basic.manage_view(player.img, player.rect)
            y += 70

    # Method about the load of prev game
    def show_prev_matchs(self):
        if self.c_main.m_game.match_load:
            load = self.c_main.m_sql.get_players_score(self.c_main.m_game.match_load)
            x = 50
            y = 50
            for data in load:
                self.c_main.v_basic.print_sentence(
                    f"{data[0]} {data[1]} score: {data[2]}", self.c_main.m_game.font, (x, y))
                y += 50
            self.c_main.v_basic.manage_view(self.c_main.m_game.prev, self.c_main.m_game.prev_rect)

        else:
            self.c_main.m_game.history = self.c_main.m_sql.get_prev_tournament()
            x = 50
            y = 50
            self.c_main.m_game.history_button = []
            for tournament in self.c_main.m_game.history:
                self.c_main.m_game.history_button.append(
                    m_load_tourn(y, x+1000, tournament[0][0]))
                self.c_main.v_basic.print_sentence(tournament[0][1], self.c_main.m_game.font, (x, y))
                y += 50
                self.c_main.v_basic.print_sentence(tournament[0][2], self.c_main.m_game.font, (x, y))
                y += 50
            for index in self.c_main.m_game.history_button:
                self.c_main.v_basic.manage_view(index.img, index.rect)

