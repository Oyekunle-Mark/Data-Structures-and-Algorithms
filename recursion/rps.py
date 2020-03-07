from typing import Optional, List, Any


def rock_paper_scissors(n: int) -> List[Any]:
    combinations = []
    plays = ['rock', 'paper', 'scissors']

    def generate_combo(turn: int, combo: Optional[List[Any]] = []) -> None:
        if turn == 0:
            combinations.append(combo)
            return

        for play in plays:
            generate_combo(turn - 1, combo + [play])

    generate_combo(n)

    return combinations
