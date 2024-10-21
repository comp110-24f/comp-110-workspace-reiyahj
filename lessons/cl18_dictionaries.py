"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
    # this comma after last entry isn't required, but
    # convenient if want to add another entry later on
}


# len evaluates to number of key-value entries
print(len(ice_cream))

# add key-value entries using subscription notation
ice_cream["mint"] = 10

# access values by their key using subscription notation
mint_orders: int = ice_cream["mint"]
print(mint_orders)

# re-assign values by their key using assignment operators
ice_cream["mint"] = ice_cream["mint"] + 1
ice_cream["mint"] += 1

# remove items by key using the pop method
print(
    ice_cream.pop("strawberry")
)  # pretty infrequent use of pop.'s return value, but still useful to know

# test if a key is in the dictionary:
print("strawberry" in ice_cream)
print("vanilla" in ice_cream)  # very fast test to see if key exists in dictionary

# loop through itesm using for-in loops
# total: int = 0
# the variable (e.g. flavor) iterates over
# each key one-by-one in the dictionary.

for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor}: {tally}")
