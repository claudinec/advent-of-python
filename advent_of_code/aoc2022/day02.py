# Day 2: Rock Paper Scissors

import os

# The first column is what your opponent is going to play: A for Rock,
# B for Paper, and C for Scissors.

# The second column, you reason, must be what you should play in response:
# X for Rock, Y for Paper, and Z for Scissors.

# Your total score is the sum of your scores for each round. The score for
# a single round is the score for the shape you selected (1 for Rock,
# 2 for Paper, and 3 for Scissors) plus the score for the outcome of
# the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

SCORING_DICT = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

def rps_score(data_suffix: str) -> int:
    print(data_suffix)
    data_file = os.path.join('data', f'day02-{data_suffix}.txt')
    total_score = 0
    # One round per line.
    with open(data_file, 'r', encoding='utf8') as rps_guide:
        for line in rps_guide:
            rps_round = line.strip()
            [their_choice, my_choice] = rps_round.split(' ')
            # Score for my choice.
            choice_score = SCORING_DICT[my_choice]
            # Did I win?
            match [their_choice, my_choice]:
                case ['A', 'Y'] | ['B', 'Z'] | ['C', 'X']:
                    win_score = 6
                case ['A', 'X'] | ['B', 'Y'] | ['C', 'Z']:
                    win_score = 3
                case ['A', 'Z'] | ['B', 'X'] | ['C', 'Y']:
                    win_score = 0
            # Score for the round.
            round_score = choice_score + win_score
            # Total score.
            total_score = total_score + round_score
    print(total_score)
    return total_score

rps_score('example')
