"""module Event key"""
import pygame


class EventKey:
    """Object to manage the key interaction of the game
    """

    def __init__(self, c_main):
        self.c_main = c_main

    def keybord_abc(self):
        """method to manage the alphabet touch of the keyboard
        """
        letters = {x: pygame.key.key_code(
            x) for x in "abcdefghijklmnopqrstuvwxyz"}
        touche = pygame.key.get_pressed()
        for (letter, value) in letters.items():
            if touche[value]:
                if self.c_main.m_game.step == "name":
                    if len(self.c_main.m_tournament.description) < 50:
                        self.c_main.m_tournament.name = self.c_main.m_tournament.name + \
                            str(letter)
                elif self.c_main.m_game.step == "description":
                    if len(self.c_main.m_tournament.description) < 200:
                        self.c_main.m_tournament.description = \
                            self.c_main.m_tournament.description + str(letter)
                elif self.c_main.m_game.step == "player":
                    self.c_main.m_game.players_search = self.c_main.m_game.players_search + \
                        str(letter)

    def keyboard_space(self):
        """method to manage the space touch of the keyboard
        """
        if self.c_main.m_game.step == "name":
            self.c_main.m_tournament.name = self.c_main.m_tournament.name + " "
        elif self.c_main.m_game.step == "description":
            self.c_main.m_tournament.description = self.c_main.m_tournament.description + " "
        elif self.c_main.m_game.step == "player":
            self.c_main.m_game.players_search = self.c_main.m_game.players_search + " "

    def keyboard_backspace(self):
        """method to manage the backspace touch of the keyboard
        """
        if self.c_main.m_game.step == "name":
            self.c_main.m_tournament.name = self.c_main.m_tournament.name[:-1]
        elif self.c_main.m_game.step == "description":
            self.c_main.m_tournament.description = self.c_main.m_tournament.description[:-1]
        elif self.c_main.m_game.step == "player":
            self.c_main.m_game.players_search = self.c_main.m_game.players_search[:-1]

    def keyboard_coutry(self, event, sql):
        """ method to manage the step where we select the country

        Args:
            event (pygame_object): the object where all the interaction are stocked
            sql (object): the object with the sql interaction
        """
        if event.key == pygame.K_LEFT:
            self.c_main.m_game.index_location -= 1
            if self.c_main.m_game.index_location < 0:
                self.c_main.m_game.index_location = len(sql.get_country()) - 1
        elif event.key == pygame.K_RIGHT:
            self.c_main.m_game.index_location += 1
            if self.c_main.m_game.index_location >= len(sql.get_country()):
                self.c_main.m_game.index_location = 0

    def keyboard_town(self, event, sql):
        """ method to manage the step where we select the town

        Args:
            event (pygame_object): the object where all the interaction are stocked
            sql (object): the object with the sql interaction
        """
        if event.key == pygame.K_LEFT:
            self.c_main.m_game.index_location -= 1
            if self.c_main.m_game.index_location < 0:
                self.c_main.m_game.index_location = len(
                    self.c_main.m_game.m_sql.get_town(self.c_main.m_tournament.country)) - 1
        elif event.key == pygame.K_RIGHT:
            self.c_main.m_game.index_location += 1
            if self.c_main.m_game.index_location >= \
                    len(sql.get_town(self.c_main.m_tournament.country)):
                self.c_main.m_game.index_location = 0

    def keyboard_location(self, event, sql):
        """ method to manage the step where we select the location

        Args:
            event (pygame_object): the object where all the interaction are stocked
            sql (object): the object with the sql interaction
        """
        if event.key == pygame.K_LEFT:
            self.c_main.m_game.index_location -= 1
            if self.c_main.m_game.index_location < 0:
                self.c_main.m_game.index_location = len(
                    sql.get_location(self.c_main.m_tournament.town)) - 1
        elif event.key == pygame.K_RIGHT:
            self.c_main.m_game.index_location += 1
            if self.c_main.m_game.index_location >= \
                    len(sql.get_location(self.c_main.m_tournament.town)):
                self.c_main.m_game.index_location = 0

    def keyboard_num(self, event):
        """method to manage the num of the keyboard

        Args:
            event (pygame_object): the object where all the interaction are stocked
        """
        letters = {x: pygame.key.key_code(
            x) for x in "1234567890"}
        touche = pygame.key.get_pressed()
        for (letter, value) in letters.items():
            if touche[value]:
                for player in self.c_main.m_round.players:
                    if player.selected:
                        player.score = int(
                            str(player.score) + str(letter))
                        if player.score > 14:
                            player.score = 14

        if event.key == pygame.K_BACKSPACE:
            for player in self.c_main.m_game.round.players:
                if player.selected:
                    player.score = 0
