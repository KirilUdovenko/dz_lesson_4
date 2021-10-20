# my_number = 1340501026051
# new_number = str(my_number)
# my_symbol = "0"
# result = new_number.count(my_symbol)
# print(result)

#############################

# number = 5102801160000
# new_number = str(number)
# my_symbol = "0"
# print(len(new_number) - len(new_number.rstrip(my_symbol)))

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
# ??????????? 4
# my_str = "Kate likes cats or dogs?"
# l_limit = "e"
# r_limit = "o"


##################

# my_list = ["Apple", "auto", "Street", "Book", "Abricos", "Basketball"]
# my_list_1 = []
# for words in my_list:
#     if words.upper().startswith("A"):
#         my_list_1.append(words)
# print(my_list_1)

##################

my_list = ["Apple", "auto", "Street", "Book", "Abricos", "Basketball"]
my_list_1 = []
for words in my_list:
    if words.upper():
            my_list_1.append(words)
print(my_list_1)
