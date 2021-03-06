"""This code will manage the windows and the event for the application """

import math
import pygame

# import model
from models.game import Game as m_game
from models.round import Round as m_round
from models.sql_function import SqlFunction as m_sql
from models.tournament import Tournament as m_tournament

# import view
from views.view import VueBasic as v_vue_basic

# import controller
from controllers.event_mouse import EventMouse as c_event_mouse
from controllers.event_key import EventKey as c_event_key
from controllers.game import Game as c_game
from controllers.round import Round as c_round
from controllers.tournament import Tournament as c_tournament


class ControllerRunGame:
    """Object controller for the all program
    """

    def __init__(self):
        pygame.init()

        # windows
        pygame.display.set_caption('Checkmate Tournament')
        self.screen = pygame.display.set_mode((1280, 720))
        # set object
        self.v_basic = v_vue_basic(self.screen)

        self.m_tournament = m_tournament()
        self.c_tournament = c_tournament(self)
        self.m_game = m_game(self)
        self.c_game = c_game(self)
        self.m_sql = m_sql()

        #  INIT POUR SPLIT LES DEPENDENCE
        self.c_tournament.set_time()
        self.c_tournament.set_round_time()

        # load bg
        self.background = self.v_basic.set_an_image(
            'assets/bg.jpg', (1280, 720))
        # create button and rect for first menu
        self.play_button = self.v_basic.set_an_image(
            'assets/button/new_game.png', (400, 100))
        self.play_button_rect = self.v_basic.set_an_image_rec(self.play_button, math.ceil(
            self.screen .get_width() / 4) - 50, math.ceil(self.screen .get_height() / 2))

        self.load_button = self.v_basic.set_an_image(
            'assets/button/load_game.png', (400, 100))
        self.load_button_rect = self.v_basic.set_an_image_rec(self.load_button, math.ceil(
            self.screen .get_width() / 4) * 2 + 50, math.ceil(self.screen .get_height() / 2))
        # * HH Charge la Favicon
        self.icon_32x32 = pygame.image.load(
            "assets/favicon.png").convert_alpha()
        # * HH Applique la Favicon
        pygame.display.set_icon(self.icon_32x32)
        # manage the game
        self.running = True
        # step for create a tournament
        self.step = {
            "name": "country",
            "country": "town",
            "town": "location",
            "location": "date",
            "date": "time",
            "time": "description",
            "description": "player",
            "player": "end"
        }

    def run(self):
        """method to run the game
        """

        self.c_key = c_event_key(self)
        self.c_mouse = c_event_mouse(self)

        while self.running:
            if self.m_game.is_launch or self.m_game.load:
                self.c_game.update()
            else:
                # app the image of first menu
                self.v_basic.manage_view(self.background, (0, 0))
                self.v_basic.manage_view(
                    self.play_button, self.play_button_rect)
                self.v_basic.manage_view(
                    self.load_button, self.load_button_rect)

            # update the screen
            pygame.display.flip()

            for event in pygame.event.get():
                # if leaving
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    self.m_sql.connector.close()
                    print("le jeu ce ferme")
                # if mouseclick
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # manage the first menu
                    if self.m_game.step is False:
                        self.c_mouse.manage_first_menu(event)

                    # Manage the load buttons
                    if self.m_game.load:
                        self.c_mouse.manage_load_button(event)
                    # manage the next step of creation of a tournament
                    elif self.m_game.next_up and self.m_game.next_rect.collidepoint(event.pos):
                        self.manage_step()
                    elif self.m_game.next_up is False and \
                            self.m_game.start_rect.collidepoint(event.pos):
                        self.c_mouse.manage_end_creation()

                    if self.m_game.next_up:
                        # manage the selection of the date
                        if self.m_game.step == "date":
                            self.c_mouse.manage_date(event)
                        # manage the selection of time
                        if self.m_game.step == "time":
                            self.c_mouse.manage_time(event)
                        # manage the selection of players
                        if self.m_game.step == "player":
                            self.c_mouse.manage_player(event)

                    # if the tournament have been created
                    if self.m_game.next_up is False:
                        if self.m_game.game_statut:

                            # if the settings have been selected
                            if self.m_round.settings:
                                self.c_mouse.manage_button_edit(event)
                                self.c_mouse.validate_round_check(event)
                            else:
                                #  Manage Game desk 1
                                self.c_mouse.manage_deck(event)
                                # Manage Validate
                                if self.m_game.validate_rect.collidepoint(event.pos):
                                    self.c_mouse.validate_round(event)
                                elif self.m_game.update_score_rect.collidepoint(event.pos):
                                    self.m_round.settings = True
                        # Mannage save
                        if self.m_round.nb_turn == 7 and \
                                self.m_game.save_rect.collidepoint(event.pos):
                            self.c_mouse.update_score()
                # if use keyboard
                elif event.type == pygame.KEYDOWN:

                    if self.m_game.next_up:
                        # manage the creation of the name
                        if self.m_game.step == "name" or self.m_game.step == "description" or \
                                self.m_game.step == "player":
                            self.c_key.keybord_abc()
                            if event.key == pygame.K_SPACE:
                                self.c_key.keyboard_space()
                            elif event.key == pygame.K_BACKSPACE:
                                self.c_key.keyboard_backspace()
                        if self.m_game.step == "country":
                            self.c_key.keyboard_coutry(event, self.m_sql)
                        if self.m_game.step == "town":
                            self.c_key.keyboard_town(event, self.m_sql)
                        if self.m_game.step == "location":
                            self.c_key.keyboard_location(event, self.m_sql)
                    # manage the keybord used for update the score
                    else:
                        if self.m_game.next_up is False:
                            if self.m_game.game_statut:
                                if self.m_round.settings:
                                    self.c_key.keyboard_num(event)
                                    if event.key == pygame.K_BACKSPACE:
                                        self.c_key.keyboard_backspace()

    def manage_step(self):
        """method to manage the step of creation for the tournament
        """
        if self.m_game.step == "country":
            tmp_country = self.m_sql.get_country()
            tmp_country = tmp_country[self.m_game.index_location]
            self.m_tournament.country = tmp_country
        if self.m_game.step == "town":
            tmp_town = self.m_sql.get_town(self.m_tournament.country)
            tmp_town = tmp_town[self.m_game.index_location]
            self.m_tournament.town = tmp_town
        if self.m_game.step == "location":
            tmp_location = self.m_sql.get_location(self.m_tournament.town)
            tmp_location = tmp_location[self.m_game.index_location]
            self.m_tournament.location = tmp_location
        if self.m_game.step == "date":
            self.m_tournament.date = f"{self.m_tournament.day.str}/" + \
                f"{self.m_tournament.month.str}/" + \
                f"{self.m_tournament.year.str}"
        if self.m_game.step == "time":
            if self.m_game.choice == 1:
                self.m_tournament.time = "bullet"
            elif self.m_game.choice == 2:
                self.m_tournament.time = "blitz"
            elif self.m_game.choice == 3:
                self.m_tournament.time = "coup rapide"
        if self.m_game.step == "player" and len(self.m_game.players) == 8:
            self.m_tournament.players = self.m_game.players
            self.m_game.step = self.step[self.m_game.step]
            self.m_game.index_location = 0
        elif self.m_game.step != "player":
            self.m_game.step = self.step[self.m_game.step]
            self.m_game.index_location = 0

    def set_round(self):
        """method to generate the first round one the tournament have been set
        """
        self.m_round = m_round(self.m_tournament.id)
        self.c_round = c_round(self, self.m_game.players)
        self.c_round.generate_round()
