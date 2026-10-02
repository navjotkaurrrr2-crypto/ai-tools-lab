Python Error Cheat-Sheet

1. IndexError

Cause:
Occurs when we try to access an index that does not exist in a list, tuple, or string.

Fix:
Make sure the index is within the valid range.

Example:

numbers = [10, 20, 30]

# Wrong
print(numbers[5])

# Fixed
print(numbers[2])

---

2. KeyError

Cause:
Occurs when we try to access a dictionary key that does not exist.

Fix:
Use an existing key or check whether the key exists before accessing it.

Example:

student = {
    "name": "Navjot",
    "age": 20
}

# Wrong
print(student["marks"])

# Fixed
print(student["age"])

---

3. TypeError

Cause:
Occurs when an operation is performed on incompatible data types.

Fix:
Use compatible data types or convert the value to the required type.

Example:

age = 20

# Wrong
print(age + " years")

# Fixed
print(str(age) + " years")

---

4. RecursionError

Cause:
Occurs when a function keeps calling itself without reaching a stopping condition.

Fix:
Add a proper base condition to stop the recursive function.

Example:

# Wrong
def count():
    count()

# Fixed
def count(n):
    if n == 0:
        return
    print(n)
    count(n - 1)

count(3)

---

5. AttributeError

Cause:
Occurs when we try to use an attribute or method that the object does not have.

Fix:
Use a method or attribute that belongs to that object's data type.

Example:

name = "Navjot"

# Wrong
print(name.append(" Kaur"))

# Fixed
print(name + " Kaur")

---

Summary

Error| Cause| Fix
IndexError| Invalid index| Use a valid index
KeyError| Missing dictionary key| Use an existing key
TypeError| Incompatible data types| Use compatible types or convert
RecursionError| Recursion has no proper stopping condition| Add a base condition
AttributeError| Object does not have the requested method/attribute| Use a valid method/attribute