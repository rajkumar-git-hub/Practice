
fp=open('abc.txt')
print(fp.__dict__)

data=fp.readlines()
print(data)

data=fp.readlines(3)
print(data)