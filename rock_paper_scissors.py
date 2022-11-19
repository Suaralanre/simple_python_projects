#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
import time


moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""


def print_pause(message):
    time.sleep(0)
    print(message)


class Player:

    score = 0

    def __init__(self):
        self.my_move = None
        self.their_move = None
        self.index = 0

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RockPlayer(Player):
    def move(self):
        return "rock"


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            human_move = input("Please enter rock," +
                               " paper or scissors: ").lower()
            if human_move in moves:
                return human_move
            else:
                print("Please enter a valid input!")


class ReflectPlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            return self.my_move


class CyclePlayer(Player):
    def move(self):
        for i in range(len(moves)):
            self.my_move = moves[self.index]
            self.index = (self.index + 1) % len(moves)
            return self.my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) is True:
            self.p1.score += 1
            print("PLAYER 1 WINS")
            print(f"PLAYER 1: {self.p1.score} | PLAYER 2: {self.p2.score}")

        elif move1 == move2:
            self.p1.score += 0
            self.p2.score += 0
            print("IT IS A TIE!")
            print(f"PLAYER 1: {self.p1.score} | PLAYER 2: {self.p2.score}")

        else:
            self.p2.score += 1
            print("PLAYER 2 WINS")
            print(f"PLAYER 1: {self.p1.score} | PLAYER 2: {self.p2.score}")

        self.p2.learn(move1, move2)

    def who_wins(self):
        print(f"FINAL SCORE-->  PLAYER 1: {self.p1.score}" +
              " | PLAYER 2: {self.p2.score}")
        if self.p1.score == self.p2.score:
            print("NO WINNER CHAMPS; ITS A DRAW!")
        elif self.p1.score > self.p2.score:
            print("PLAYER ONE IS THE CHAMPION! ")
        else:
            print("PLAYER TWO IS THE CHAMPION")

    def play_game(self):
        print_pause("A classic two-person game.")
        print_pause("Players start each round by playing," +
                    " rock, paper or scissors")
        print_pause("The rules of the game are pretty simple:" +
                    " Rock crushes scissors, scissors cut paper," +
                    " and paper covers rock")
        print_pause("This particular game runs in three rounds")
        print_pause("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            print("\n")
        self.who_wins()


if __name__ == '__main__':
    while True:
        game = Game(HumanPlayer(), CyclePlayer())
        game.play_game()
        replies = ['y', 'n']
        replay = ""
        while replay not in replies:
            replay = input("Would you like to play again? y/n ").lower()
        if replay == "y":
            continue
        break
