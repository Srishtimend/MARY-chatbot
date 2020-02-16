# A Sub-Experiment On Generating Clarifying Questions

Objective: To get the who what when where and why from a sentence, then rearrange them in a variety of ways to form questions.

#### Example 1
I have always like onions
When did you start liking onions?

#### Example 2
I watched a play
who: I
verb: watched
what: a_play
when: (empty)
where: (empty)
why: (empty)
how: (empty)
Since some of the fields (when, where, why, and how) are blank, proceed to ask user in order to fill in the information
Which play did you watch?
Where did you watch it?
Did you like watching it?
What made you want to watch it?
By play, do you mean a drama performance, or moves made in a sports game?

## Sample Outputs
make_intermediate.py
```
give it to me
VERB PRON ADP PRON 
vndn
v(n).d(n)
give(it).to(me)
[Finished in 1.7s]
```

example_question1.py
```
Molly
is
upset

why is Molly upset ?
what makes Molly upset ?
how is Molly upset ?
[Finished in 0.1s]
```

example_question2.py
```
I
choose
to_attend
TreeHacks

why did you choose so ?
why did you choose to_attend ?
when did you choose to_attend ?
why did you choose TreeHacks specifically ?
[Finished in 0.1s]
```


conjugate_verb.py
```
[('imperative', 'imperative present', '2s', 'sit'), ('imperative', 'imperative present', '1p', 'sit'), ('imperative', 'imperative present', '2p', 'sit'), ('indicative', 'indicative past tense', '1s', 'sat'), ('indicative', 'indicative past tense', '2s', 'sat'), ('indicative', 'indicative past tense', '3s', 'sat'), ('indicative', 'indicative past tense', '1p', 'sat'), ('indicative', 'indicative past tense', '2p', 'sat'), ('indicative', 'indicative past tense', '3p', 'sat'), ('indicative', 'indicative present', '1s', 'sit'), ('indicative', 'indicative present', '2s', 'sit'), ('indicative', 'indicative present', '3s', 'sits'), ('indicative', 'indicative present', '1p', 'sit'), ('indicative', 'indicative present', '2p', 'sit'), ('indicative', 'indicative present', '3p', 'sit'), ('indicative', 'indicative present continuous', '1s 1s', 'sitting'), ('indicative', 'indicative present continuous', '2s 2s', 'sitting'), ('indicative', 'indicative present continuous', '3s 3s', 'sitting'), ('indicative', 'indicative present continuous', '1p 1p', 'sitting'), ('indicative', 'indicative present continuous', '2p 2p', 'sitting'), ('indicative', 'indicative present continuous', '3p 3p', 'sitting'), ('indicative', 'indicative present perfect', '1s', 'sat'), ('indicative', 'indicative present perfect', '2s', 'sat'), ('indicative', 'indicative present perfect', '3s', 'sat'), ('indicative', 'indicative present perfect', '1p', 'sat'), ('indicative', 'indicative present perfect', '2p', 'sat'), ('indicative', 'indicative present perfect', '3p', 'sat'), ('infinitive', 'infinitive present', 'it', 'sit')]
[Finished in 1.0s]
```