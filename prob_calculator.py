import copy
import random
# Consider using the modules imported above.


class Hat:
    """Create a hat with different coloured balls of various amounts."""

    def __init__(self, **kwargs):
        contents = []
        for key, val in kwargs.items():
            for i in range(val):
                contents.append(key)
        self.contents = contents

    def draw(self, num):
        """Draws a user specified number of balls from the hat at random."""

        contents = self.contents
        if num > len(contents):
            return contents

        drawn = []
        for i in range(num):
            ballIndex = random.randrange(len(contents))
            drawn.append(contents[ballIndex])
            contents.pop(ballIndex)

        self.contents = contents
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Execute a number of specified experiments on a pre determined hat and calculate the probability of getting the user specified balls."""

    m = 0
    for i in range(num_experiments):
        hatCopy = copy.deepcopy(hat)
        expCopy = copy.deepcopy(expected_balls)
        drawn_balls = hatCopy.draw(num_balls_drawn)
        for ball in drawn_balls:
            if ball in expCopy:
                expCopy[ball] -= 1

        if all(x <= 0 for x in expCopy.values()):
            m += 1
    return m/num_experiments
