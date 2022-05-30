#!/usr/bin/env python3
# now we will be seeing characteristics of string by using square brackets "[]".
# this is usually to index the characters which are writen in the string

string_index = 'This is a test string'
#               0123456789.....

print(string_index[0])
# here what will happen that it will just print only 0 no of index from string_index line which will be "T".
# well I don't know about other programming language, but you can use -ve numbering for indexing to print  characters from the last of the statement.

print(string_index[-1])
# here you will get "G" which is the ending of "string" you can change the negative number to test it.

# what was happening in the above statement was that it only print a single characters.
# but what if you want to print certain characters from a sentence.
# for that we will use : to get it out just check the code below.
print(string_index[0:4])
# here you will be able to get "This" as an answer.
# let's see the explanation of string_index[0:4] here what will happen is it will return with 4 characters because 0 indicate the starting position and 4 means how much number of characters should be extracted from starting position of the index.
# now if I just want to print test string then I need to find out the location of test then just print it.
print(string_index[10:])
# here what it will do is it will start printing from test till the end because we have defined the starting point, but we haven't defined ending point so ti will print till the end.
# so as we have seen in the above code that if we don't give any number to ending point then it will print till the end but what if we don't define starting point and just define ending point then what will happen?
print(string_index[:4])
# as we have seen that square brackets are being used to print certain characters, so we can use it in different types of variables.
string_index_copy = string_index[:]
# so what we did is just copied all the text present in string_index to string_index_copy
print(string_index_copy)
