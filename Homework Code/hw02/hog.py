"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice):
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    assert num_rolls <= 10, 'cannot roll more than 10 dice'
    # BEGIN Question 1
    x = 1
    points = 0
    pig_out = False
    while x < num_rolls+1:
        temp = 0
        temp += dice()
        if temp == 1: 
            pig_out = True #pig out rule
        points += temp
        x +=1
    if pig_out: 
        print('PIG OUT, 1 point added')
        return 1
    else: 
        print(points, 'points added')
        return points
    # END Question 1

def take_turn(num_rolls, opponent_score, dice):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    if num_rolls == 0: #free bacon rule
        print('FREE BACON')
        if opponent_score < 10:
            return opponent_score + 1
        else:
            return (max(opponent_score%10, int(opponent_score/10)) + 1)
    else:  #call roll dice using arguments
        print('Rolling dice')
        return roll_dice(num_rolls, dice)
    # END Question 2

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    if score + opponent_score == 0:
        return six_sided
    elif ((score + opponent_score) % 7) == 0:
        print('Scores are a multiple of 7, using 4 sided dice')
        return four_sided
    else: 
        print('Scores are not a multiple of 7, using 6 sided dice')
        return six_sided
    # END Question 3

def is_swap(score0, score1):
    """Return True if ending a turn with SCORE0 and SCORE1 will result in a
    swap.

    Swaps occur when the last two digits of the first score are the reverse
    of the last two digits of the second score.
    """
    # BEGIN Question 4
    if score0 > 99: score0 -= 100
    if score1 > 99: score1 -= 100
    s0d1, s0d2, s1d1, s1d2 = 0, 0, 0, 0
    s0d1 = int(score0/10)
    s0d2 = score0%10
    s1d1 = int(score1/10)
    s1d2 = score1%10
    if s0d1 == s1d2 and s0d2 == s1d1:
        print('Score0 is the opposite of Score1, SWINE SWAP')
        return True
    else:
        print('Scores are not opposites, no swap')
        return False
    # END Question 4

def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    print('-----Start Game-----')
    while score0 < goal and score1 < goal:
        diceType = select_dice(score0, score1)
        if who == 0:
            score0 += take_turn(strategy0(score0, score1), score1, diceType)
            print('player0 has', score0, 'points')
        else:
            score1 += take_turn(strategy1(score1, score0), score0, diceType)
            print('player1 has', score1, 'points')
        if is_swap(score0, score1):
            temp = score0
            score0 = score1
            score1 = temp
        print("-----SWITCHING PLAYERS-----\n")
        who = other(who)
    # END Question 5
    print("\nResults: Player0 finished with", score0, "points, Player1 finished with", score1, "points")
    return score0, score1

play(always_roll(5), always_roll(5))