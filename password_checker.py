import re


pattern = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
password = 'Derge4##'

check = pattern.fullmatch(password)
print(check)
