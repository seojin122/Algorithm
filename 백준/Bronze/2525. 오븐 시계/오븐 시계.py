hour, minutes = map(int, input().split())
time = int(input())


hour += (time // 60)
minutes += (time % 60 )

if(minutes >= 60):
    hour += 1
    minutes -= 60

if(hour >= 24):
    hour -= 24

print(hour, minutes)