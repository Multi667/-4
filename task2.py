alf = {}


def get_count_char(str_):
    str_ = str_.strip()  # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = str_.lower()
    new_s = []
    for i in str_:
        if i.isalpha() == True:
            new_s.append(i)
    str_ = ''.join(new_s)
    new_s.sort()

    for i in str_:
        if i in alf:
            alf[i] += 1
        else:
            alf[i] = 1
    return alf


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def finally_I_did_it(slovar):
    val = slovar.values()
    key = slovar.keys()
    summa = sum(val)
    proc = summa/100
    result = [int(num * proc) for num in val]   #Для ответа она не нужна, но в условии требуется же)
    slo = dict(zip(key, result))
    return slo
