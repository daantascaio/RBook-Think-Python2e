fruit = 'banana'

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

print()


def aws(str):

    str_n = len(str)
    while str_n != 0:
        print(str[str_n - 1])
        str_n -= 1


aws('banana')

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    print(letter + suffix)


word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
