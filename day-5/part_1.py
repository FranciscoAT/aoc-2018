import sys

poly_string = input()

done = False
while done is False:
    is_finished = True
    for index in range(len(poly_string) - 1):
        first = poly_string[index]
        second = poly_string[index + 1]
        if (first.lower() == second and first == second.upper()) or (first.upper() == second and first == second.lower()):
            poly_string = poly_string[:index] + poly_string[index + 2:]
            is_finished = False
            break
    done = is_finished

print(poly_string)
print(len(poly_string))