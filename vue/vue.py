import pygame
from turtle import pd

from add_player import Add_player
from date_select import Date_selected
from load_a_tournament import Load_a_tournament
from round import Round
from SQL_function import SQL_function
from tournament import Tournament

# create class game


class VueBasic:
    """Object Who will manage the game
    """

    def __init__(self, screen):
        self.screen = screen

    
    # Method general
    def print_sentence(self, sentence, font=False, position=(340, 100)):
        """ the Methode to print a sentence in the game

        Args:
            sentence (string): the string to print
            font ([object pygame]): the font who will be use on the print
            position (tuple, optional): the position of the print. Defaults to (340, 100).
        """

        if not font:
            font = self.font
        text = font.render(sentence, 1, (255, 255, 255))
        self.screen.blit(text, position)

    def set_an_image(self, path, size=False):
        """ Method to set up an image

        Args:
            path (str): path to the image
            size (bool, optional): size of the images

        Returns:
            object: object img pygame
        """
        img = pygame.image.load(path)
        if size:
            img = pygame.transform.scale(img, size)
        return img

    def set_an_image_rec(self, img, x, y):
        """ Method to set up an image

        Args:
            path (str): path to the image
            size (bool, optional): size of the images

        Returns:
            object: object img pygame resized
        """
        img_rect = img.get_rect()
        img_rect.x = x
        img_rect.y = y
        return img_rect

    def manage_view(self, vue, vue_rect):
        self.screen.blit(vue, vue_rect)