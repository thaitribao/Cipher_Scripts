#This file contains the constant lists for the rotors used in Enigma
#The rotors matched the calculated value described in Rotors.xls
#Think of this as a rotor box from which you can pick
#Which ever rotor you want to place in the machine

#First Rotor
ROTOR_1 = [3,16,13,7,9,6,1,9,10,-3,-6,10,13,7,8,9,3,-17,5,-11,-19,-7,-17,-14,-12,-23]
#Second Rotor (Ceasar shift by 1)
ROTOR_2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-25]


ROTORS = [ROTOR_1,ROTOR_2]
