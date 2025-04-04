# STRING METHODS

string = 'Hello, how are you'
s = type(string)
print(s)

s = dir(string) # using dir func you can know how many methods present for this class
print(s)

print(help(s.clear)) # Using help function you can know what does this methods do?


# find() METHOD
# find method is used to find occurrence of sub string in the original string(from left to right).
print(string.find('o'))
print(string.find('o',4))
print(string.find('o',5))
print(string.find('c'))
print(string.find('how'))

# rfind() METHOD
# (Traversing from right to left)
print(string.rfind('o'))
print(string.rfind('o',15))
print(string.rfind('o',0,15))
print(string.rfind('k'))

# index() METHOD
#(it is similier to find() method but the minor diff is that when any str is not present then error occer instence of -1)
print(string.index('o'))
print(string.index('o',4))
print(string.index('o',5))
print(string.index('how'))
# print(string.index('c')) # ERROR

# rindex() METHOD
# (it is similer to rfind() method same minor diff as well as find() and rfind method)
print(string.rindex('o'))
print(string.rindex('o',15))
print(string.rindex('o',0,15))
# print(string.rindex('k')) # Error

# count() METHOD (used to total count occerence of char or sub)
print(string.count('o'))
print(string.count('dhor')) # return 0


"""    THESE METHOD GENRATING NEW STRING NOT MODIFY ORIGINAL STRING (BELLOW)  """
# ljust() METHOD (it is used to give space from the LEFT side)
s = 'python'
n = s.ljust(10,'-')
print(n)
n = s.ljust(15,'.')
print(n)

# rjust() METHOD (it is used to give space from the RIGHT side)
n = s.rjust(10,'-')
print(n)

# center() METHOD (used to come center)
n = s.center(20,'-')
print(n)

"""   strip() method remove space along with character    """
# lstrip() METHOD (lstrip()used to remove only leading spaces)
new ="   python   "
n = new.lstrip()
# print(f"'{n}'")
print(n)

# rstrip() METHOD (rstrip()used to remove only trailing spaces)
n = new.rstrip()
print(n)

# strip() METHOD (strip() used to remove leading and trailing spaces)
n = new.strip()
print(n)

s1 = '.... ... +++ kkkhajoor'
print(s1.lstrip())
print(s1.lstrip(".")) #it will remove only starting dots because sfter this sapce there which is diff
print(s1.lstrip('. +')) #it can remove multiple char
print(s1.strip('. +k'))

# capitalize() METHOD (it capitalize only first latter of string)
string2 = "tu jhooti mai makkar"
c = string2.capitalize()
print(c)

# title() METHOD (it capitalize first latter of each word in string)
c = string2.title()
print(c)

# lower() METHOD (it makes lower to each word in str)
c = string2.lower()
print(c)

# upper() METHOD (it makes each letter capital)
c = string2.upper()
print(c)

# swapcase() METHOD (used to swap each upper to lower vica versa)
swap = 'HEllo , SHivanANSH'
c = swap.swapcase()
print(c)

# casefold() METHOD (it do work same as lower but minor diff is-)
c = swap.casefold()
print(c)

# MINOR DIFFERENCE 
a1 = 'heLLO'
a2 = 'HELLO'
print(a1 == a2)


T = True
F = False
if a1.lower() == a2.lower():
    print(T)
else:
    print(F)

b1 = 'Bu\u00DF'
print(b1)  # o/p Buß

b2 = 'Buss'
print(b1 == b2)
print(b1.lower() == b2.lower()) # False
print(b1.casefold() == b2.casefold())  #True

t = '\u01C6'
print(t)
print(t.upper())
print(t.title())

# isupper() METHOD 
print(string.isupper())
print(string2.isupper())
print(swap.isupper())
b = 'HELLO'
print(b.isupper())

# islower() METHOD
print(string.islower())
print(string2.islower())
print(swap.islower())

# istitle() METHOD
print(string.istitle())
print(string2.istitle())
print(swap.istitle())
print(b2.istitle())


# isalnum() METHOD (not consider space or any special char)
d = 'hello 5435'
print(d.isalnum())
print(b.isalnum())

# isalpha() METHOD (not consider space any char only alpha)
print(d)
print(string.isalpha())
print(b.isalpha())

# isspace() METHOD (consider only space even not empty str)
f = '   '
print(f.isspace())
f = ''
print(f.isspace())
print(b.isspace())

# isascii() METHOD (ASCII char consider like abc #@ etc)
print(string.isascii())
v = '`@ 4 - + = etc'
print(v.isascii())

# UNICODE 
uni_code = '\u03b1\u03b2\u03b3'
print(uni_code)
print(uni_code.isalpha())
print(uni_code.isalnum())
print(uni_code.isascii())

# isidentifire() METHOD (it check if literls or user_input follow varialbe rules then return in bool)
x = 'length_01'
y = '07_lenght'
z = 'length@_01'
print(x.isidentifier())
print(y.isidentifier())
print(z.isidentifier())

# isprintable() METHOD (it check if literls or user_input can be printable instead of escape(\t, \r, \n) char then return in bool)
print(x.isprintable())
o = 'hello \n boy'
print(o.isprintable()) # False

u = '\u03b8\u03b4\u03b7'
print(u)
print(u.isprintable())
print(u.isidentifier())

# isdecimal() isnumaric() isdigit() METHODS (all these works upon numaric data)
print("9038091489194718947")
num_str1 = '123'
print(num_str1.isdecimal())
print(num_str1.isdigit())
print(num_str1.isnumeric())

num_str2 = '8\u00b2'  
print(num_str2)  #('8^2') this is not valid so we write in unicode
print(num_str2.isdecimal())
print(num_str2.isdigit())
print(num_str2.isnumeric())

num_str3 = '5\u00bd'   #('1/2')
print(num_str3.isdecimal())
print(num_str3.isdigit())
print(num_str3.isnumeric())

# startswith(), endswith(), partition(), rpartition(), removesuffix(), removeprefix()
s = 'python is very easy'
# startswith() METHOD (It will say whether a given string is starts with)
print(s.startswith('python'))
print(s.startswith('is',7))
print(s.startswith('java'))

# endswith() METHOD (It will say if the string ends with ( certain string ) then it will return True) 
print(s.endswith('easy'))
print(s.endswith('java'))
print(s.endswith('is',0,9))

email = 'anushkapatkar497@gmail.com'
print(email.endswith('@gmail.com'))

# removeprefix() METHOD (It will remove the substring (from first only ))
print(email.removeprefix('anushka'))
print(email.removeprefix('patkar'))

# removesuffix() METHOD (It will remove the substring (last))
print(email.removesuffix('.com'))
print(email.removesuffix('@gmail'))

# partition() METHOD (It will divide s.partition(‘is‘) It will check where is ‘is’ then it will form a tuple)
print(s.partition('is'))
print(s.partition('s'))

# rpartition() METHOD (It will perform from the right hand side)
print(s.rpartition('s'))
print(s.rpartition('y'))
print(s.rpartition('e'))

# replace() METHOD (it replace specified substr with another substr in str)
r_string = 'I love banana , banana is my fav fruit'
new_string = r_string.replace('banana','apple')
print(new_string)
new_string = r_string.replace('banana','cherry',1)
print(new_string)

r_string = 'a-b-c-d-e'
result = r_string.replace('-',',')
print(result)
result = r_string.replace('-',',',2)
print(result)
# WHEN SPECIFY SUBSTR NOT AVAILABLE IN STR THEN IT RETURNS ORIGINAL STR
new_string = r_string.replace('n','f')
print(new_string)

r_string = 'anushka@gmail.com'
result = r_string.replace('gmail' , 'patkar')
print(result)

# join() METHOD(it used to combine elements of an iterable(list,tuple,string etc))
r = ['p','y','t','h','o','n']
result = ''.join(r)
print(result)

a = 'abc'
b = 'xyz'
r = a.join(b)  # calling a method and joining upon b
print(r)

c = '/'
r1 = c.join(a)
print(r1)

l1 = ['john', 'hanuman', 'ramji']
s = '-'
print(s.join(l1))
s = ','
print(s.join(l1)) # return as single str

# split() METHOD (it used to divied string into piece multiple time but it not return separator in o/p)
s = 'john hanuman ramji'
print(s.split())

l1 = 'john , hanuman , ramji'
print(l1.split(','))

s = 'john hanuman ramji'
print(s.split('n')) # Not return separater ('n')

s = 'ram-sita-hanuman-dev-sakti'
print(s.split())
print(s.split('-'))
print(s.split('-',3))

# rsplit() METHOD (it similer to split but it start from right side)
s = 'ram-sita-hanuman-dev-sakti'
print(s.rsplit('-'))
print(s.rsplit('-',3))

# splitlines() METHOD (it works only for newline )
new_line = 'aaa\nbbb\tccc\rddd\ffff'
print(new_line.splitlines())
print(new_line.splitlines(keepends = True))
print(new_line.split())
