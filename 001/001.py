import numpy as np

def sum_of_multiples(multiples, max_value):
    """Takes a length 2 list of multiples to check, and an integer maximum
    value to check."""
    # To elegantly solve this problem we are going to find the sum of all the
    # numbers that are divisible by the first number in the list "multiple",
    # and then the second number in the list "multiple". In the process we have
    # over counted by all the numbers that are divisible by the two "multiple"
    # numbers multiplied together. So we subtract out the sum of all the
    # numbers that are divisible by the two "multiple" numbers multiplied
    # together.
    #
    # Explicitly for this problem, we find the sum of numbers divisible by 3,
    # add that to the sum of numbers divisible by 5, and subtract the sum of
    # numbers divisible by 15.
    if len(multiples) != 2:
        print "Expected only two multiples to check."
        print "Out of scope, I'll need additional funds for a scope change."
        return None
    multiples.append(multiples[0]*multiples[1])
    # Make a numpy array for easier math.
    multiples = np.array(multiples)

    # The sum of numbers divisible by a number can be calculated by taking the
    # number itself and adding it to the largest number less than max_value
    # that it is divisible by, and then multiplying it by the half the number
    # of numbers that it is divisible by within the range.
    #
    # Explicitly for this problem for the number 5, there are 999/5 = 199
    # numbers that are divisible by 5 between 1 to 999. The first number is 5
    # and the last number is 999-999%5 = 995. The sum of the first and last
    # number is 1000. The sum of the second number and the second to last
    # number also add to 1000, and so on. Of the 199 numbers that are divisible
    # by 5, there are 199/2.0 of these pairs, and the sum of all these is
    # 1000(199/2.0). NOTE: we divide by a float in case the number of numbers
    # divisible by a number is odd.

    sub_totals = (multiples+max_value-max_value%multiples)*\
            (max_value/multiples)/2.0

    # Sum the first two numbers and subtract the last number to get the total.
    return sum(sub_totals[0:2]) - sub_totals[2]

if __name__ == "__main__":
    print sum_of_multiples(multiples=[3,5], max_value=999)
