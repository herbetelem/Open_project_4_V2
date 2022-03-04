import pygame

class EventKey:

    def __init__(self, game):
        self.game = game

    def keybord_abc(self):
        letters = {x: pygame.key.key_code(
                        x) for x in "abcdefghijklmnopqrstuvwxyz"}
        touche = pygame.key.get_pressed()
        for (l, value) in letters.items():
            if touche[value]:
                if self.game.step == "name":
                    if len(self.game.tournament.description) < 50:
                        self.game.tournament.name = self.game.tournament.name + \
                            str(l)
                elif self.game.step == "description":
                    if len(self.game.tournament.description) < 200:
                        self.game.tournament.description = self.game.tournament.description + \
                            str(l)
                elif self.game.step == "player":
                    self.game.players_search = self.game.players_search + \
                        str(l)

    def keyboard_space(self):
        if self.game.step == "name":
            self.game.tournament.name = self.game.tournament.name + " "
        elif self.game.step == "description":
            self.game.tournament.description = self.game.tournament.description + " "
        elif self.game.step == "player":
            self.game.players_search = self.game.players_search + " "

    def keyboard_backspace(self):
        if self.game.step == "name":
            self.game.tournament.name = self.game.tournament.name[:-1]
        elif self.game.step == "description":
            self.game.tournament.description = self.game.tournament.description[:-1]
        elif self.game.step == "player":
            self.game.players_search = self.game.players_search[:-1]

    def keyboard_coutry(self, event, sql):
        if event.key == pygame.K_LEFT:
            self.game.index_location -= 1
            if self.game.index_location < 0:
                self.game.index_location = len(sql.get_country()) - 1
        elif event.key == pygame.K_RIGHT:
            self.game.index_location += 1
            if self.game.index_location >= len(sql.get_country()):
                self.game.index_location = 0
    
    def keyboard_town(self, event, sql):
        if event.key == pygame.K_LEFT:
            self.game.index_location -= 1
            if self.game.index_location < 0:
                self.game.index_location = len(
                    self.game.sql.get_town(self.game.tournament.country)) - 1
        elif event.key == pygame.K_RIGHT:
            self.game.index_location += 1
            if self.game.index_location >= len(sql.get_town(self.game.tournament.country)):
                self.game.index_location = 0

    def keyboard_location(self, event, sql):
        if event.key == pygame.K_LEFT:
            self.game.index_location -= 1
            if self.game.index_location < 0:
                self.game.index_location = len(sql.get_location(self.game.tournament.town)) - 1
        elif event.key == pygame.K_RIGHT:
            self.game.index_location += 1
            if self.game.index_location >= len(sql.get_location(self.game.tournament.town)):
                self.game.index_location = 0

    def keyboard_num(self, event):
        letters = {x: pygame.key.key_code(
            x) for x in "1234567890"}
        touche = pygame.key.get_pressed()
        for (l, value) in letters.items():
            if touche[value]:
                for player in self.game.round.players:
                    if player.selected:
                        player.score = int(
                            str(player.score) + str(l))
                        if player.score > 14:
                            player.score = 14

        if event.key == pygame.K_BACKSPACE:
            for player in self.game.round.players:
                if player.selected:
                    player.score = 0
