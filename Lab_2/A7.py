x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

color1 = 'White' if (x1 + y1) % 2 == 0 else 'Black'

color2 = 'White' if (x2 + y2) % 2 == 0 else 'Black'

if color1 == color2:
    print("YES")
    print(color1)
else:
    print("NO")
