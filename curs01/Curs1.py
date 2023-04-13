from decimal import Decimal
print("hellow world!")

name = 'Andrei'

print(name)

if name == 'Andrei':
    print(f'Avem de a face cu {name}')
else:
    print('nu stiu cine esti!')

names = ['Ana' , 'Ioana', 'Maria', 'Alexandru', 'Mario', 'Iza']


keyword = 'Elena'

if keyword not in names:
    print(f'{keyword} was not found!')

if not (4 <2):
    print('Salut')

d1 = {1: 'Salut'}
d2 = d1

print ((d1 is d2))

empty_str = ' '

print(chr(97))
print(ord('A'))

print ('Salut \n\tMarius \\')

print(r'Salut \n Marius')

print(f'For only ')

price = Decimal(49)
print(f'For only {price:.2f} dollars! {name} have a nice day!')

print(name)
# strings are immutable!! (odata definit un string nu se poate modifica)

name ='Darius'
print(name)

my_list = list()
my_list = []

print(names)
names[0] = 'Elena'
#print(names)
#print(names[:2])
#names.sort()
print(sorted(names))

print(names)

#intr un set fiecare elem este unic
#intr o lista poti avea "elena" de mai multe ori

names = ['Ana' , 'Ana', 'Ioana', 'Maria', 'Alexandru', 'Mario', 'Iza']
print(names)
set_names = set(names)
print(set_names)
#setul este o colectie neordonata si imutabil , seturile nu sunt indexate

new_names = ['Ana', 'Gabriela']
set_new_names = set(new_names)
print(set_new_names.issubset(set_names))

new_list = list(set_new_names)
print(new_list)

all_wrods = {
    'vacanta': ['www.tui.ro', 'www.booking.com'],
    'grecia': ['www.wikipedia.com', 'www.booking.com']
}

person = {
    'name': 'Ion',
    'last_name': 'Popescu',
    'age': 34,

}

print(person['age'])