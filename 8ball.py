import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtfull']
print(messages[random.randint(0,len(messages)-1)]) #Notice this expression, this produces a random number between to use for the index, regardless of the size of messages
#That is, you'll get a random number between 0 and the value of len(messages) - 1
#The benefit of this approach is that you can easily add and remove strings to the messages list without changing other lines of code
#If you later update code, there will be fewer lines the change and fewer changes for you to introduce bugs
