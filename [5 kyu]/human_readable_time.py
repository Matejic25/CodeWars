# Human Readable Time
# https://www.codewars.com/kata/52685f7382004e774f0001f7/python

# Write a function, which takes a non-negative integer (seconds) as input
# and returns the time in a human-readable format (HH:MM:SS)
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)


# Sample input:
# 273

# Sample output:
# '00:04:33'


def make_readable(seconds):
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    digits = [f"0{i}" if int(i) < 10 else f"{i}" for i in [hours, minutes, seconds]]
    return "".join(digits[i] + ":" if i != len(digits) - 1 else digits[i] for i in range(len(digits)))


print(make_readable(273))
