def descending_order(num):
    numstr = str(num)

    sortdigits = sorted(numstr, reverse=True)

    result = int(''.join(sortdigits))

    return result
# or you can do it as
#def descending_order(num):
#   return int(''.join(sorted(str(num), reverse=True)))