ext = "the cat sat on the mat the cat purred"
words={}
for word in ext.split(): # split method is used to split the string into a list of words based on whitespace
    if word in words:    #checking if the word is already in the dictionary or not
        words[word] += 1 # increment the count of the word
    elif word not in words:
        words[word] = 1 # add the word to the dictionary with a count of 1

print(words)
        