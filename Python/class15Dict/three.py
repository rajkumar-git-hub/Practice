student = {
    "id": 101,
    "name": "Raj Kumar",
    "age": 21,
    "course": "Python Full Stack",
    "email": "raj@example.com",
    "city": "Chennai"
}

print(student.values())
print(student.keys())
print(student.items())

#OR 

# We can use for loop to print these in seperate lines

for key in student.keys():
    print(key)

print("\n")

for value in student.values():
    print(value)

print("\n")

for item in student.items():
    print(item)


print("\n")

for k,v in student.items():
    print(f"{k} : {v}")