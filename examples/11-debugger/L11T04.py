points = []
for i in range(0,5):
    tuomarit = int(input("Give points: "))
    points.append(tuomarit)

points.remove(max(points))
points.remove(min(points))

print("==>> Total points are", sum(points))