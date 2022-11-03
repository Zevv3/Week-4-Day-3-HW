# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.
# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python/636087a37dadeacedfcb3462

def accum_Original(s):
    # your code
    amount = 0
    result_list = []
    for letter in s:
        amount += 1
        for i in range(amount):
            if i == 0:
                letter = letter.upper()
                result_list.append(letter)
            elif i != 0:
                letter = letter.lower()
                result_list.append(letter)
        result_list.append('-')
    result_list.pop()
    result = str("".join(result_list))
    return result
print(accum_Original("HbideVbxncC"))
def accum_Updated(s):
    result = ""
    for count, letter in enumerate(s):
        result += letter.upper() + letter.lower() * count + "-"
    return result[:len(result) - 1]
print(accum_Updated("HbideVbxncC"))

def accum_Listcomp(s):
    return '-'.join(letter.title() * count for count, letter in enumerate(s, 1))
print(accum_Listcomp(("HbideVbxncC")))