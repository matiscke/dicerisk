# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:49:34 2016
Dicing algorithm for the board game "Risk". This tool saves you from dicing forever when two large armies confront each other in the game. 

Winning probabilities are taken from:
Jörg Bewersdorff: Glück, Logik und Bluff: Mathematik im Spiel - Methoden, Ergebnisse und Grenzen, Vieweg+Teubner Verlag, 5. Auflage 2010

@author: Martin Schlecker, March 2016
"""
import numpy as np
import sys

def singleAttack(Nattack, Ndefend):
    Ptie = .0
    # winning probabilities depending on attackers-to-defenders ratio
    if Nattack == 1:
        if Ndefend == 1:
            Ptotal = .417
            Pdefeat = .583
        elif Ndefend == 2:
            Ptotal = .255
            Pdefeat = .746
    elif Nattack == 2:
        if Ndefend == 1:
            Ptotal = .579
            Pdefeat = .421
        elif Ndefend == 2:
            Ptotal = .228
            Pdefeat = .448
            Ptie = .324
    elif Nattack == 3:
        if Ndefend == 1:
            Ptotal = .660
            Pdefeat = .340
        elif Ndefend == 2:
            Ptotal = .372
            Pdefeat = .293  
            Ptie = .336
    # compute outcome of single battle
    # pick random number from uniform distribution [0,1]
    p = np.random.rand()
    if p < Ptotal:
        return 'total'
    elif Ptotal < p < Ptotal + Pdefeat:
        return 'defeat'
    else:
        return 'tie'

def main(Nattack, Ndefend):
    Nbattles = 0
    # dice attacks until one army is depleted
    while (Nattack > 0) and (Ndefend > 0):
        outcome = singleAttack(min(Nattack, 3), min(Ndefend, 2))
        if outcome == 'total':
            Ndefend -= min(Ndefend, 2)
        elif outcome == 'defeat':
            Nattack -= min(Nattack, 2)
        else:
            Ndefend -= 1
            Nattack -= 1
        Nbattles += 1
    
    # output results
    print '{} battles fought.'.format(Nbattles)
    print 'remaining attackers: {}\nremaining defenders: {}'.format(Nattack, Ndefend)
    if Nattack > Ndefend:
        print 'The attacker wins!'
    elif Ndefend > Nattack:
        print 'The defender wins!' 
        
        
if __name__ == "__main__":
    if len(sys.argv) >= 2:  # check if argument given (first element is the script itself)
        main(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print 'Not enough arguments given. Inputs are number of attackers, number of defenders.'
