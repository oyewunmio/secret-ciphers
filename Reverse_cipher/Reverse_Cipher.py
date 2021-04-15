'''Reverse cipher does encrypts a message by printing it in reverse order
And decrypting it by reversing the reversed message to get the original message'''

# note this cipher is a very weak cipher 

Message = input('Enter your message:\t')
length = len(Message)
reversed = ''
while length > 0:
    length -= 1
    reversed = reversed + Message[length]

print('The message has been encrypted to\n',reversed)

