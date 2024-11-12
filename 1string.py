str = "   Hello, Python World!   "


lowercase_string = str.lower()
print("2. lower(): '{}'".format(lowercase_string))

uppercase_string = str.upper()
print("3. upper(): '{}'".format(uppercase_string))

title_string = str.title()
print("4. title(): '{}'".format(title_string))

replaced_string = str.replace("Python", "Java")
print("5. replace(): '{}'".format(replaced_string))

find_index = str.find("Python")
print("6. find(): Index of 'Python' is {}".format(find_index))

split_string = str.split()
print("7. split(): {}".format(split_string))

join_string = "-".join(split_string)
print("8. join(): '{}'".format(join_string))

alpha_check = "Hello".isalpha()
print("9. isalpha(): Is 'Hello' alphabetic? {}".format(alpha_check))

numeric_check = "12345".isnumeric()
print("10. isnumeric(): Is '12345' numeric? {}".format(numeric_check))

startswith_check = str.startswith("   Hello")
print("11. startswith(): Does the string start with '   Hello'? {}".format(startswith_check))

endswith_check = str.endswith("World!   ")
print("12. endswith(): Does the string end with 'World!   '? {}".format(endswith_check))

count_occurrences = str.count("o")
print("13. count(): Number of occurrences of 'o' is {}".format(count_occurrences))

digit_check = "12345".isdigit()
print("14. isdigit(): Is '12345' a digit? {}".format(digit_check))

swapcase_string = str.swapcase()
print("15. swapcase(): '{}'".format(swapcase_string))

zfilled_string = "42".zfill(5)
print("16. zfill(): '{}'".format(zfilled_string))

formatted_string = "Hello, {}!".format("Alice")
print("17. format(): '{}'".format(formatted_string))

space_check = "   ".isspace()
print("18. isspace(): Is '   ' whitespace only? {}".format(space_check))


string = input("Enter a string")
alpha=digit=special=word=0
for ch in string:
    if ch.isalpha():
        alpha+=1
    elif ch.isdigit():
        digit+=1
    elif not ch.isalnum():
        special+=1
    else:
        word+=1
print("Number of alphabets:",alpha)
print("Number of digits:",digit)
print("Number of special characters:",special)
print("Number of words:",word)
print("Number of strings:",string)

# =================================================================

