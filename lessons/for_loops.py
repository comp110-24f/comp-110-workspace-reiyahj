"""For loops practice; Class on October 7th, 2024."""

pets: list[str] = ["Louie", "Bo", "Bear"]
# Tell every pet they're a good boy!
for elem in pets:
    print(f"Good boy, {elem}!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]
# Prints every element's index and value!
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
