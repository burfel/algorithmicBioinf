#!/usr/bin/env python
# encoding: utf-8

##-------- Uebung 5 -------------

'''
## Aufgabe 5.1
stationaere Verteiungen: pi_L = 2/3 , pi_F = 1/3
Die stationaere Verteilung gleicht den beobachteten Haeufigkeiten bei einer 
genuegend grossen Anzahl an Beobachtungen des Zufallsexperiment.
'''


## Aufgabe 5.2

############### following part from http://en.wikipedia.org/wiki/Viterbi_algorithm

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
 
    # Initialize base cases (t == 0)
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
 
    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}
 
        for y in states:
            (prob, state) = max((V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]
 
        # Don't need to remember the old paths
        path = newpath
    n = 0           # if only one element is observed max is sought in the initialization values
    if len(obs) != 1:
        n = t
#    print_dptable(V)
    (prob, state) = max((V[n][y], y) for y in states)
    return (prob, path[state])

 ######################################################################################
 
# observation sequence    
obs = list('315116246446644245311321631164152133625144543631656626566666651166453132651245636664631636663162326455236266666625151631222555441666566563564324364131513465146353411126414626253356366163666466232534413661661163252562462255265252266435353336233121625364414432335163243633665562466662632666612355245242') 

# the two states		 
states = ('F','L')  
# stable distribution
start_p = {'F': 1./3., 'L': 2./3. }  
# transition probabilities
transition_p = {'F' : {'F': 0.95, 'L': 0.05},'L' : {'F': 0.1, 'L': 0.9}} 
# emission probabilities
emission_p = {'F': {'1': 1./6., '2': 1./6., '3': 1./6., '4': 1./6., '5': 1./6., '6': 1./6.},'L': {'1':1./10., '2':1./10., '3':1./10., '4':1./10., '5':1./10., '6': 1./2.}}


(prob0, path0) = (viterbi(obs, states, start_p, transition_p, emission_p))    
print prob0,path0


## Aufgabe 5.3

# reverse observation sequence
list.reverse(obs)

(prob1, path1) = (viterbi(obs, states, start_p, transition_p, emission_p))
print '\n', prob1,path1

# reverse path sequence and determine hamming distance to original path0
list.reverse(path1)

def hamming_distance(s1, s2):
  distance = 0
  for i in range(len(s1)):
    distance += int(s1[i] != s2[i])
  return distance
	
print '\nHamming distance:', hamming_distance(path0, path1)

'''
Die Hamming-Distanz der beiden Sequenzen ist 0, d.h. sie sind identisch. 
'''
   


