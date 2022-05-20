#!/usr/bin/env python3
# now we will be seeing characteristics of string by using square brackets "[]".
# this is usually to index the characters which are writen in the string

string_index = 'This is a test string'
#               0123456789.....

print(string_index[0])
# here what will happen that it will just print only 0 no of index from string_index line which will be "T".
# well I don't know about other programming language, but you can use -ve numbering for indexing to print characters from the last of the statement.

print(string_index[-1])
# here you will get "G" which is the ending of "string" you can change the negative number to test it.

# what was happening in the above statement was that it only print a single characters.
# but what if you want to print certain characters from a sentence.
# for that we will use : to get it out just check the code below.
print(string_index[0:4])
# here you will be able to get "This" as an answer.
# let's see the explanation of string_index[0:4] here what will happen is it will return with 4 characters because 0 indicate the starting position and 4 means how much number of characters should be extracted from starting position of the index.
