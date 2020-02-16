text = "Molly.is(upset)"

who = text[0:text.index('.')]
verb = text[text.index('.')+1:text.index('(')]
what = text[text.index('(')+1:text.index(')')]

print(who)
print(verb)
print(what)

print()

print('why',verb,who,what,'?')
print('what makes',who,what,'?')
print('how',verb,who,what,'?')