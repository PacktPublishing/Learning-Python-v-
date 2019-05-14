#file_object = open(file_name ,access_mode)

file_input = open("sample1.txt",'r')
all_read = file_input.read()
print all_read
file_input.close()