def obsah_kruhu(prumer):
    return 3.14 * prumer / 2 ** 2

#obsah_kruhu(5)

words = open("C:\Programování\python-academy\čtvrtá lekce\words.txt", "r")

word_list = words.readlines()
clean_list= []
for i in word_list:
    clean_list.append(i.rstrip("\n"))
print(clean_list)
words.close()

with open("C:\Programování\python-academy\čtvrtá lekce\words.txt", "r") as file:
    word_list = file.readlines()
    clean_list = []
for i in word_list:
    clean_list.append(i.rstrip("\n"))
print(clean_list)