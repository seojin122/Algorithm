N = int(input())
x0, y0 = map(int, input().split())
minx = maxx = x0
miny = maxy = y0
    
for _ in range(N-1):
    x, y = map(int, input().split())
    if(x>= maxx):
        maxx = x
    if(x<minx):
        minx = x

    if(y>= maxy):
        maxy = y
    if(y<miny):
        miny = y

print((maxx-minx) * (maxy-miny))