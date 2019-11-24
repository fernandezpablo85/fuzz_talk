from hypothesis.stateful import RuleBasedStateMachine, rule, invariant, precondition
from hypothesis import note
from hypothesis.strategies import sampled_from


stuff_to_move = sampled_from(["wolf", "sheep", "grass"])


def all_in(set, *elements):
    return all(e in set for e in elements)


def all_alone_in(set, *elements):
    return all_in(set, *elements) and "you" not in set


def invalid_side(s):
    sheep_dies = all_alone_in(s, "wolf", "sheep")
    eats_grass = all_alone_in(s, "grass", "sheep")
    return sheep_dies or eats_grass

def stage_move(origin, destination, to_move):
    new_origin = origin - to_move
    new_destination = destination.union(to_move)
    invalid = invalid_side(new_origin) or invalid_side(new_destination)
    return new_origin, new_destination, invalid


class WolfAndSheep(RuleBasedStateMachine):
    def __init__(self):
        super(WolfAndSheep, self).__init__()
        self.left_side = set(["wolf", "sheep", "grass", "you"])
        self.right_side = set()

    @precondition(lambda self: "you" in self.left_side)
    @rule(item=stuff_to_move)
    def move_right(self, item):
        to_move = [item] if item in self.left_side else []
        to_move = set(to_move + ["you"])
        new_left, new_right, invalid_move = stage_move(self.left_side, self.right_side, to_move)
        if invalid_move:
            note("move would result in invalid side")
        else:
            note(f"{new_left} => {to_move} => {self.right_side}")
            self.right_side = new_right
            self.left_side = new_left

    @precondition(lambda self: "you" in self.right_side)
    @rule(item=stuff_to_move)
    def move_left(self, item):
        to_move = [item] if item in self.right_side else []
        to_move = set(to_move + ["you"])
        new_right, new_left, invalid_move = stage_move(self.right_side, self.left_side, to_move)
        if invalid_move:
            note("move would result in invalid side")
        else:
            note(f"{self.left_side} <= {to_move} <= {new_right}")
            self.right_side = new_right
            self.left_side = new_left

    @invariant()
    def problem_solved(self):
        left_side_empty = self.left_side == set()
        all_on_right_side = self.right_side == set(["you", "wolf", "sheep", "grass"])
        solved = left_side_empty and all_on_right_side
        assert not solved


# ignored. uncomment to run
# WolfAndSheepTest = WolfAndSheep.TestCase
