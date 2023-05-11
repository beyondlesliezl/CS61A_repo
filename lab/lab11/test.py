dic = {'a': 2 ,'b':5}
print(dic['a'])
dic2 = {'c':2,'d':39}
dic.update(dic2)


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)  # 输出 {'a': 1, 'b': 3, 'c': 4}
