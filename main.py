from src.phonebook import Phonebook

contato = Phonebook()

print(contato.entries['POLICIA'])

contato.entries['Kleice']='1010'
print(contato.entries['Kleice'])

print(contato.entries.keys())
print(contato.entries.values())

print(contato.search('Kleice'))