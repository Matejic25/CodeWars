# Bouncing Balls
# https://www.codewars.com/kata/5544c7a5cb454edb3c000047/solutions/python

# A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.
# He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).
# His mother looks out of a window 1.5 meters from the ground.
# How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

# Three conditions must be met for a valid experiment:
# Float parameter "h" in meters must be greater than 0
# Float parameter "bounce" must be greater than 0 and less than 1
# Float parameter "window" must be less than h.
# If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

# Notes:
# The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.


# Sample input:
# (3, 0.66, 1.5)

# Sample output
# 3


def bouncing_ball(h, bounce, window):
    if 0 < window < h and 0 < bounce < 1:
        view_count = 0
        while h > window:
            h = h * bounce
            view_count += 1
            if h > window:
                view_count += 1
            else:
                pass
        return view_count
    else:
        return -1


print(bouncing_ball(3, 0.66, 1.5))
