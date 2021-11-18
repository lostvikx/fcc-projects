import random
import copy

class Hat:

  # *args & **kwargs
  def __init__(self, **ball_color):
    
    self.contents = []

    for color in ball_color:
      # Calc frequency
      freq = ball_color[color]

      for i in range(0, freq):
        self.contents.append(color)

    # This is cheating, lol!
    self.cp_contents = copy.deepcopy(self.contents)

  def draw(self, n_ball_drawn):

    rm_ball = []

    if n_ball_drawn >= len(self.contents):
      # Make a copy using blank slice
      rm_ball = self.contents[:]
      self.contents.clear()
    else:

      for i in range(0, n_ball_drawn):
        # Random ball index
        ball_index = random.randint(0, len(self.contents) - 1)
        # Using .pop() to remove & return the val
        rm_ball.append(self.contents.pop(ball_index))

    # This worked though!
    # try:
    #   return rm_ball
    # finally:
    #   for i in range(len(rm_ball)):
    #     self.contents.append(rm_ball[i])

    return rm_ball


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  success = 0
  # Because num_experiments change
  n_ex = num_experiments

  while num_experiments > 0:

    balls = dict()
    # Random draw
    drawn_balls = hat.draw(num_balls_drawn)

    # Frequency dict
    for ball in drawn_balls:
      balls[ball] = balls.get(ball, 0) + 1

    # Needs to pass len(expected_balls) tests or all test criteria
    pass_test = 0

    # Iterate over the expected
    for color, n_balls in expected_balls.items():

      # Iterate over random drawn balls
      for c, b in balls.items():
        # Check color
        if color == c:
          # There should be atleast b or expected amount of balls in the drawn balls
          if b >= n_balls:
            pass_test += 1
            # Not sure if it makes the algo any faster!
            # break

    if pass_test == len(expected_balls.items()):
      success += 1
      # Cool debugging!
      # print("Pass:", end=" ")

    # Useful for debugging
    # print(balls)

    # Neat trick
    hat.contents = copy.deepcopy(hat.cp_contents)

    num_experiments -= 1

  return success / n_ex


hat = Hat(blue=3, red=2, green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=10)

print(probability)
