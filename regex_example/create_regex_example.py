'''
ref: https://docs.python.org/3.6/library/re.html
'''
import re

# create Regex object
#    - passing raw string r'...'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')


# Regex.search() method
#    - searches the string it is passed for any matches to the regex
#    - returns Match object
#    - if no match, returns None   
mo = phoneNumRegex.search('My number is 415-555-4242.')
# NoneTypeError if no match
print('Phone number found: ' + mo.group())

# grouping with ()
#
# create groups
#    - group() or group(0) returns entire matched text
#    - group(1) returns 1st grouped match, group(2) returns 2nd grouped match
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group())     # 415-555-4242
print(mo.group(1))    # 415
print(mo.group(2))    # 555-4242

# show tuple of grouped matches
print(mo.groups())    # ('415', '555-4242')

# match multiple groups
#    - when pipe '|' is used, the first one matched will be returned
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
#Batman

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())
#Tina Fey

# another example
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
#Batmobile
print(mo.group(1))
#mobile

#
# ? optional match
#
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
#Batman
print(mo1.groups())
#(None,1)

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
#Batwoman
print(mo2.group(1))
#wo

#
# * matching zero or more
#
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
#Batman

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
#Batwoman

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
#Batwowowowoman

#
# + matching one or more
#
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
#Batwoman

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
#Batwowowowoman

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)
#True

# {} matching with specific occurance
#    - {3}   3 times
#    - {,4}  up to 4 times
#    - {2,5} 2 to 4 times
#    - {4,}  4 times or more
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
#HaHaHa

mo2 = haRegex.search('Ha')
print(mo2 == None)
#True

# regex is 'greedy' by default
#    - matches the longest string possible
#    - if 'non-greedy', matches shortest string
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
#HaHaHaHaHa

# {}? 
#    - to define 'non-greedy'
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
#HaHaHa

# Regex.findAll() method
#    - search() is for one match
#    - findAll() finds all, return a list of all matches
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
#415-555-9999

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
#['415-555-9999', '212-555-0000']

# findAll with groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # has no groups
ml = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(ml)
#[('415, '555-9999'), ('212', '555-0000')]



'''Common character Classes
\d  Any numeric digit from 0 to 9.

\D  Any character that is not a numeric digit from 0 to 9.

\w  Any letter, numeric digit, or the underscore character. (Think of this 
    as matching "word" characters.)

\W  Any character that is not a letter, numeric digit, or the underscore
    character.

\s  Any space, tab, or newline character. (Think of this as matching "space"
    characters.)

\S  Any character that is not a space, tab, or newline.

Special class:
[0-5]  is same as (0|1|2|3|4|5) but much shorter and neat
[a-zA-Z0-9]  group together
[^aeiouAEIOU]  [^...] refers to negative class which matches all characters
               there are not in the character class
'''
# example
xmasRegex = re.compile(r'\d+\s\w+')
ml = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds_nest, 3 hens, 2 doves, 1 partridge')

print(ml)
#['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

# customer made character class
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))
#['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

# ^ at the start of regex means must match at the beginning
# $ at the end means must match at the end
#
beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello world!')
print(mo)
#<_sre.SRE_Match object; span=(0, 5), match='Hello'>
print(mo.group())
#Hello

print(beginsWithHello.search('He said hello.') == None)
#True

# example
#    - end with a digit
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
#<_sre.SRE_Match object; span=(16, 17), match='2'>
print(endsWithNumber.search('Your number is forty two.') == None)
#True

# example
#    - start AND end with at least one or more digits
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
#<_sre.SRE_Match object; span=(0, 10), match='1234567890'>
print(wholeStringIsNum.search('12345xyz67890') == None)
#True
print(wholeStringIsNum.search('12 34567890') == None)
#True

# . a wildcard character match any one character, except newline
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
#['cat', 'hat', 'sat', 'lat', 'mat']

# (.*)
#    - match anything
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
#Al
print (mo.group(2))
#Sweigart

# example
#    - 'non-greedy' mode
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
#<To serve man>

#    - default 'greedy' mode
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
#<To serve man> for dinner.>

# (.*) including '\n'
#    - re.DOTALL as 2nd argument
noNewlineRegex = re.compile('.*')
g = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(repr(g))
#Serve the public trust.

newlineRegex = re.compile('.*', re.DOTALL)
g = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(repr(g))   # print raw text
#Serve the public trust.\nProtect the innocent.\nUphold the law.

# re.I or re.IGNORECASE  
#    - case insensitive
robocop = re.compile(r'robocop', re.I)
print(robocop.search('Robocop is part man, part machine, all cop.').group())
#Robocop

# Regex.sub() method
#    - string to replace any matches
namesRegex = re.compile(r'Agent \w+')
s = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(s)
#CENSORED gave the secret documents to CENSORED.

# exmaple
#    - The \1 in r'\1****' will be replaced by whatever text was matched by
#      group 1
agentNamesRegex = re.compile(r'Agent (\w)\w*')
s = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(s)
#A**** told C**** that E**** knew B**** was a double agent.

# re.VERBOSE mode
#    - make regex easier to read
#    - uses ''' ''' to create multiline string
#    - #comment are ignored
# instead of ...
#
# phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
#
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

# regex can only accept a 2nd argument
#    - if several flag constants are reqquired
#    - need to combine several flag constants into one
# example
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
