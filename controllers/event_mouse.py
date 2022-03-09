from models.game import Game


class EventMouse():

    def __init__(self, c_main):
        self.c_main = c_main

    def manage_first_menu(self, event):
        if self.c_main.play_button_rect.collidepoint(event.pos):
            self.c_main.m_game.is_launch = True
            self.c_main.m_game.step = "name"
        if self.c_main.load_button_rect.collidepoint(event.pos):
            self.c_main.m_game.load = True

    def manage_load_button(self, event):
        for button in self.c_main.m_game.history_button:
            if button.rect.collidepoint(event.pos):
                self.c_main.m_game.match_load = button.id_tournament
            if self.c_main.m_game.prev_rect.collidepoint(event.pos):
                self.c_main.m_game.match_load = False

    def manage_end_creation(self):
        if self.c_main.m_tournament.created is False:
            self.c_main.m_game.set_var_game()
            self.c_main.m_tournament.created = True

    def manage_date(self, event):
        if self.c_main.m_tournament.day.rect.collidepoint(event.pos):
            if self.c_main.m_tournament.day.str == 31:
                self.c_main.m_tournament.day.str = 1
            else:
                self.c_main.m_tournament.day.str += 1
        if self.c_main.m_tournament.month.rect.collidepoint(event.pos):
            if self.c_main.m_tournament.month.str == 12:
                self.c_main.m_tournament.month.str = 1
            else:
                self.c_main.m_tournament.month.str += 1
        if self.c_main.m_tournament.year.rect.collidepoint(event.pos):
            self.c_main.m_tournament.year.str += 1

    def manage_time(self, event):
        if self.c_main.m_game.choice_A_rect.collidepoint(event.pos):
            self.c_main.m_game.choice = 1
        if self.c_main.m_game.choice_B_rect.collidepoint(event.pos):
            self.c_main.m_game.choice = 2
        if self.c_main.m_game.choice_C_rect.collidepoint(event.pos):
            self.c_main.m_game.choice = 3

    def manage_player(self, event):
        for button in self.c_main.m_game.tmp_players:
            if button.rect.collidepoint(event.pos):
                if button.id_player not in self.c_main.m_game.players and \
                        len(self.c_main.m_game.players_search) > 0:
                    self.c_main.m_game.players.append(button.id_player)
                    self.c_main.m_game.players_search = ""
                    self.c_main.m_game.step = "player"

    def manage_button_edit(self, event):
        for player in self.c_main.m_round.players:
            if player.rect.collidepoint(event.pos):
                for all_player in self.c_main.m_round.players:
                    all_player.img = self.c_main.v_basic.set_an_image(
                        'assets/button/editer.png', (150, 50))
                    all_player.selected = False
                player.img = self.c_main.v_basic.set_an_image(
                    'assets/button/editer-check.png', (150, 50))
                player.selected = True
    
    def validate_round_check(self, event):
        if self.c_main.m_game.validate_rect.collidepoint(event.pos):
            self.c_main.c_round.generate_round()
            self.c_main.m_round.settings = False

            ###### RENDRE GENERIQUE #############
            self.c_main.m_game.deck_1 = self.c_main.v_basic.set_an_image('assets/match-no-result.png', (140, 140))
            self.c_main.m_game.deck_2 = self.c_main.v_basic.set_an_image('assets/match-no-result.png', (140, 140))
            self.c_main.m_game.deck_3 = self.c_main.v_basic.set_an_image('assets/match-no-result.png', (140, 140))
            self.c_main.m_game.deck_4 = self.c_main.v_basic.set_an_image('assets/match-no-result.png', (140, 140))
            ###### RENDRE GENERIQUE #############
    
    def manage_deck(self, event):
        ###### RENDRE GENERIQUE #############
        if self.c_main.m_game.deck_1_rect.collidepoint(event.pos):
            self.c_main.m_game.deck_1 = self.c_main.v_basic.set_an_image('assets/match-nul.png', (140, 140))
            self.c_main.m_round.match[0][2] = 3

        elif self.c_main.m_game.area_win_1.collidepoint(event.pos):
            self.c_main.m_game.deck_1 = self.c_main.v_basic.set_an_image('assets/match-win-1.png', (140, 140))
            self.c_main.m_round.match[0][2] = 1

        elif self.c_main.m_game.area_win_2.collidepoint(event.pos):
            self.c_main.m_game.deck_1 = self.c_main.v_basic.set_an_image('assets/match-win-2.png', (140, 140))
            self.c_main.m_round.match[0][2] = 2

        #  Manage Game desk 2
        if self.c_main.m_game.deck_2_rect.collidepoint(event.pos):
            self.c_main.m_game.deck_2 = self.c_main.v_basic.set_an_image('assets/match-nul.png', (140, 140))
            self.c_main.m_round.match[1][2] = 3

        elif self.c_main.m_game.area_win_3.collidepoint(event.pos):
            self.c_main.m_game.deck_2 = self.c_main.v_basic.set_an_image('assets/match-win-1.png', (140, 140))
            self.c_main.m_round.match[1][2] = 1

        elif self.c_main.m_game.area_win_4.collidepoint(event.pos):
            self.c_main.m_game.deck_2 = self.c_main.v_basic.set_an_image('assets/match-win-2.png', (140, 140))
            self.c_main.m_round.match[1][2] = 2

        #  Manage Game desk 3
        if self.c_main.m_game.deck_3_rect.collidepoint(event.pos):
            self.c_main.m_game.deck_3 = self.c_main.v_basic.set_an_image('assets/match-nul.png', (140, 140))
            self.c_main.m_round.match[2][2] = 3

        elif self.c_main.m_game.area_win_5.collidepoint(event.pos):
            self.c_main.m_game.deck_3 = self.c_main.v_basic.set_an_image('assets/match-win-1.png', (140, 140))
            self.c_main.m_round.match[2][2] = 1

        elif self.c_main.m_game.area_win_6.collidepoint(event.pos):
            self.c_main.m_game.deck_3 = self.c_main.v_basic.set_an_image('assets/match-win-2.png', (140, 140))
            self.c_main.m_round.match[2][2] = 2

        #  Manage Game desk 4
        if self.c_main.m_game.deck_4_rect.collidepoint(event.pos):
            self.c_main.m_game.deck_4 = self.c_main.v_basic.set_an_image('assets/match-nul.png', (140, 140))
            self.c_main.m_round.match[3][2] = 3

        elif self.c_main.m_game.area_win_7.collidepoint(event.pos):
            self.c_main.m_game.deck_4 = self.c_main.v_basic.set_an_image('assets/match-win-1.png', (140, 140))
            self.c_main.m_round.match[3][2] = 1

        elif self.c_main.m_game.area_win_8.collidepoint(event.pos):
            self.c_main.m_game.deck_4 = self.c_main.v_basic.set_an_image('assets/match-win-2.png', (140, 140))
            self.c_main.m_round.match[3][2] = 2
        ###### RENDRE GENERIQUE #############
        pass

    def validate_round(self, event):
        if self.c_main.m_game.validate_rect.collidepoint(event.pos):
            result = []
            for match in self.c_main.m_round.match:
                result.append(match[2])
            self.c_main.c_round.validate_round(result)
            if self.c_main.m_round.nb_turn < 7:
                self.c_main.c_round.generate_round()
                ########### RENDRE GENERIQUE #############
                self.c_main.m_game.deck_1 = self.c_main.v_basic.set_an_image('assets/match-no-result.png', (140, 140))
                self.c_main.m_game.deck_2 = self.c_main.v_basic.set_an_image('assets/match-no-result.png', (140, 140))
                self.c_main.m_game.deck_3 = self.c_main.v_basic.set_an_image('assets/match-no-result.png', (140, 140))
                self.c_main.m_game.deck_4 = self.c_main.v_basic.set_an_image('assets/match-no-result.png', (140, 140))
            else:
                self.c_main.m_game.game_statut = False
                ########### RENDRE GENERIQUE #############

    def update_score(self, event):
            # Mannage save
        for player in self.c_main.m_round.players:
            self.c_main.m_sql.save_score(
                (player.id, self.c_main.m_tournament.id, player.score))
        self.c_main.m_game = Game(self.c_main)
