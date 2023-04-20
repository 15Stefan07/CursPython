"""
r -> citim, nu adaugam, daca fisierul nu exista apare eroare
w -> scriem, daca fisierul nu exista, il adauga, daca exista ceva scris in fisier, il rescrie
a -> append, daca exista ceva scris in fisier, adauga la final, nu apare eroare daca fisierul nu exista
r+ -> scriere + citire
"""
# file = open('data2.txt', "r+")
# file.write("Hello2")
# file.close()

# file = open('data1.txt', 'r+')
# try:
#     file.write("Hello")
# finally:
#     file.close()

with open('data.txt', 'w') as file:
      file.writelines(['hello','hello1','hello2'])
    # file.write("Hello\n")
    # file.write("Hello1\n")
    # file.write("Hello2\n")

# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line)

# with open('data.txt', 'r') as file:
#     print(list(file))
#      for line in list(file):
#          print(line)

with open('data.txt','r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line)