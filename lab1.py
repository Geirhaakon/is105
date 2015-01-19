# -*- coding: latin-1 -*-

#
#  IS-105 LAB1
#
#  lab1.py - kildekode vil inneholde studentenes l�sning.
#         
#
#
import sys

# Skriv inn fullt navn p� gruppemedlemene (erstatte '-' med navn slikt 'Kari Tr�')
gruppe = {  'student1': 'Glenn Greibesland' }

#
#  Oppgave 1
#    Leke med utskrift 
#    Skriv ut f�lgende "ascii art" i en funksjon (erstatte pass)
#    Funksjonen skal hete ascii_fugl() og skal være uten argumenter og uten returverdier
#    Den skal skrive ut f�lgende n�r den brukes ascii_fugl
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
#	 Implementer funksjonen som gj�r en "bitwise" AND operasjon (erstatt pass)
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
#    For � finne desimalverdien til et tegn kan funksjonen ord brukes, for eksempel
#      ord('A') , det vil gi et tall 65 i ti-tallssystemet
#    For � formattere 6 i ti-tallssystemet til 00000110 i to-tallssystemet
#      '{0:08b}'.format(6)
#      00000110
#
#    Formatteringsstrengen forklart:
#      {} setter en variabel inn i strengen
#      0 tar variabelen i argument posisjon 0
#      : legger til formatteringsmuligheter for denne variabelen (ellers hadde den 6 desimalt)
#      08 formatterer tall til 8 tegn og fuller med nuller til venstre hvis n�dvendig
#      b konverterer tallet til dets binære representasjon
#
#	 Hvilke begrensninger vil en slik funksjon ha? (tips: pr�v med bokstaven '�', f.eks.)
#	 Forklar resultatet ascii8Bin('�')
#	 Hvilke faktorer p�virker resultatet? Forklar.
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
#	 Forklart hver linje i denne funksjonen (hva er list, hva gj�r in)
#	 Skriv selv inn tester ved � bruke assert i funksjonen test()
#
def transferBin(string): 
	l = list(string)
	for c in l:
		# skriv ut den binære representasjon av hvert tegn (bruk ascii8Bin funksjonen din)
		print "Den binære representasjonen for %s:" % c, ascii8Bin(c)
		

def transferBinSummary(string):
	binString = ''
	for char in string:
		binString += ascii8Bin(char)
		print "Hele den bin�re representasjonen av strengen: %s" % binString
#
#  Oppgave 7
#    transferHex - gj�r det samme som transferBin, bare skriver ut representasjonen
#					av strengen heksadesimalt (bruk formattering forklart i Oppgave 6)
#					Skriv gjerne en st�ttefunksjon ascii2Hex, som representerer et tegn
#					med 2 heksadesimale tegn
#    Skriv selv inn tester ved � bruke assert i funksjonen test()
#  
def transferHex(string):
	l = list(string)
	for c in l:
		print "Den heksadesimale representasjonen for %s:" % c, ascii2Hex(c)

def transferHexSummary(string):
	hexString = ''
	for char in string:
		hexString += ascii2Hex(char)
		print "Hele den bin�re representasjonen av strengen: %s" % hexString
#
#
# Oppgave 8
# 		Implementer en funksjon unicodeBin, som kan behandle norske bokstaver
# 		Kravspesifikasjon for denne funksjonen er den samme som for ascii8Bin funksjonen
def unicodeBin(character):
	return ''.join(format(ord(i),'0>8b') for i in character)

#
# Oppgave 9
# 	Studer python module psutils (m� være obs p� versjon)
#   Pr�v � finne ut hvordan du kan finne ut og skrive ut f�lgende informasjon om din 
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
#	Hvilke andre muligheter har man for � finne informasjon om maskinvare i GNU/Linux?
#
def printSysInfo():
	pass


def test():
	assert bitAnd(6, 5) == 4
	assert bitXor(4, 5) == 1
	assert bitOr(0, 1) == 1
	assert ascii8Bin('a') == '01100001'
	assert ascii8Bin('A') == '01000001'
	# Skriv her inn passende tester for tarnsferBin og transferHex funksjoner
	# fra oppgavene 6 og 7
	assert unicodeBin('�') == '11100101'
	# Dine egne tester
	return "Testene er fullf�rt uten feil."


# Bruk denne funksjonen for � vise at alle testene er kj�rt feilfritt
print test()
		
