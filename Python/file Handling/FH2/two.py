fp=open('abc.txt','a')

print(fp.name)
print(fp.mode)
print(fp.writable())
print(fp.readable())
print("Is the file CLosed -",fp.closed)
fp.close()
print("Is the file CLosed -",fp.closed)