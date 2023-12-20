import gensim
import re
pat = re.compile("(.*)_NOUN")


pos = ["гардероб_NOUN","руководитель_NOUN","вешалка_NOUN","глава_NOUN"]
word2vec = gensim.models.KeyedVectors.load_word2vec_format("cbow.txt", binary=False, unicode_errors='ignore')
dist = word2vec.most_similar(positive =pos)
for i in dist:
    e = pat.match(i[0])
    if e is not None:
        print(e.group(1))
"""
слова : директор номерок
результат:
куратор
руководство
плечики
сотрудник
директор
номерок
вестибюль
шкаф

"""
