#!/usr/bin/env python3

from babel import Babel, _ , ngettext

# an example of marking strs for singular and plural forms
greeting = _("Hello, World!")

num = 5
message = ngettext(
    "You have one message",  # singular form
    "You have %(num)d messages",  # plural form
    num
) % {'num': num}   # formatting the message with the actual number
# example usage
print(greeting)   # output: Hello, World!
print(message)   # output: You have 5 meassages
