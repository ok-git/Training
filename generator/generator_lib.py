import random
import string


def var_or_fixed(maxlen, fixedlen):
    if fixedlen:
        return maxlen
    else:
        return random.randrange(maxlen)


def random_string(prefix, maxlen, fixedlen=False, punctuation=False, spaces=True):
    symbols = string.ascii_letters + string.digits
    if punctuation:
        symbols = symbols + string.punctuation
    if spaces:
        symbols = symbols + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(var_or_fixed(maxlen, fixedlen))])


def random_day_of_month():
    return str(random.choice(range(1, 31)))


def random_month():
    months = ("January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December")
    return random.choice(months)


def random_year():
    return str(random.choice(range(1899, 2018)))
