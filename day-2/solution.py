# part 1

# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

test_input = """A Y
B X
C Z"""


# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
def decrypt_guide(encrypted_msg):
    decryption_map = {
        'A': 'Rock',
        'X': 'Rock',
        'B': 'Paper',
        'Y': 'Paper',
        'C': 'Scissors',
        'Z': 'Scissors'}
    return decryption_map[encrypted_msg]

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock


def calculate_round_score(dec_opponent_choise, dec_your_choise):
    shapes_scores = {
        'Rock': 1,
        'Paper': 2,
        'Scissors': 3}

    if dec_opponent_choise == dec_your_choise:
        return 3 + shapes_scores[dec_your_choise]

    if dec_your_choise + dec_opponent_choise in ['RockScissors', 'ScissorsPaper', 'PaperRock']:
        return 6 + shapes_scores[dec_your_choise]

    return 0 + shapes_scores[dec_your_choise]


def part_one(input):
    rounds = input.splitlines()
    total_score = 0
    for round in rounds:
        opponent_choise, your_choise = round.split(' ')

        dec_opponent_choise = decrypt_guide(opponent_choise)
        dec_your_choise = decrypt_guide(your_choise)

        total_score += calculate_round_score(
            dec_opponent_choise, dec_your_choise)

    return total_score


assert part_one(test_input) == 15

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock


def decrypt_ultra_guide(strategy, dec_opponent_choise):
    your_ultra_choise = ''
    if strategy == 'Y':
        your_ultra_choise = dec_opponent_choise
    elif strategy == 'X':
        defeat_map = {
            'Rock': 'Scissors',
            'Scissors': 'Paper',
            'Paper':  'Rock'}
        your_ultra_choise = defeat_map[dec_opponent_choise]
    elif strategy == 'Z':
        win_map = {
            'Scissors': 'Rock',
            'Paper': 'Scissors',
            'Rock': 'Paper'}
        your_ultra_choise = win_map[dec_opponent_choise]
    return your_ultra_choise


def part_two(input):
    rounds = input.splitlines()
    total_score = 0
    for round in rounds:
        opponent_choise, your_strategy = round.split(' ')

        dec_opponent_choise = decrypt_guide(opponent_choise)
        dec_your_choise = decrypt_ultra_guide(
            your_strategy, dec_opponent_choise)

        total_score += calculate_round_score(
            dec_opponent_choise, dec_your_choise)

    return total_score


assert part_two(test_input) == 12

puzzle_input = open("input.txt", "r").read()

# part one solution
print(part_one(puzzle_input))

# part two solution
print(part_two(puzzle_input))
