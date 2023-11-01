import typing
from nltk.tokenize import word_tokenize
from typing import Optional
from rnnmorph.predictor import RNNMorphPredictor 

tag = typing.NamedTuple('tag', case = str, gender =str, number =str) 

def unpack(s:str) -> Optional[tag]:
    a = s.split('|')
    c = g = n = None 
    for sent in a:
        words = sent.split('=')
        match words[0]:
            case 'Case':
                c = words[1]
            case 'Gender':
                g = words[1]
            case 'Number':
                n = words[1]
    if ((c is None) or (n is None)):
        return None
    else:
        return tag(c, g, n)

predictor = RNNMorphPredictor(language='ru')
f = open('input.txt','r')
st = f.read()
f.close()
s = predictor.predict(word_tokenize(st))
ans = []

for i in range(0, len(s)-1):
    if(s[i].pos == 'NOUN' or s[i].pos == 'ADJ' or 
       s[i+1].pos == 'NOUN' or s[i+1].pos == 'ADJ'):
        tag1 = unpack(s[i].tag)
        tag2 = unpack(s[i+1].tag)
        if (tag1 is not None and tag1 == tag2 ):
            ans.append((s[i].normal_form, s[i+1].normal_form))

with open('output_rnn.txt', 'w') as fp:
    fp.write('\n'.join('%s %s' % x for x in ans))
