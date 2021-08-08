import phonenumbers
print('Telefon raqam orqali davlatini va qaysi servisdaligini aniqlab beradigon dastur.')
from phonenumbers import geocoder
number = input('Telefon raqaminggizni kiriting: ')
ch_number = phonenumbers.parse(number,"ch")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "en")
print(carrier.name_for_number(service_number,"en"))
