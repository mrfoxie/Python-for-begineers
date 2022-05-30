#!/usr/bin/env python3
# Formatted strings are known as dynamic strings which increases the complexity of programming as well as it becomes hard for hackers to decode your code lets see the example.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
# as you know that we have taking input from user and then stored it into variables and say for example we want to highlight age.
# so what do we do is use concatenation to do it.

print(first_name + ' ' + last_name + ' is "' + age + '" old.')
# so as we see that this is just a static type of print. now we will be using dynamic style of formatting, due to that we will be using formatting tool to do it.
format_text = f'{first_name} {last_name} is "{age}" old.'
# when we use {} brackets which means that it's a dynamic text. this helps us to make a dynamic sentence or paragraph whenever you need it. now lets print it.
print(format_text)

# let's take an example test.
name_one = input("Enter name for first friend: ")
name_two = input("Enter name for second friend: ")
two_friends = f'''

{name_one} and {name_two} were friends. On a holiday they went walking into a forest, enjoying the beauty of nature. Suddenly they saw a bear coming at them. They became frightened.

{name_two}, who knew all about climbing trees, ran up to a tree and climbed up quickly. He didn’t think of {name_one}. {name_one} had no idea how to climb the tree.

{name_one} thought for a second. He’d heard animals don’t prefer dead bodies, so he fell to the ground and held his breath. The bear sniffed him and thought he was dead. So, it went on its way.

{name_two} asked {name_one}: “What did the bear whisper into your ears?”

{name_one} replied, “The bear asked me to keep away from friends like you” …and went on his way.

Moral of the story: A friend in need is a friend indeed.
'''
print(two_friends)
