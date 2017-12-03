"""
Simple parser tugas TBA
Muhammad Arizal Saputro
Agung Tri Wibowo
Rixi Anggriawan
Amalia
"""

from MyParser import doParse
from MyValidator import checkToken

#Tugas Tahap 1




inputan = input('Masukan String (pisahkan dengan spasi): ')

output = doParse(inputan)

print(output)

#Tugas Tahap 2



print(checkToken(output))













