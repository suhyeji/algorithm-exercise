def hanoiTower(n, source, dest, temp):
    if n == 1:
        print("%d -> %d" % (source, dest))
    else:
        hanoiTower(n - 1, source, temp, dest)
        print("%d -> %d" % (source, dest))
        hanoiTower(n - 1, temp, dest, source)

n = int(input())
hanoiTower(n, 0, 2, 1)