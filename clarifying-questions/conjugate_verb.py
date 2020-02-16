import mlconjug

# # To use mlconjug with the default parameters and a pre-trained conjugation model.
# default_conjugator = mlconjug.Conjugator(language='fr')

# # Verify that the model works
# test1 = default_conjugator.conjugate("manger").conjug_info['Indicatif']['Passé Simple']['1p']
# test2 = default_conjugator.conjugate("partir").conjug_info['Indicatif']['Passé Simple']['1p']
# test3 = default_conjugator.conjugate("facebooker").conjug_info['Indicatif']['Passé Simple']['1p']
# test4 = default_conjugator.conjugate("astigratir").conjug_info['Indicatif']['Passé Simple']['1p']
# test5 = default_conjugator.conjugate("mythoner").conjug_info['Indicatif']['Passé Simple']['1p']
# print(test1)
# print(test2)
# print(test3)
# print(test4)
# print(test5)

# You can now iterate over all conjugated forms of a verb by using the newly added Verb.iterate() method.
default_conjugator = mlconjug.Conjugator(language='en')
test_verb = default_conjugator.conjugate("sit")
all_conjugated_forms = test_verb.iterate()
print(all_conjugated_forms)