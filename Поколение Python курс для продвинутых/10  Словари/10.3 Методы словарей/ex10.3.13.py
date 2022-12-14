# Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.


s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'


slist = s.split()
sdict = {}
res_word_list = []
for word in slist:
    sdict[word] = sdict.get(word, 0) + 1
max_value = max(sdict.values())
for key, value in sdict.items():
    if value == max_value:
        res_word_list.append(key)
print(min(res_word_list))

