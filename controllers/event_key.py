import pygame

class EventKey:

    def __init__(self, c_main):
        self.c_main = c_main

    def keybord_abc(self):
        letters = {x: pygame.key.key_code(
                        x) for x in "abcdefghijklmnopqrstuvwxyz"}
        touche = pygame.key.get_pressed()
        for (l, value) in letters.items():
            if touche[value]:
                if self.c_main.m_game.step == "name":
                    if len(self.c_main.m_tournament.description) < 50:
                        self.c_main.m_tournament.name = self.c_main.m_tournament.name + \
                            str(l)
                elif self.c_main.m_game.step == "description":
                    if len(self.c_main.m_tournament.description) < 200:
                        self.c_main.m_tournament.description = self.c_main.m_tournament.description + \
                            str(l)
                elif self.c_main.m_game.step == "player":
                    self.c_main.m_game.players_search = self.c_main.m_game.players_search + \
                        str(l)

    def keyboard_space(self):
        if self.c_main.m_game.step == "name":
            self.c_main.m_tournament.name = self.c_main.m_tournament.name + " "
        elif self.c_main.m_game.step == "description":
            self.c_main.m_tournament.description = self.c_main.m_tournament.description + " "
        elif self.c_main.m_game.step == "player":
            self.c_main.m_game.players_search = self.c_main.m_game.players_search + " "

    def keyboard_backspace(self):
        if self.c_main.m_game.step == "name":
            self.c_main.m_tournament.name = self.c_main.m_tournament.name[:-1]
        elif self.c_main.m_game.step == "description":
            self.c_main.m_tournament.description = self.c_main.m_tournament.description[:-1]
        elif self.c_main.m_game.step == "player":
            self.c_main.m_game.players_search = self.c_main.m_game.players_search[:-1]

    def keyboard_coutry(self, event, sql):
        if event.key == pygame.K_LEFT:
            self.c_main.m_game.index_location -= 1
            if self.c_main.m_game.index_location < 0:
                self.c_main.m_game.index_location = len(sql.get_country()) - 1
        elif event.key == pygame.K_RIGHT:
            self.c_main.m_game.index_location += 1
            if self.c_main.m_game.index_location >= len(sql.get_country()):
                self.c_main.m_game.index_location = 0
    
    def keyboard_town(self, event, sql):
        if event.key == pygame.K_LEFT:
            self.c_main.m_game.index_location -= 1
            if self.c_main.m_game.index_location < 0:
                self.c_main.m_game.index_location = len(
                    self.c_main.m_game.m_sql.get_town(self.c_main.m_tournament.country)) - 1
        elif event.key == pygame.K_RIGHT:
            self.c_main.m_game.index_location += 1
            if self.c_main.m_game.index_location >= len(sql.get_town(self.c_main.m_tournament.country)):
                self.c_main.m_game.index_location = 0

    def keyboard_location(self, event, sql):
        if event.key == pygame.K_LEFT:
            self.c_main.m_game.index_location -= 1
            if self.c_main.m_game.index_location < 0:
                self.c_main.m_game.index_location = len(sql.get_location(self.c_main.m_tournament.town)) - 1
        elif event.key == pygame.K_RIGHT:
            self.c_main.m_game.index_location += 1
            if self.c_main.m_game.index_location >= len(sql.get_location(self.c_main.m_tournament.town)):
                self.c_main.m_game.index_location = 0

    def keyboard_num(self, event):
        letters = {x: pygame.key.key_code(
            x) for x in "1234567890"}
        touche = pygame.key.get_pressed()
        for (l, value) in letters.items():
            if touche[value]:
                for player in self.c_main.m_round.players:
                    if player.selected:
                        player.score = int(
                            str(player.score) + str(l))
                        if player.score > 14:
                            player.score = 14

        if event.key == pygame.K_BACKSPACE:
            for player in self.c_main.m_game.round.players:
                if player.selected:
                    player.score = 0
