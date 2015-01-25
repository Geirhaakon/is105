# -*- coding: latin-1 -*-

#
#  IS-105 LAB1
#
#  lab1.py - kildekode vil inneholde studentenes løning.
#         
#
#
import sys
import psutil
# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå)
gruppe = {  'student1': 'Glenn Greibesland' }

#
#  Oppgave 1
#    Leke med utskrift 
#    Skriv ut følgende "ascii art" i en funksjon (erstatte pass)
#    Funksjonen skal hete ascii_fugl() og skal være uten argumenter og uten returverdier
#    Den skal skrive ut følgende nå den brukes ascii_fugl
#
#       \/_
#  \,   /( ,/
#   \\\' ///
#    \_ /_/
#    (./
#     '` 
def ascii_fugl():
	thebird = """\
       \/_
  \,   /( ,/
   \\\' ///
    \_ /_/
    (./
     '`
     """
	print thebird

#  Oppgave 2
#    bitAnd - x&y
#	 Implementer funksjonen som gjør en "bitwise" AND operasjon (erstatt pass)
#    Eksempel: bitAnd(6, 5) = 4
#		Forklaring: 6 binært er 110, mens 5 er 101. Hvis vi sammenligner bitvis
#					1 AND 1 gir 1, 1 AND 0 gir 0 og 0 AND 1 gir 0 => 100 binært
#					er 4 desimalt. Antagelse: posisjonsbasert tallsystem og 
#					den mest signifikante bit-en er lengst til venstre
def bitAnd(x, y):
	return x&y

#
#  Oppgave 3
#    bitXor - x^y
#    Eksempel: bitXor(4, 5) = 1
#
def bitXor(x, y):
	return x^y

#
#  Oppgave 4
#    bitOr - x|y
#    Eksempel: bitOr(0, 1) = 1
#
def bitOr(x, y):
	return x|y

#
#  Oppgave 5
#
#  Tips:
#    For å finne desimalverdien til et tegn kan funksjonen ord brukes, for eksempel
#      ord('A') , det vil gi et tall 65 i ti-tallssystemet
#    For å formattere 6 i ti-tallssystemet til 00000110 i to-tallssystemet
#      '{0:08b}'.format(6)
#      00000110
#
#    Formatteringsstrengen forklart:
#      {} setter en variabel inn i strengen
#      0 tar variabelen i argument posisjon 0
#      : legger til formatteringsmuligheter for denne variabelen (ellers hadde den 6 desimalt)
#      08 formatterer tall til 8 tegn og fuller med nuller til venstre hvis nødvendig
#      b konverterer tallet til dets binære representasjon
#
#	 Hvilke begrensninger vil en slik funksjon ha? (tips: prøv med bokstaven 'å', f.eks.)
#	 Forklar resultatet ascii8Bin('å')
#	 Hvilke faktorer påvirker resultatet? Forklar.
#
def ascii8Bin(letter):
	return '{0:08b}'.format(ord(letter))

def ascii2Hex(letter):
	return '{0:x}'.format(ord(letter))

# 
# 
#  Oppgave 6
#    transferBin - ta en tilfeldig streng som argument og skriver ut en blokk av 8-bits strenger
#                  som er den binære representasjon av strengen
#    Eksempel: transferBin("Hi") skriver ut: 
#                01001000
#                01101001
#	 Forklart hver linje i denne funksjonen (hva er list, hva gjør in)
#	 Skriv selv inn tester ved å bruke assert i funksjonen test()
#
def transferBin(string): 
	l = list(string) # Ikke nødvendig å legge i liste.
	for c in l:
		# skriv ut den binære representasjon av hvert tegn (bruk ascii8Bin funksjonen din)
		return "Den binære representasjonen for %s:" % c, ascii8Bin(c)
		

def transferBinSummary(string):
	binString = ''
	for char in string:
		binString += ascii8Bin(char)
	return "Hele den bin�re representasjonen av strengen \'%s\' er: %s" % (string, binString)
#
#  Oppgave 7
#    transferHex - gjør det samme som transferBin, bare skriver ut representasjonen
#					av strengen heksadesimalt (bruk formattering forklart i Oppgave 6)
#					Skriv gjerne en støttefunksjon ascii2Hex, som representerer et tegn
#					med 2 heksadesimale tegn
#    Skriv selv inn tester ved å bruke assert i funksjonen test()
#  
def transferHex(string):
	l = list(string)
	for c in l:
		return "Den heksadesimale representasjonen for %s:" % c, ascii2Hex(c)

def transferHexSummary(string):
	hexString = ''
	for char in string:
		hexString += ascii2Hex(char)
	return "Hele den heksadesimale representasjonen av strengen \'%s\' er: %s" % (string, hexString)
#
#
# Oppgave 8
# 		Implementer en funksjon unicodeBin, som kan behandle norske bokstaver
# 		Kravspesifikasjon for denne funksjonen er den samme som for ascii8Bin funksjonen
def unicodeBin(character):
	return '{0:08b}'.format(ord(character.decode('utf8')))

#
# Oppgave 9
# 	Studer python module psutils (må være obs på versjon)
#   Prøv å finne ut hvordan du kan finne ut og skrive ut følgende informasjon om din 
#   datamaskin-node:
#
# 			Brand and model
# 			Hard drive capacity
# 			Amount of RAM
# 			Model and speed of CPU
# 			Display resolution and size
# 			Operating system
#	
#	Forklar hvorfor man kan / ikke kan finne denne informasjon vha. psutil modulen.
#	Skriv en funksjon printSysInfo som skriver ut den informasjon som psutil kan finne.
#	Kan dere skrive en test for denne funksjonen?
#	Hvilke andre muligheter har man for å finne informasjon om maskinvare i GNU/Linux?
#
def printSysInfo():
	mem = psutil.virtual_memory()
	hdd = psutil.disk_partitions()
	print "Memory information: \n", mem, "\n\nHard drive information: \n", hdd


def test():
	assert bitAnd(6, 5) == 4
	assert bitXor(4, 5) == 1
	assert bitOr(0, 1) == 1
	assert ascii8Bin('a') == '01100001'
	assert ascii8Bin('A') == '01000001'
	# Skriv her inn passende tester for tarnsferBin og transferHex funksjoner
	# fra oppgavene 6 og 7
	hexTestString = 'vanskeligTest'
	hexTest = transferHexSummary(hexTestString).split(':')[1].strip()
	assert hexTest == '76616e736b656c696754657374'
	assert len(hexTest)/2 == len(hexTestString)
	binTestString = 'VeldiGvanskeliG'
	binTest = transferBinSummary(binTestString).split(':')[1].strip()
	assert binTest == '010101100110010101101100011001000110100101000111011101100110000101101110011100110110101101100101011011000110100101000111'
	assert len(binTest)/8 == len(binTestString)
	
	#Sjekk at transferBinSummary er riktig i forhold til ascii8Bin
	binS = 0
	binE = 8
	for c in binTestString:
		assert binTest[binS:binE] == ascii8Bin(c)
		binS+=8
		binE+=8 

	#Sjekk at transferHexnSummary er riktig i forhold til ascii2Hex
	hexS = 0
	hexE = 2
	for c in hexTestString:
		assert hexTest[hexS:hexE] == ascii2Hex(c)
		hexS+=2
		hexE+=2 
	
	assert unicodeBin('å') == '11100101'

	return "Testene er fullført uten feil."

	

# Bruk denne funksjonen for å vise at alle testene er kjørt feilfritt
print test()
		
