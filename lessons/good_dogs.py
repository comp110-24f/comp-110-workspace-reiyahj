"""In-Class, November 20, 2024. Recursion practice over a list."""


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    """Recursive function to see if all dogs were good in puppy school."""
    # Handle base case #1 where a dog is found whose score is NOT at threshold (false)
    # Handle base case where final dog is found to be above threshold (true)
    # Handle recursive case where we check the next index in the list recursively
    num_dogs: int = len(scores)
    if num_dogs <= idx:
        raise IndexError("idx too high")
    elif int(scores[idx]["score"]) < thresh:
        return False
    else:
        if num_dogs == idx + 1:
            return True
        else:
            print(f"Good dog, {scores[idx]["name"]}")
            return all_good(scores, thresh, idx + 1)


pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "10"},
    {"name": "Ada", "score": "9"},
    {"name": "Pip", "score": "7"},
]


print(all_good(scores=pack, thresh=8, idx=0))
