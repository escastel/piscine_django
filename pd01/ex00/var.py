def my_var():
    var_int = 42
    print(var_int, "has a type", type(var_int))
    var_str_num = "42"
    print(var_str_num, "has a type", type(var_str_num))
    var_str_txt = "quarante-deux"
    print(var_str_txt, "has a type", type(var_str_txt))
    var_float = 42.0
    print(var_float, "has a type", type(var_float))
    var_bool = True
    print(var_bool, "has a type", type(var_bool))
    var_list = [42]
    print(var_list, "has a type", type(var_list))
    var_dict = {42: 42}
    print(var_dict, "has a type", type(var_dict))
    var_tup = (42,)
    print(var_tup, "has a type", type(var_tup))
    var_set = set()
    print(var_set, "has a type", type(var_set))

if __name__ == '__main__':
    my_var()