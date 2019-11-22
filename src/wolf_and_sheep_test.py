from hypothesis.stateful import RuleBasedStateMachine, rule, invariant, precondition
from hypothesis import note
from hypothesis.strategies import sampled_from


stuff_to_move = ["wolf", "sheep", "grass"]


class WolfAndSheep(RuleBasedStateMachine):
    def __init__(self):
        super(WolfAndSheep, self).__init__()
        self.left_side = set(["wolf", "sheep", "grass", "you"])
        self.right_side = set()

    def on_side(self, side, *args):
        return all(a in side for a in args)

    def you_are_left(self):
        return "you" in self.left_side

    def you_are_right(self):
        return "you" in self.right_side

    def invalid_side(self, s):
        sheep_dies = self.on_side(s, "wolf", "sheep") and not self.on_side(s, "you")
        eats_grass = self.on_side(s, "grass", "sheep") and not self.on_side(s, "you")
        return sheep_dies or eats_grass

    @precondition(lambda self: self.you_are_left())
    @rule(a=sampled_from(stuff_to_move))
    def move_right(self, a):
        to_move = set([a] + ["you"]) if a in self.left_side else set(["you"])
        new_left = self.left_side - to_move
        new_right = self.right_side.union(to_move)
        if self.invalid_side(new_left):
            note(f"move would result in invalid left side {self.left_side}")
            return

        if self.invalid_side(new_right):
            note(f"move would result in invalid right side {self.right_side}")
            return

        note(f"{self.left_side} => {to_move} => {self.right_side}")
        self.right_side = new_right
        self.left_side = new_left

    @precondition(lambda self: self.you_are_right())
    @rule(a=sampled_from(stuff_to_move))
    def move_left(self, a):
        to_move = set([a] + ["you"]) if a in self.right_side else set(["you"])
        new_right = self.right_side - to_move
        new_left = self.left_side.union(to_move)
        if self.invalid_side(new_left):
            note(f"move would result in invalid left side {self.left_side}")
            return

        if self.invalid_side(new_right):
            note(f"move would result in invalid right side {self.right_side}")
            return

        note(f"{self.left_side} <= {to_move} <= {self.right_side}")
        self.right_side = new_right
        self.left_side = new_left

    @invariant()
    def problem_solved(self):
        left_side_empty = self.left_side == set()
        all_on_right_side = self.right_side == set(["you", "wolf", "sheep", "grass"])
        solved = left_side_empty and all_on_right_side
        assert not solved


WolfAndSheepTest = WolfAndSheep.TestCase
