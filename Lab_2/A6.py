N = int(input("Enter the number of seconds: "))
h = N // 3600
m = (N-(h * 3600))//60
s = (N-(h * 3600)) % 60
print("{}:{:02}:{:02}".format(h, m, s))

