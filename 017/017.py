# A dictionary containing special cases of numbers written out as english
# words. Contains 1 through 20, along with {30, 40, 50, 60, 70, 80, 90}. Using
# these words we can rebuild any other word up to 999. Note we'll need to add
# the word 'hundred' or 'hundredand'. See below.
special_case_dict = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six",
        7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve",
        13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen",
        17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thirty",
        40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty",
        90:"ninety"}

def int2text(integer):
    """Takes an integer below 1001 and converts it into english text. Ignore
    spaces and hyphens as the instructions require."""
    # Numbers 1-99 are handled by simply looking up words in the special_case
    # dictionary.
    if integer < 100:
        return digit2text(integer)

    elif integer < 1000:
        # If exactly some hundred, then just return the word for the hundred's
        # place and the word 'hundred'
        if integer%100 == 0:
            return digit2text(integer/100)+'hundred'
        # Otherwise return the word for the hundred's place, the word
        # 'hundredand' and do some composition to make the rest of the words.
        else:
            return digit2text(integer/100)+'hundredand'+\
                    digit2text(integer%100)
    # Special case for 1000.
    elif integer == 1000:
        return "onethousand"

def digit2text(integer):
    """Takes integer digits/double digits and returns the english text for
    these numbers."""
    # If the integer is in the special cases dictionary, then look up the word,
    # return it, and we're done.
    if integer in special_case_dict.keys():
        return special_case_dict[integer]
    # Otherwise compose the word, by taking the number in the ten's place and
    # multiplying by 10 (i.e. integer/10*10 evaluates to a number in the set
    # {10, 20, 30, 40, 50, 60, 70, 80, 90} for any input integer between 10-99.
    # Then add word for the number in the one's place
    else:
        return special_case_dict[integer/10*10]+special_case_dict[integer%10]

if __name__ == "__main__":
    text = ""
    for i in range(1,1001):
#        print int2text(i)
        text += int2text(i)
    print len(text)
