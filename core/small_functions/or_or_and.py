
# or_function = 'or'
# and_function = 'and'
#
# or_or_and = {
#     or_function : lambda a, b: a or b,
#     and_function: lambda a, b: a and b,
# }


class OrOrAnd(object):
    or_function = (lambda a, b: a or b)
    and_function = (lambda a, b: a and b)


# or_function =(lambda a, b: a or b)
# and_function= (lambda a, b: a and b)
# print(or_function('d', 9))
