from collections import OrderedDict

a=5
ordered_dictionary = OrderedDict()

# ordered_dictionary['a'] = 1
ordered_dictionary['b'] = 2
ordered_dictionary['c'] = 3
ordered_dictionary['d'] = 4
ordered_dictionary['e'] = 5

ordered_dictionary['a']=ordered_dictionary.get('a',0)+5

print(ordered_dictionary['a'])