import nltk
from nltk.tokenize import word_tokenize
from pymorphy2 import MorphAnalyzer

f = open('input.txt','r')
st = f.read()
s = word_tokenize(st)
morph = MorphAnalyzer()
ans = []
f.close()

def checker (a, b: str):
    p = morph.parse(a)[0]
    p1 = morph.parse(b)[0]
    if(p.tag.POS == 'NOUN' or p.tag.POS == 'ADJF' or
       p1.tag.POS == 'NOUN' or p1.tag.POS == 'ADJF'):
        if(p.tag.case == p1.tag.case and p.tag.number == p1.tag.number 
           and p.tag.gender == p1.tag.gender):
            ans.append((p.normal_form, p1.normal_form))

for i in range(0, len(s)-1): 
    checker(s[i], s[i+1])

with open('output_pymorph.txt', 'w') as fp:
    fp.write('\n'.join('%s %s' % x for x in ans))

