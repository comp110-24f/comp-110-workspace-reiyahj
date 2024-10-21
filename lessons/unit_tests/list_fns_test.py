from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first

# unit test benefit: can make changes to fn & retest just by pressing this play button
# (don't have to rewrite tests every time you change code)
# this is how COMP110 autograder is made!


def test_get_first() -> None:
    """Tests get_first function."""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert get_first(fruits) == "apples"


def test_remove_first_ret_value() -> None:
    """Tests that remove_first function returns None."""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert remove_first(fruits) is None


def test_remove_first_behavior() -> None:
    """Tests that remove_first removes first element."""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    remove_first(fruits)
    assert get_and_remove_first(fruits) == ["oranges", "bananas"]


def test_get_first_edge_case() -> None:
    """Tests that get_first works with empty list."""
    input: list[str] = []
    assert get_first(input) == ""
