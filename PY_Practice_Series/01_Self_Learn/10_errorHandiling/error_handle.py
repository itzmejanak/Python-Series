file = open("PY_Practice_Series/10_errorHandiling/youtube.txt", 'w')

try:
    file.write("janak with python")
finally:
    file.close()

with open("PY_Practice_Series/10_errorHandiling/youtube.txt", 'w') as file:
    file.write("janak with python")