""" Module Tournament """

import pygame

from models.date import Date_selected as m_date

# create class game


class Tournament:
    """Object Who will manage the game
    """

    def __init__(self, c_main):
        self.c_main = c_main

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

    # Method about the creation
    def create_tournament(self):
        """ Method to manage the step of creation of the Tournament """

        self.switch_tournament.get(
            self.c_main.m_game.step, self.create_tournament_name)()

    def create_tournament_name(self):
        """ Method for create the tournament's name """

        self.c_main.v_basic.print_sentence(
            "Please enter the name of the tournament")
        bkg_input = self.c_main.v_basic.set_an_image(
            'assets/button/input.png', (700, 150))
        self.c_main.v_basic.manage_view(bkg_input, (((1280 - 700) / 2), 300))
        text = self.c_main.m_game.font.render(
            self.c_main.m_tournament.name, 1, (255, 255, 255))
        self.c_main.v_basic.manage_view(text, (((1280 - 700) / 2 + 50), 340))
        if len(self.c_main.m_tournament.name) > 0:
            self.c_main.v_basic.manage_view(
                self.c_main.m_game.next, self.c_main.m_game.next_rect)

    def create_tournament_place(self):
        """ Method for select the tournament's country """

        if self.c_main.m_game.step == "country":
            sentence = "Please, choose the country"
            self.c_main.v_basic.print_sentence(sentence)
            self.c_main.v_basic.manage_view(
                self.c_main.m_game.next, self.c_main.m_game.next_rect)
            data = self.c_main.m_sql.get_country()
        elif self.c_main.m_game.step == "town":
            sentence = "Please, choose the town"
            self.c_main.v_basic.print_sentence(sentence)
            self.c_main.v_basic.manage_view(
                self.c_main.m_game.next, self.c_main.m_game.next_rect)
            data = self.c_main.m_sql.get_town(self.c_main.m_tournament.country)
        elif self.c_main.m_game.step == "location":
            sentence = "Please, choose the location"
            self.c_main.v_basic.print_sentence(sentence)
            self.c_main.v_basic.manage_view(
                self.c_main.m_game.next, self.c_main.m_game.next_rect)
            data = self.c_main.m_sql.get_location(
                self.c_main.m_tournament.town)

        sentence_tmp = pygame.font.Font(None, 130).render(
            "<  " + str(data[self.c_main.m_game.index_location][1]) + "  >",
            1,
            (255, 255, 255))
        self.c_main.v_basic.manage_view(sentence_tmp, (350, 300))

    def create_tournament_date(self):
        """ Method for select the tournament's date """

        font_date = pygame.font.Font(None, 70)
        self.c_main.v_basic.print_sentence("Please choose the date")
        self.c_main.v_basic.manage_view(
            self.c_main.m_game.next, self.c_main.m_game.next_rect)
        self.c_main.v_basic.print_sentence(str(
            self.c_main.m_tournament.day.str), font_date, self.c_main.m_tournament.day.rect)
        self.c_main.v_basic.print_sentence(str(
            self.c_main.m_tournament.month.str), font_date, self.c_main.m_tournament.month.rect)
        self.c_main.v_basic.print_sentence(str(
            self.c_main.m_tournament.year.str), font_date, self.c_main.m_tournament.year.rect)

    def create_tournament_time(self):
        """ Methode for select the type of time """

        self.c_main.v_basic.print_sentence("Please choose the time style")
        self.c_main.v_basic.manage_view(
            self.c_main.m_game.next, self.c_main.m_game.next_rect)
        self.set_round_time()
        self.c_main.v_basic.manage_view(
            self.c_main.m_game.choice_A, self.c_main.m_game.choice_A_rect)
        self.c_main.v_basic.manage_view(
            self.c_main.m_game.choice_B, self.c_main.m_game.choice_B_rect)
        self.c_main.v_basic.manage_view(
            self.c_main.m_game.choice_C, self.c_main.m_game.choice_C_rect)
        self.c_main.v_basic.print_sentence(
            "bullet", self.c_main.m_game.font, (130, 310))
        self.c_main.v_basic.print_sentence(
            "blitz", self.c_main.m_game.font, (530, 310))
        self.c_main.v_basic.print_sentence(
            "speed shot", self.c_main.m_game.font, (930, 310))

    def set_time(self):
        """ Method for se't up the rect of time management """

        # set up the day month and year in pygame format

        self.c_main.m_tournament.day = m_date("%d", 400, 300)
        self.c_main.m_tournament.month = m_date("%m", 620, 300)
        self.c_main.m_tournament.year = m_date("%Y", 840, 300)

    def set_round_time(self):
        """ Methode for update the display of the time selector """

        self.c_main.m_game.choice_A = self.c_main.v_basic.set_an_image(
            'assets/button/round.png', (60, 60))
        self.c_main.m_game.choice_A_rect = self.c_main.v_basic.set_an_image_rec(
            self.c_main.m_game.choice_A, 50, 300)
        self.c_main.m_game.choice_B = self.c_main.v_basic.set_an_image(
            'assets/button/round.png', (60, 60))
        self.c_main.m_game.choice_B_rect = self.c_main.v_basic.set_an_image_rec(
            self.c_main.m_game.choice_B, 450, 300)
        self.c_main.m_game.choice_C = self.c_main.v_basic.set_an_image(
            'assets/button/round.png', (60, 60))
        self.c_main.m_game.choice_C_rect = self.c_main.v_basic.set_an_image_rec(
            self.c_main.m_game.choice_C, 850, 300)

        if self.c_main.m_game.choice == 1:
            self.c_main.m_game.choice_A = self.c_main.v_basic.set_an_image(
                'assets/button/round_selected.png', (60, 60))
        if self.c_main.m_game.choice == 2:
            self.c_main.m_game.choice_B = self.c_main.v_basic.set_an_image(
                'assets/button/round_selected.png', (60, 60))
        if self.c_main.m_game.choice == 3:
            self.c_main.m_game.choice_C = self.c_main.v_basic.set_an_image(
                'assets/button/round_selected.png', (60, 60))

    def create_tournament_description(self):
        """ Methode for write the description of the tournament """

        self.c_main.v_basic.print_sentence(
            "Please enter the tournament's description")
        bkg_input = self.c_main.v_basic.set_an_image(
            'assets/button/input.png', (700, 150))
        self.c_main.v_basic.manage_view(bkg_input, (((1280 - 700) / 2), 300))
        text_tmp = self.c_main.m_tournament.description
        text_y = 320
        while len(text_tmp) > 0:
            font = pygame.font.Font(None, 35)
            self.c_main.v_basic.print_sentence(
                text_tmp[:50], font, (((1280 - 700) / 2 + 10), text_y))
            text_tmp = text_tmp[50:]
            text_y += 30
        if len(self.c_main.m_tournament.description) > 0:
            self.c_main.v_basic.manage_view(
                self.c_main.m_game.next, self.c_main.m_game.next_rect)

    def create_tournament_player(self):
        """ Methode for select the player of the tournament """

        tmp_p = 8 - len(self.c_main.m_game.players)
        self.c_main.v_basic.print_sentence(
            f"Please select the {tmp_p} players", self.c_main.m_game.font, (340, 50))

        # check if all the players have been selected
        if len(self.c_main.m_game.players) == 8:
            self.c_main.v_basic.manage_view(
                self.c_main.m_game.next, self.c_main.m_game.next_rect)
        else:
            bkg_input = self.c_main.v_basic.set_an_image(
                'assets/button/input.png', (600, 75))
            self.c_main.v_basic.manage_view(bkg_input, (310, 100))
            self.c_main.v_basic.manage_view(
                self.c_main.m_game.search_button, self.c_main.m_game.search_button_rect)
            self.c_main.v_basic.print_sentence(
                self.c_main.m_game.players_search, self.c_main.m_game.font, (330, 120))
            self.c_main.v_basic.print_sentence(
                "player name", self.c_main.m_game.font, (20, 120))
            self.search_player()

    def search_player(self):
        """ method to search the players """

        if len(self.c_main.m_game.players_search) > 0:
            # get the list of player in the bdd
            request = self.c_main.m_sql.get_players(
                self.c_main.m_game.players_search)
            index = 0
            tmp_x = 250
            tmp_y = 250

            # set up the button to false, in case of less than 8 result
            for tmp in self.c_main.m_game.tmp_players:
                tmp.show = False
            for player in request:
                font = pygame.font.Font(None, 35)
                self.c_main.v_basic.print_sentence(
                    player[1] + " " + player[2], font, (tmp_x, tmp_y))
                if index == 3:
                    tmp_y = 250
                    tmp_x = 700
                else:
                    tmp_y += 100
                self.c_main.m_game.tmp_players[index].show = True
                self.c_main.m_game.tmp_players[index].id_player = player[0]
                index += 1

            # check if the player has been already selected or if the button have to be seen
            for tmp in self.c_main.m_game.tmp_players:
                if tmp.show:
                    if tmp.id_player not in self.c_main.m_game.players:
                        self.c_main.v_basic.manage_view(tmp.img, tmp.rect)

    def create_tournament_end(self):
        """ Method to save the tournament in the bdd """
        # save the tournament in the db
        data = (self.c_main.m_tournament.name,
                self.c_main.m_tournament.location[0],
                self.c_main.m_tournament.nb_turn,
                self.c_main.m_tournament.description,
                self.c_main.m_tournament.time,
                self.c_main.m_tournament.date
                )
        self.c_main.m_sql.create_tournament(data, self.c_main.m_game.players)
        self.c_main.m_tournament.id = self.c_main.m_sql.get_tournament_id(
            [self.c_main.m_tournament.name, self.c_main.m_tournament.description, self.c_main.m_tournament.date])
        self.c_main.m_tournament.id = self.c_main.m_tournament.id[0][0]
        self.c_main.m_game.step = "next"

    def resume_tournament(self):
        """Method to resume the informations of the tournament """

        list_resume = [["Tournament resume", pygame.font.Font(None, 35), (340, 50)],
                       [f"Name: {self.c_main.m_tournament.name}",
                           pygame.font.Font(None, 35), (340, 100)],
                       [f"Country: {self.c_main.m_tournament.country}",
                           pygame.font.Font(None, 35), (340, 150)],
                       [f"Town: {self.c_main.m_tournament.town}",
                           pygame.font.Font(None, 35), (340, 200)],
                       [f"Location: {self.c_main.m_tournament.location}",
                           pygame.font.Font(None, 35), (340, 250)],
                       [f"Date: {self.c_main.m_tournament.date}",
                           pygame.font.Font(None, 35), (340, 300)],
                       [f"Time: {self.c_main.m_tournament.time}",
                           pygame.font.Font(None, 35), (340, 350)],
                       [f"Description: {self.c_main.m_tournament.description}",
                           pygame.font.Font(None, 35), (340, 400)],
                       [f"Players: {self.c_main.m_tournament.players}", pygame.font.Font(None, 35), (340, 450)]]
        for resume in list_resume:
            self.c_main.v_basic.print_sentence(resume[0], resume[1], resume[2])
        self.c_main.v_basic.manage_view(
            self.c_main.m_game.start, self.c_main.m_game.start_rect)
        self.c_main.m_game.next_up = False
