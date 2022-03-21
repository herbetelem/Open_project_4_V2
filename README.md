# Project Openclassroom Développez un programme logiciel en Python
[![forthebadge](http://forthebadge.com/images/badges/works-on-my-machine.svg)](http://forthebadge.com)  [![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

The goal of this project is to create a program allowing the creation and management of chess tournaments, while storing the results in a database.

## First version

this project is a review from a old version, i have created this one with the MVC patern
- link: https://github.com/herbetelem/Open_project_4

## Launching

For lauching this projet, we will use the file main.py in the terminal

### Prerequisites

You will need

- pygame https://www.pygame.org/wiki/GettingStarted

### Installation

Into your file use comand ``pip install -r requirement.txt`` for install all librairy


## Launching

Just Use this commmand ``python main.py``


## Flake8-html

the flake8 have been generate into the folder flake-report
If you want to generate an other one une this command ``flake8 --format=html --htmldir=flake-report --max-line-length=119``


## Functional

On the first menu choose whether you want to load tournament data, or create a new one
If you select:
- load: in this case, you will have a list of previously completed tournaments, you can choose one to see its ranking
- new game: in this case you will have 2 more step:
  - create the tournament: in this step you will have to enter the information requested at each step, then validated so that the tournament is created and saved in the database
  - manage the tournament: in this step you will have to generate the round once, select per match the player who won or the board in case of a draw, then validate the round

## Made with

* [Visual Studio Code](https://code.visualstudio.com/) - Code editor


## Author

* **Hadrien Herbet** _alias_ [@herbetelem](https://github.com/herbetelem)
