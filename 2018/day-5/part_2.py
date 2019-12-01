import sys

poly_string = input()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_length(poly_string_in):
    done = False
    while done is False:
        is_finished = True
        for index in range(len(poly_string_in) - 1):
            first = poly_string_in[index]
            second = poly_string_in[index + 1]
            if (first.lower() == second and first == second.upper()) or (first.upper() == second and first == second.lower()):
                poly_string_in = poly_string_in[:index] + poly_string_in[index + 2:]
                is_finished = False
                break
        done = is_finished
    return len(poly_string_in)

longest = 1000000000
for character in alphabet:
    print(character)
    poly_string_in = poly_string.replace(character, '')
    poly_string_in = poly_string_in.replace(character.upper(), '')
    poly_string_in_len = get_length(poly_string_in)
    if poly_string_in_len < longest:
        longest = poly_string_in_len

print(longest)