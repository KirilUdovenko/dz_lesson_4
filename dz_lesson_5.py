# my_number = 1340501026051
# new_number = str(my_number)
# my_symbol = "0"
# result = new_number.count(my_symbol)
# print(result)

#############################

# number = 5102801160000
# new_number = len(str(number)) - len(str(number).strip('0'))
# print(new_number)

##########################

# text = "19 меньше чем 27 но больше чем 7"
# new_text = text.split()
# sum_num = 0
# for symbol in new_text:
#     if symbol.isdigit():
#         sum_num += int(symbol)
#         print(symbol)
# print("sum=", sum_num)

##########################

# my_str = "Kate likes cats or dogs?"
# l_limit = "e"
# r_limit = "o"
# res_str = my_str[my_str.find(l_limit) + 1: my_str.rfind(r_limit)]
# print(res_str)

##################

# my_list = ["Apple", "auto", "Book", "Abricos", "Basketball"]
# new_list = []
# for words in my_list:
#     if words.upper().startswith("A"):
#         new_list.append(words)
# print(new_list)

##################

# my_list = ["apple", "auto", "book", "abricos", "basket"]
# new_list = []
# for words in my_list:
#     if "a" in words:
#         new_list.append(words)
# print(new_list)

##########################

# my_list = [1, 2, 3, "11", "22", 33]
# new_list = []
# for text in my_list:
#     if type(text) == str:
#         new_list.append(text)
# print(new_list)

#########################

# my_str = "ssssadfgfwasd32ynlop"
# new_str = []
# for symbol in set(my_str):
#     if my_str.count(symbol) == 1:
#         new_str.append(symbol)
# print(new_str)

####################

# my_str_1 = "asdwqfasdtht"
# my_str_2 = "obngiadwtnvr"
# res_list = list(set(my_str_1).intersection(set(my_str_2)))
# print(res_list)

########################

# my_str_1 = "aaaasdf1"
# my_str_2 = "asdfff2"
# new_str = []
# for symbol in set(my_str_1).intersection(set(my_str_2)):
#     if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
#         new_str.append(symbol)
# print(new_str)

##################

# my_str = "asdwqfesasdqwtgf"
# if len(my_str) % 2:
#     my_str += "_"
# res_list = []
# for index in range(0, len(my_str), 2):
#     res_list.append(my_str[index: index + 2])
# print(res_list)
