def print_list_integer1(my_list=[]):
    print("{}".format(my_list[0]))
    print("{}".format(my_list[1]))
    print("{}".format(my_list[2]))
    print("{}".format(my_list[3]))
    print("{}".format(my_list[4]))
# line 8 too long
    print("{}\n{}\n{}\n{}\n{}".format(my_list[0], my_list[1], my_list[2], my_list[3], my_list[4]))
# no new line
    print(my_list[0], my_list[1], my_list[2], my_list[3], my_list[4])

    for item in my_list:
        print(item)
