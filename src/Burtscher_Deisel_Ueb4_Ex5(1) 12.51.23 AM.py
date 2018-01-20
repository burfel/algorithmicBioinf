# Using Python 2.7


# Viterbi Algorithmus
# Code von: http://en.wikipedia.org/wiki/Viterbi_algorithm
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
            (prob, state) = max((V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0)\
                for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]
 
        # Don't need to remember the old paths
        path = newpath
    n = 0           # if only one element is observed max is sought in the 
                    #initialization values
    if len(obs) != 1:
        n = t
    #print_dptable(V)
    (prob, state) = max((V[n][y], y) for y in states)
    return (prob, path[state])
 
# Prints a table of the steps.
# Code von: http://en.wikipedia.org/wiki/Viterbi_algorithm
def print_dptable(V):
    s = "    " + " ".join(("%7d" % i) for i in range(len(V))) + "\n"
    for y in V[0]:
        s += "%.5s: " % y
        s += " ".join("%.7s" % ("%f" % v[y]) for v in V)
        s += "\n"
    print(s)
    
   
if __name__ == '__main__':
    file = open('casino.txt','r')
    content = file.readlines()
    observations = list(content[0])
    states = list(content[1])
    for i in range(len(observations))[::-1]:
        if '123456'.find(observations[i]) == -1:
            del observations[i]
    for i in range(len(states))[::-1]:
        if 'FL'.find(states[i]) == -1:
            del states[i]
    start_probability = {'F': 2.0/3, 'L':1.0/3} 
    transition_probability = \
        {'F':{'F':0.95,'L':0.05},'L':{'F':0.1,'L':0.9}}
    emission_probability = \
        {'F':{'1':1.0/6,'2':1.0/6,'3':1.0/6,'4':1.0/6,'5':1.0/6,'6':1.0/6},\
        'L':{'1':0.1,'2':0.1,'3':0.1,'4':0.1,'5':0.1,'6':0.5}}
    (prob, path) = viterbi(observations, states, start_probability, \
        transition_probability,    emission_probability)
    (prob_reversed, path_reversed) = viterbi(observations[::-1], states, \
        start_probability, transition_probability,    emission_probability)
    print "Viterbi Pfad der Sequenz:\n"+''.join(path)
    print "Viterbi Pfad der umgedrehten Sequenz:\n"+''.join(path_reversed)
