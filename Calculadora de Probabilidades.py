import random
import copy

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents.clear()
            return drawn_balls
        return [self.contents.pop(random.randint(0, len(self.contents) - 1)) for _ in range(num_balls)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        
        drawn_counts = {color: balls_drawn.count(color) for color in expected_balls}
        
        if all(drawn_counts.get(color, 0) >= count for color, count in expected_balls.items()):
            success_count += 1

    return success_count / num_experiments

# Ejemplo de uso

hat = Hat(blue=5, red=4, green=2)
probability = experiment(
    hat=hat,
    expected_balls={'red': 1, 'green': 2},
    num_balls_drawn=4,
    num_experiments=2000
)
print(f"Probability: {probability}")