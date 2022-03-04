# import python
import pygame
from turtle import pd

# import model
from model.game import Game as m_game
from model.players import Player as m_player
from model.round import Round as m_round
from model.sql_function import SqlFunction as m_sql
from model.tournament import Tournament as m_tournament

# import view
from vue.vue import VueBasic as v_vue_basic

# import controller
from controller.event_mouse import EventMouse as c_event_mouse
from controller.event_key import EventKey as c_event_key
from controller.round import Round as c_round
from controller.tournament import Tournament as c_tournament


# create class game

class Game:
    """Object Who will manage the game
    """

    def __init__(self, game):
        """ Object who will handle the game and the different step of it

        Args:
            screen (object pygame): the object of the screen
        """
        self.data = game
        self.vue_basic = v_vue_basic(self.data.screen)

    #  Method to manage all
    def update(self):

        # load the histry of tournament
        if self.data.load:
            self.vue_basic.manage_view(self.data.background_3, (0, 0))
            self.show_prev_matchs()
        # load the tournament
        elif self.data.tournament.created:
            # app the background
            self.vue_basic.manage_view(self.data.background_2, (0, 0))
            if self.data.round.settings:
                self.show_settings()
            elif self.data.game_statut:
                self.show_match()
            else:
                self.show_result()
        # load the creation of the tournament
        else:
            # app the background
            self.vue_basic.manage_view(self.data.background, (0, 0))
            # if we want to create a tournament
            self.data.tournament.create_tournament()

    # Method about the tournament
    def show_match(self):
        """ Method who will show the match of the actual round """

        self.vue_basic.print_sentence(
            f"Round match list n°{self.data.round.nb_turn + 1}", self.data.font, (400, 50))

        # match 1
        self.vue_basic.print_sentence(
            f"{self.data.round.match[0][0].last_name[0]}.{self.data.round.match[0][0].name[:5]}", self.data.font, (50, 190))
        self.vue_basic.print_sentence(
            f"{self.data.round.match[0][1].last_name[0]}.{self.data.round.match[0][1].name[:5]}", self.data.font, (450, 190))
        self.vue_basic.manage_view(self.data.deck_1, self.data.deck_1_rect)
        self.vue_basic.manage_view(self.data.area_rect_win_1, self.data.area_win_1)
        self.vue_basic.manage_view(self.data.area_rect_win_2, self.data.area_win_2)

        # match 2
        self.vue_basic.print_sentence(
            f"{self.data.round.match[1][0].last_name[0]}.{self.data.round.match[1][0].name[:5]}", self.data.font, (50, 490))
        self.vue_basic.print_sentence(
            f"{self.data.round.match[1][1].last_name[0]}.{self.data.round.match[1][1].name[:5]}", self.data.font, (450, 490))
        self.vue_basic.manage_view(self.data.deck_2, self.data.deck_2_rect)
        self.vue_basic.manage_view(self.data.area_rect_win_3, self.data.area_win_3)
        self.vue_basic.manage_view(self.data.area_rect_win_4, self.data.area_win_4)

        # match 3
        self.vue_basic.print_sentence(
            f"{self.data.round.match[2][0].last_name[0]}.{self.data.round.match[2][0].name[:5]}", self.data.font, (650, 190))
        self.vue_basic.print_sentence(
            f"{self.data.round.match[2][1].last_name[0]}.{self.data.round.match[2][1].name[:5]}", self.data.font, (1050, 190))
        self.vue_basic.manage_view(self.data.deck_3, self.data.deck_3_rect)
        self.vue_basic.manage_view(self.data.area_rect_win_5, self.data.area_win_5)
        self.vue_basic.manage_view(self.data.area_rect_win_6, self.data.area_win_6)

        # match 4
        self.vue_basic.print_sentence(
            f"{self.data.round.match[3][0].last_name[0]}.{self.data.round.match[3][0].name[:5]}", self.data.font, (650, 490))
        self.vue_basic.print_sentence(
            f"{self.data.round.match[3][1].last_name[0]}.{self.data.round.match[3][1].name[:5]}", self.data.font, (1050, 490))
        self.vue_basic.manage_view(self.data.deck_4, self.data.deck_4_rect)
        self.vue_basic.manage_view(self.data.area_rect_win_7, self.data.area_win_7)
        self.vue_basic.manage_view(self.data.area_rect_win_8, self.data.area_win_8)

        # button validate and settings
        self.vue_basic.manage_view(self.data.update_score, self.data.update_score_rect)
        tmp_check = True
        for match in self.data.round.match:
            if match[2] < 1:
                tmp_check = False

        if tmp_check:
            self.vue_basic.manage_view(self.data.validate, self.data.validate_rect)

    def show_result(self):
        """ Method to show the result of the tournament
        """
        self.data.round.sort_by_rank()
        x = 40
        y = 40
        for index in range(1, 9):
            self.vue_basic.print_sentence(
                f"Place {index}: {self.data.round.players[index-1].name} {self.data.round.players[index-1].last_name}, score = {self.data.round.players[index-1].score}", self.data.font, (x, y))
            y += 70
        self.vue_basic.manage_view(self.save, self.save_rect)

    def show_settings(self):
        """ Method for show the score during a tournament and edit it """

        self.data.round.sort_by_rank()
        x = 40
        y = 40
        for index in range(1, 9):
            self.vue_basic.print_sentence(
                f"Place {index}: {self.data.round.players[index-1].name} {self.data.round.players[index-1].last_name}, score = {self.data.round.players[index-1].score}", self.data.font, (x, y))
            y += 70
        self.vue_basic.manage_view(self.data.validate, self.data.validate_rect)
        x = 900
        y = 40
        for player in self.data.round.players:
            player.rect = self.set_an_image_rec(player.img, x, y)
            self.vue_basic.manage_view(player.img, player.rect)
            y += 70

    # Method about the load of prev game
    def show_prev_matchs(self):
        if self.data.match_load:
            load = self.sql.get_players_score(self.data.match_load)
            x = 50
            y = 50
            for data in load:
                self.vue_basic.print_sentence(
                    f"{data[0]} {data[1]} score: {data[2]}", self.data.font, (x, y))
                y += 50
            self.vue_basic.manage_view(self.data.prev, self.data.prev_rect)

        else:
            self.data.history = self.sql.get_prev_tournament()
            x = 50
            y = 50
            self.data.history_button = []
            for tournament in self.data.history:
                self.data.history_button.append(
                    Load_a_tournament(y, x+1000, tournament[0][0]))
                self.vue_basic.print_sentence(tournament[0][1], self.data.font, (x, y))
                y += 50
                self.vue_basic.print_sentence(tournament[0][2], self.data.font, (x, y))
                y += 50
            for index in self.data.history_button:
                self.vue_basic.manage_view(index.img, index.rect)

