import phonenumbers
from phonenumbers import geocoder

telefone = "+5597981173997"
telefone_ajustado = phonenumbers.parse(telefone)
print(telefone_ajustado)
# Descobrir localização do numero
local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
print(local)
