def rock_paper_scissors(n):
    combinations = []
    plays = ['rock', 'paper', 'scissors']

    def generate_combo(turn, combo=[]):
        if turn == 0:
            combinations.append(combo)
            return

        for play in plays:
            generate_combo(turn - 1, combo + [play])

    generate_combo(n)

    return combinations
