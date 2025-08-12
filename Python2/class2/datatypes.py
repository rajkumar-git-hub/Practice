#

# 1. int (integer)
my_int = 10
print(my_int, type(my_int))  # Output: 10 <class 'int'>

# 2. float
my_float = 10.5
print(my_float, type(my_float))  # Output: 10.5 <class 'float'>

# 3. str (string)
my_str = "Hello"
print(my_str, type(my_str))  # Output: Hello <class 'str'>

# 4. complex
my_complex = 3 + 4j
print(my_complex, type(my_complex))  # Output: (3+4j) <class 'complex'>

# 5. bool (boolean)
my_bool = True
print(my_bool, type(my_bool))  # Output: True <class 'bool'>

# 6. list
my_list = [1, 2, 3, 1, 3]
print(my_list, type(my_list))  # Output: [1, 2, 3, 1, 3] <class 'list'>

# 7. tuple
my_tuple = (1, 2, 3, 1, 4, 2)
print(my_tuple, type(my_tuple))  # Output: (1, 2, 3, 1, 4, 2) <class 'tuple'>

# 8. set
my_set = {1, 2, 3, 1 , 2 , 3}
print(my_set, type(my_set))  # Output: {1, 2, 3} <class 'set'>

# 9. dict (dictionary)
my_dict = {"name": "Raj", "age": 25}
print(my_dict, type(my_dict))  # Output: {'name': 'Raj', 'age': 25} <class 'dict'>

# 10. bytes (immutable sequence of bytes)
my_bytes = b"hello"
print(my_bytes, type(my_bytes))  # Output: b'hello' <class 'bytes'>

# 11. bytearray (mutable sequence of bytes)
my_bytearray = bytearray(5)  # creates 5 zero bytes
print(my_bytearray, type(my_bytearray))  # Output: bytearray(b'\x00\x00\x00\x00\x00')

# 12. frozenset (immutable set)
my_frozenset = frozenset([1, 2, 3])
print(my_frozenset, type(my_frozenset))  # Output: frozenset({1, 2, 3}) <class 'frozenset'>

# 13. range (sequence of numbers)
my_range = range(5)
print(list(my_range), type(my_range))  # Output: [0, 1, 2, 3, 4] <class 'range'>

# 14. NoneType
my_none = None
print(my_none, type(my_none))  # Output: None <class 'NoneType'>

# 15. function
def my_function():
    return "Hello from function"

print(my_function, type(my_function))  # Output: <function my_function at ...> <class 'function'>
print(my_function())  # Output: Hello from function
