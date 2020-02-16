inv = {}
inv['I'] = "you"

text = "I.choose(to_attend(TreeHacks))"


who = text[0:text.index('.')]
verb = text[text.index('.')+1:text.index('(')]
text2 = text[text.index('(')+1:-1]
what = text2[0:text2.index('(')]
what2 = text2[text2.index('(')+1:-1]


print(who)
print(verb)
print(what)
print(what2)

print()


print('why did', inv[who], verb, 'so', '?')
print('why did', inv[who], verb, what, '?')
print('when did', inv[who], verb, what, '?')
print('why did', inv[who], verb, what2, 'specifically', '?')
