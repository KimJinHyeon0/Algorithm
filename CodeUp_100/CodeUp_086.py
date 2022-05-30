w, h, b = map(int, input().split())
size = w*h*b/8/1024/1024
print("%.2f MB" %size)
