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

    def __init__(self, screen):
        """ Object who will handle the game and the different step of it

        Args:
            screen (object pygame): the object of the screen
        """

        self.set_var_program(screen)
        self.set_var_tournament()
        self.vue = v_vue_basic(screen)

    # Method to init the var -------------------------
    def set_var_program(self, screen):
        """ Method who will set the variables that will be used for the program.

        Args:
            screen (object pygame): the object of the screen
        """

        # set the variable or object
        self.is_launch = False
        self.screen = screen
        self.step = False
        self.load = False
        self.match_load = False
        self.history_button = []
        self.sql = m_sql()

        # set the different background
        self.background =  self.vue.set_an_image('assets/bg-2.jpeg', (1280, 720))
        self.background_2 =  self.vue.set_an_image('assets/bg-3.jpeg', (1280, 720))
        self.background_3 =  self.vue.set_an_image('assets/bg-4.jpeg', (1280, 720))

        # set the button next or start
        self.next =  self.vue.set_an_image('assets/button/next.png', (400, 150))
        self.next_rect =  self.vue.set_an_image_rec(
            self.next, (1280 - 400) / 2, 500)
        self.start =  self.vue.set_an_image('assets/button/start.png', (400, 150))
        self.start_rect =  self.vue.set_an_image_rec(
            self.start, (1280 - 400) / 2, 500)
        self.search_button =  self.vue.set_an_image(
            'assets/button/search.png', (50, 50))
        self.search_button_rect =  self.vue.set_an_image_rec(
            self.search_button, 940, 125)
        self.prev =  self.vue.set_an_image('assets/button/prev.png', (400, 150))
        self.prev_rect =  self.vue.set_an_image_rec(
            self.prev, (1280 - 400) / 2, 500)

        self.next_up = True

        # set the font
        self.font = pygame.font.Font(None, 55)
        self.font_turn = pygame.font.Font(None, 90)

    def set_var_tournament(self):
        """ Method who will set the variables that will be used for the tournament """
        # var about the tournament
        self.players = []
        self.tournament = Tournament(self)
        self.index_location = 0
        self.set_time()
        self.choice = 1
        self.choice_A = ""
        self.choice_B = ""
        self.choice_C = ""
        self.set_round_time()

        # set the button more and less
        self.more = self.font_turn.render("+", 1, (255, 255, 255))
        self.more_rect = self.more.get_rect()
        self.more_rect.x = 400
        self.more_rect.y = 300
        self.less = self.font_turn.render("-", 1, (255, 255, 255))
        self.less_rect = self.less.get_rect()
        self.less_rect.x = 800
        self.less_rect.y = 300

        # set the players
        self.players = []
        self.players_search = ""
        self.tmp_players = []
        list_search_location = [[245, 190], [345, 190], [445, 190], [
            545, 190], [245, 640], [345, 640], [445, 640], [545, 640]]
        for i in list_search_location:
            self.tmp_players.append(Add_player(i[0], i[1], False, 0))

        # all method for the create
        self.switch_tournament = {
            "name": self.create_tournament_name,
            "country": self.create_tournament_place,
            "town": self.create_tournament_place,
            "location": self.create_tournament_place,
            "date": self.create_tournament_date,
            "time": self.create_tournament_time,
            "description": self.create_tournament_description,
            "player": self.create_tournament_player,
            "end": self.create_tournament_end,
            "next": self.resume_tournament
        }

    def set_var_game(self):
        """ Method who will set the variables that will be used for game """

        #  set the button object tha will be used for the management of the tournament
        self.game_statut = True
        self.validate =  self.vue.set_an_image(
            'assets/button/validate.png', (150, 50))
        self.validate_rect =  self.vue.set_an_image_rec(self.validate, 550, 650)
        self.update_score =  self.vue.set_an_image(
            'assets/button/setting.png', (50, 50))
        self.update_score_rect =  self.vue.set_an_image_rec(
            self.update_score, 750, 650)
        self.save =  self.vue.set_an_image('assets/button/save.png', (150, 50))
        self.save_rect =  self.vue.set_an_image_rec(self.save, 600, 600)
        self.round = Round(self.players, self.tournament.id)
        self.round.generate_round()
        self.player_selected = 0

        # generate all the desck object
        deck_tmp = self.generate_var_game(275, 150, 50, 200, 450, 200)
        self.deck_1 = deck_tmp[0]
        self.deck_1_rect = deck_tmp[1]
        self.player_1_rect = deck_tmp[2]
        self.player_2_rect = deck_tmp[3]
        self.area_win_1 = deck_tmp[4]
        self.area_rect_win_1 = deck_tmp[5]
        self.area_win_2 = deck_tmp[6]
        self.area_rect_win_2 = deck_tmp[7]

        deck_tmp = self.generate_var_game(275, 450, 50, 490, 450, 490)
        self.deck_2 = deck_tmp[0]
        self.deck_2_rect = deck_tmp[1]
        self.player_3_rect = deck_tmp[2]
        self.player_4_rect = deck_tmp[3]
        self.area_win_3 = deck_tmp[4]
        self.area_rect_win_3 = deck_tmp[5]
        self.area_win_4 = deck_tmp[6]
        self.area_rect_win_4 = deck_tmp[7]

        deck_tmp = self.generate_var_game(875, 150, 650, 200, 1050, 200)
        self.deck_3 = deck_tmp[0]
        self.deck_3_rect = deck_tmp[1]
        self.player_5_rect = deck_tmp[2]
        self.player_6_rect = deck_tmp[3]
        self.area_win_5 = deck_tmp[4]
        self.area_rect_win_5 = deck_tmp[5]
        self.area_win_6 = deck_tmp[6]
        self.area_rect_win_6 = deck_tmp[7]

        deck_tmp = self.generate_var_game(875, 450, 650, 490, 1050, 490)
        self.deck_4 = deck_tmp[0]
        self.deck_4_rect = deck_tmp[1]
        self.player_7_rect = deck_tmp[2]
        self.player_8_rect = deck_tmp[3]
        self.area_win_7 = deck_tmp[4]
        self.area_rect_win_7 = deck_tmp[5]
        self.area_win_8 = deck_tmp[6]
        self.area_rect_win_8 = deck_tmp[7]

    def generate_var_game(self, deck_rect_x, deck_rect_y, area_A_x, area_A_y, area_B_x, area_B_y):
        """Method to generate the desck and player pygame object

        Args:
            deck_rect_x (int): rect X of the desk
            deck_rect_y (int): rect Y of the desk
            area_A_x (int): rect X of the Player A
            area_A_y (int): rect Y of the Player A
            area_B_x (int): rect X of the Player B
            area_B_y (int): rect Y of the Player B

        Returns:
            tuple: all pygame object
        """

        deck =  self.vue.set_an_image('assets/match-no-result.png', (140, 140))
        deck_rect =  self.vue.set_an_image_rec(deck, deck_rect_x, deck_rect_y)
        area_win_A = pygame.Rect((area_A_x, area_A_y), (150, 40))
        area_rect_win_A = pygame.Surface(area_win_A.size)
        area_rect_win_A.set_alpha(0)
        area_win_B = pygame.Rect((area_B_x, area_B_y), (150, 40))
        area_rect_win_B = pygame.Surface(area_win_B.size)
        area_rect_win_B.set_alpha(0)

        return deck, deck_rect, '', '', area_win_A, area_rect_win_A, area_win_B, area_rect_win_B