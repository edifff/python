def construct_palindrome(string):

    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    first_half = ""
    second_half = ""
    middle_char = ""
    for char, count in char_count.items():
        if count % 2 == 0:
            first_half += char * (count // 2)
            second_half = (char * (count // 2)) + second_half
        else:
            middle_char = char
            first_half += char * (count // 2)
            second_half = (char * (count // 2)) + second_half

    palindrome = first_half + middle_char + second_half
    return palindrome

n=int(input())
string = input()

# Получаем палиндром
palindrome = construct_palindrome(string)
print(palindrome)