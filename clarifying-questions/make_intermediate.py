# pip install spacy
# python -m spacy download en_core_web_sm

import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Process whole documents
# text = ("i am tired perhaps due to lack of sleep") #nvaaddndn
# text = ("i am super sleepy because lack of sleep") #nvaadndn
# text = ("dragon ball super is an anime") #nnnvnn
# text = ("the music is well written") #nnvav
# text = ("I ate fresh fruit for breakfast")
# text = ("I love grape juice")
# text = ("I eat fresh tattertots and mangoes for breakfast")
# text = "I am aware of the changes that you put in place"
text = ("give it to me")


doc = nlp(text)

n = ['PRON', 'NOUN', 'PROPN']
v = ['VERB', 'AUX']
a = ['ADJ', 'ADV']
d = ['ADP', 'SCONJ']
t = ['DET']
e = ['PART']
c = ['CCONJ']
k = ['PUNCT']

r = []

print(text)

for token in doc:
	p = token.pos_

	print(p, end=' ')

	if p in n:
		r.append('n')
	elif p in v:
		r.append('v')
	elif p in a:
		r.append('a')
	elif p in d:
		r.append('d')
	elif p in t:
		r.append('t')
	elif p in e:
		r.append('e')
	elif p in c:
		r.append('c')
	elif p in k:
		r.append('k')

print()
print(''.join(r))

dict = {}
dict['v'] = 'v'
dict['n'] = 'n'
dict['vn'] = 'v(n)'
dict['nv'] = 'n.v()'
dict['nvn'] = 'n.v(n)'
dict['nvvn'] = 'n.v_v(n)'
dict['anvvn'] = 'a_n.v(n)'
dict['anvn'] = 'a_n.v(n)'
dict['nnvn'] = 'n_n.v(n)'
dict['nnvvn'] = 'n_n.v_v(n)'
dict['nnva'] = 'n_n.v(a)'
dict['nvandn'] = 'n.v(a_n).d(n)'
dict['nvan'] = 'n.v(a_n)'
dict['nvndn'] = 'n.v(n.d(n))'
dict['nvancndn'] = 'n.v([a_n,` n]).d(n)'
dict['nnnvtn'] = 'n_n_n.v(t_n)'
dict['tnvav'] = 't_n.v(a_v)'
dict['nvaadndn'] = 'n.v(a_a.d(n.d(n)))'
dict['nvaaddndn'] = 'n.v(a_a.d_d(n.d(n)))'
dict['nvadtntnvdn'] = 'n.v(a.d(t_n.t(n.v().d(n))))'
dict['nvnn'] = 'n.v(n_n)'
dict['tdtvv'] = 't.d(t).v_v()'
dict['nvaa'] = 'n.v(a_a)'
dict['vndn'] = 'v(n).d(n)'

y = dict[''.join(r)]

print(y)

q = []
i = 0
for x in y:

	if x in ['(', ')', '_', '.', '[', ']', ',', ' ']:
		q.append(x)
	elif x in ['`']:
		i += 1
	else:
		q.append(doc[i].text)
		i += 1

print(''.join(q))

