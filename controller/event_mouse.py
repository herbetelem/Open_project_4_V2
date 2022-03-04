from model.game import Game


class EventMouse():

    def __init__(self, game, main):
        self.game = game
        self.main = main

    def manage_first_menu(self, event):
        if self.main.play_button_rect.collidepoint(event.pos):
            self.game.is_launch = True
            self.game.step = "name"
        if self.main.load_button_rect.collidepoint(event.pos):
            self.game.load = True

    def manage_load_button(self, event):
        for button in self.game.history_button:
            if button.rect.collidepoint(event.pos):
                self.game.match_load = button.id_tournament
            if self.game.prev_rect.collidepoint(event.pos):
                self.game.match_load = False

    def manage_end_creation(self):
        if self.game.tournament.created is False:
            self.game.set_var_game()
            self.game.tournament.created = True

    def manage_date(self, event):
        if self.game.day.rect.collidepoint(event.pos):
            if self.game.day.str == 31:
                self.game.day.str = 1
            else:
                self.game.day.str += 1
        if self.game.month.rect.collidepoint(event.pos):
            if self.game.month.str == 12:
                self.game.month.str = 1
            else:
                self.game.month.str += 1
        if self.game.year.rect.collidepoint(event.pos):
            self.game.year.str += 1

    def manage_time(self, event):
        if self.game.choice_A_rect.collidepoint(event.pos):
            self.game.choice = 1
        if self.game.choice_B_rect.collidepoint(event.pos):
            self.game.choice = 2
        if self.game.choice_C_rect.collidepoint(event.pos):
            self.game.choice = 3

    def manage_player(self, event):
        for button in self.game.tmp_players:
            if button.rect.collidepoint(event.pos):
                if button.id_player not in self.game.players and \
                        len(self.game.players_search) > 0:
                    self.game.players.append(button.id_player)
                    self.game.players_search = ""
                    self.game.step = "player"

    def manage_button_edit(self, event):
        for player in self.game.round.players:
            if player.rect.collidepoint(event.pos):
                for all_player in self.game.round.players:
                    all_player.img = self.game.set_an_image(
                        'assets/button/editer.png', (150, 50))
                    all_player.selected = False
                player.img = self.game.set_an_image(
                    'assets/button/editer-check.png', (150, 50))
                player.selected = True
    
    def validate_round_check(self, event):
        if self.game.validate_rect.collidepoint(event.pos):
            self.game.round.generate_round()
            self.game.round.settings = False

            ###### RENDRE GENERIQUE #############
            self.game.deck_1 = self.main.v_vue.set_an_image('../assets/match-no-result.png', (140, 140))
            self.game.deck_2 = self.main.v_vue.set_an_image('../assets/match-no-result.png', (140, 140))
            self.game.deck_3 = self.main.v_vue.set_an_image('../assets/match-no-result.png', (140, 140))
            self.game.deck_4 = self.main.v_vue.set_an_image('../assets/match-no-result.png', (140, 140))
            ###### RENDRE GENERIQUE #############
    
    def manage_deck(self, event):
        ###### RENDRE GENERIQUE #############
        if self.game.deck_1_rect.collidepoint(event.pos):
            self.game.deck_1 = self.main.v_vue.set_an_image('../assets/match-nul.png', (140, 140))
            self.game.round.match[0][2] = 3

        elif self.game.area_win_1.collidepoint(event.pos):
            self.game.deck_1 = self.main.v_vue.set_an_image('../assets/match-win-1.png', (140, 140))
            self.game.round.match[0][2] = 1

        elif self.game.area_win_2.collidepoint(event.pos):
            self.game.deck_1 = self.main.v_vue.set_an_image('../assets/match-win-2.png', (140, 140))
            self.game.round.match[0][2] = 2

        #  Manage Game desk 2
        if self.game.deck_2_rect.collidepoint(event.pos):
            self.game.deck_2 = self.main.v_vue.set_an_image('../assets/match-nul.png', (140, 140))
            self.game.round.match[1][2] = 3

        elif self.game.area_win_3.collidepoint(event.pos):
            self.game.deck_2 = self.main.v_vue.set_an_image('../assets/match-win-1.png', (140, 140))
            self.game.round.match[1][2] = 1

        elif self.game.area_win_4.collidepoint(event.pos):
            self.game.deck_2 = self.main.v_vue.set_an_image('../assets/match-win-2.png', (140, 140))
            self.game.round.match[1][2] = 2

        #  Manage Game desk 3
        if self.game.deck_3_rect.collidepoint(event.pos):
            self.game.deck_3 = self.main.v_vue.set_an_image('../assets/match-nul.png', (140, 140))
            self.game.round.match[2][2] = 3

        elif self.game.area_win_5.collidepoint(event.pos):
            self.game.deck_3 = self.main.v_vue.set_an_image('../assets/match-win-1.png', (140, 140))
            self.game.round.match[2][2] = 1

        elif self.game.area_win_6.collidepoint(event.pos):
            self.game.deck_3 = self.main.v_vue.set_an_image('../assets/match-win-2.png', (140, 140))
            self.game.round.match[2][2] = 2

        #  Manage Game desk 4
        if self.game.deck_4_rect.collidepoint(event.pos):
            self.game.deck_4 = self.main.v_vue.set_an_image('../assets/match-nul.png', (140, 140))
            self.game.round.match[3][2] = 3

        elif self.game.area_win_7.collidepoint(event.pos):
            self.game.deck_4 = self.main.v_vue.set_an_image('../assets/match-win-1.png', (140, 140))
            self.game.round.match[3][2] = 1

        elif self.game.area_win_8.collidepoint(event.pos):
            self.game.deck_4 = self.main.v_vue.set_an_image('../assets/match-win-2.png', (140, 140))
            self.game.round.match[3][2] = 2
        ###### RENDRE GENERIQUE #############
        pass

    def validate_round(self, event):
        if self.game.validate_rect.collidepoint(event.pos):
            result = []
            for match in self.game.round.match:
                result.append(match[2])
            self.game.round.validate_round(result)
            if self.game.round.nb_turn < 7:
                self.game.round.generate_round()
                ########### RENDRE GENERIQUE #############
                self.game.deck_1 = self.main.v_vue.set_an_image('../assets/match-no-result.png', (140, 140))
                self.game.deck_2 = self.main.v_vue.set_an_image('../assets/match-no-result.png', (140, 140))
                self.game.deck_3 = self.main.v_vue.set_an_image('../assets/match-no-result.png', (140, 140))
                self.game.deck_4 = self.main.v_vue.set_an_image('../assets/match-no-result.png', (140, 140))
            else:
                self.game.game_statut = False
                ########### RENDRE GENERIQUE #############

    def update_score(self, event):
            # Mannage save
        for player in self.game.round.players:
            self.game.sql.save_score(
                (player.id, self.game.tournament.id, player.score))
        self.game = Game(self.game.screen)

    def test():
        elif game.update_score_rect.collidepoint(event.pos):
            self.game.round.settings = True

                # Mannage save
                if self.game.round.nb_turn == 7 and game.save_rect.collidepoint(event.pos):
                    for player in self.game.round.players:
                        game.sql.save_score(
                            (player.id, game.tournament.id, player.score))
                    game = Game(screen)
