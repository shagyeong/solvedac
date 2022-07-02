char = list(input())

thenofspace = (char.count(" ")) + 1

if   char[0] == " " and char[len(char) -1] == " ":
    print(thenofspace - 2)
elif (
char[0] == " " and char[len(char) -1] != " " or
char[0] != " " and char[len(char) -1] == " "):
    print(thenofspace - 1)
else:
    print(thenofspace)
