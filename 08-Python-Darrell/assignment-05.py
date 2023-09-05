str = 'Qui labore Lorem ullamco esse adipisicing ad eu cupidatat commodo ea ullamco. Id et ad eu veniam consectetur. Ullamco ipsum sint proident amet do cupidatat cupidatat laboris mollit laborum ex irure non occaecat. Aliquip eu tempor nisi et qui non esse ad quis reprehenderit. Adipisicing adipisicing quis eu excepteur fugiat culpa et commodo exercitation exercitation. Deserunt duis labore officia nisi do nostrud anim laborum occaecat. Laborum Lorem reprehenderit sit aute ullamco fugiat nostrud adipisicing exercitation. Aute ex magna enim officia aliqua nostrud cupidatat.'

""" 
    Find the word size that occurs the most 
    Ex Output:
        5 letter words occurs the most with 15 occurrances    
"""
#Create dict 
word_size = {len(word): 0 for word in str.split()}

#Count occurrences of each word size
for word in str.split():
    word_size[len(word)] +=1

#Find most common word size and occurences
most_common = max(word_size, key=word_size.get)
occurences = word_size[most_common]

#Print result
print(f"{most_common} letter words occurs the most with {occurences} occurrences")

