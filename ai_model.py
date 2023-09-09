# install tensorforce

import numpy as np
import tensorflow as tf
import tensorforce as tfc
from tensorforce.agents import Agent
from tensorforce.environments import Environment
from tensorforce.execution import Runner

#Create a custom environment based on reversi game
class ReversiEnvironment(Environment):
    def __init__(self):
        super().__init__()
        self.board = np.zeros((8,8), dtype=np.int32)
        self.board[3,3] = 1
        self.board[3,4] = -1
        self.board[4,3] = -1
        self.board[4,4] = 1
        self.current_player = 1
        self.winner = 0
        self.done = False
        self.reward = 0

    def states(self):
        return dict(type='int', shape=(8,8), num_values=3)

    def actions(self):
        return dict(type='int', num_values=64)

    # Reset the environment
    def reset(self):
        self.board = np.zeros((8,8), dtype=np.int32)
        self.board[3,3] = 1
        self.board[3,4] = -1
        self.board[4,3] = -1
        self.board[4,4] = 1
        self.current_player = 1
        self.winner = 0
        self.done = False
        self.reward = 0
        return self.board

    # Execute one step within the environment
    def execute(self, actions):
        # Check if the game is done
        if self.done:
            raise Exception('Episode is done')

        # Check if the action is valid
        if self.board[actions//8, actions%8] != 0:
            raise Exception('Invalid action')

        # Update the board
        self.board[actions//8, actions%8] = self.current_player

        # Check if the game is done
        self.done = self.check_done()

        # Update the reward
        self.reward = self.get_reward()

        # Update the current player
        self.current_player = -self.current_player

        return self.board, self.done, self.reward

    # Check if the game is done
    def check_done(self):
        # Check if the board is full
        if np.count_nonzero(self.board) == 64:
            return True

        # Check if the current player has valid moves
        for i in range(8):
            for j in range(8):
                if self.board[i,j] == 0:
                    if self.check_valid(i, j, self.current_player):
                        return False
        