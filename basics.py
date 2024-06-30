#Type "python" in the terminal to check version, "python3 --verionn in linux"
#Tools-Build or ctrl+b to run code

print("hello world!")

name = "dawid tkaczyk"
print(name.title())
print(name.upper())
print(name.lower())

#f-strings
first_name = "tom"
last_name = "hardy"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")

#Another way to print a string and a variable
print("Hello!!", full_name.title())

# \t - tab \n - new line
print("Languages:\tPython, Javascript, C\nAnd more!")

#Eliminate whitespace with .rstrip() and .lstrip() or all with .strip()

# Use CTRL + / on a Windows machine to quickly comment out highlighted code