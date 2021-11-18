# IP Validation
# https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python

# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
# IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

# Notes:
# Leading zeros (e.g. 01.02.03.04) are considered INVALID
# Inputs are guaranteed to be a single string


# Sample input:
# '123.045.067.089'

# Sample output
# False


def is_valid_IP(strng):
    splited = strng.split(".")
    if len(splited) != 4:
        return False
    else:
        passed = 0
        for i in splited:
            if str(i[0]) == "0" and len(str(i)) > 1 or i.isdigit() is False or int(i) not in range(0, 256):
                return False
            else:
                passed += 1
        if passed == 4:
            return True


print(is_valid_IP('123.045.067.089'))
