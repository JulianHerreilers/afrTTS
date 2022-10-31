phones_file_name = "phones.txt"
phones_file = open(phones_file_name, 'r')
lines_phones = phones_file.read()
phones_file.close()
a = lines_phones.split()
print(a)