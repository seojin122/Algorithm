
dotx1, doty1 = map(int, input().split(" "))
dotx2, doty2 = map(int, input().split(" "))
dotx3, doty3 = map(int, input().split(" "))



if (dotx1 == dotx2):
    x = dotx3
elif (dotx2 == dotx3):
    x = dotx1
elif (dotx1 == dotx3):
    x = dotx2


if (doty1 == doty2):
    y = doty3
elif (doty2 == doty3):
    y = doty1
elif (doty1 == doty3):
    y = doty2

print(x, y)