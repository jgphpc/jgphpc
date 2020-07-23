def arrangliste(seq, k):
    """Liste des arrangements des objets de la liste seq pris k à k"""
    p = []
    i, imax = 0, 2**len(seq)-1
    while i<=imax:
        s = []
        j, jmax = 0, len(seq)-1
        while j<=jmax:
            if (i>>j)&1==1:
                s.append(seq[j])
            j += 1
        if len(s)==k:
            v = permutation(s)
            #v = permutliste(s)
            p.extend(v)
        i += 1
    return p

# Python function to print permutations of a given list 
def permutation(lst):
    # If lst is empty then there are no permutations 
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only 
    # one permutation is possible 
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are 
    # more than 1 characters 
    l = [] # empty list that will store current permutation 
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)):
        m = lst[i]

    # Extract lst[i] or m from the list. remLst is 
    # remaining list 
    remLst = lst[:i] + lst[i+1:]

    # Generating all permutations where m is first 
    # element 
    for p in permutation(remLst):
        l.append([m] + p)
    return l

#ok:
#from itertools import permutations
#list(permutations('abcde',2))
#print(arrangliste(['A','B','C'],2))
#print(arrangliste(['A','B','C','D','E'],1))
#print(type(arrangliste(['A','B','C','D','E'],2)))
def myprint_chf_l2(lst):
    for iii in range(len(lst)):
        print(iii,
              lst[iii][0], lst[iii][1],
              chf[lst[iii][0]], chf[lst[iii][1]],
              chf[lst[iii][0]] + chf[lst[iii][1]], # 'chf',
              (chf[lst[iii][0]] + chf[lst[iii][1]]) * .9 # -10%
              # lst[iii][0] ,'+', lst[iii][1], '=',
              # chf[lst[iii][0]], '+', chf[lst[iii][1]], '=',
              # chf[lst[iii][0]]   +  chf[lst[iii][1]], 'chf',
              # (chf[lst[iii][0]]   +  chf[lst[iii][1]]) * .9
              )
    return

def myprint_chf_l3(lst):
    for iii in range(len(lst)):
        print(iii,
              lst[iii][0], lst[iii][1], lst[iii][2],
              chf[lst[iii][0]], chf[lst[iii][1]], chf[lst[iii][2]],
              chf[lst[iii][0]] + chf[lst[iii][1]] + chf[lst[iii][2]], # 'chf',
              (chf[lst[iii][0]] + chf[lst[iii][1]] + chf[lst[iii][2]]) * .9 # -10%
              )
    return

def myprint_eur_l2(lst):
    for iii in range(len(lst)):
        print(iii,
              lst[iii][0], lst[iii][1],
              eur[lst[iii][0]], eur[lst[iii][1]],
              eur[lst[iii][0]] + eur[lst[iii][1]], # 'eur',
              (eur[lst[iii][0]] + eur[lst[iii][1]]) * .9 # -10%
              # lst[iii][0] ,'+', lst[iii][1], '=',
              # eur[lst[iii][0]], '+', eur[lst[iii][1]], '=',
              # eur[lst[iii][0]]   +  eur[lst[iii][1]], 'eur',
              # (eur[lst[iii][0]]   +  eur[lst[iii][1]]) * .9
              )
    return

def myprint_eur_l3(lst):
    for iii in range(len(lst)):
        print(iii,
              lst[iii][0], lst[iii][1], lst[iii][2],
              eur[lst[iii][0]], eur[lst[iii][1]], eur[lst[iii][2]],
              eur[lst[iii][0]] + eur[lst[iii][1]] + eur[lst[iii][2]], # 'eur',
              (eur[lst[iii][0]] + eur[lst[iii][1]] + eur[lst[iii][2]]) * .9 # -10%
              )
    return

# http://python.jpvweb.com/python/mesrecettespython/doku.php?id=arrangements
# https://docs.python.org/2/library/itertools.html#itertools.permutations
# http://math.heig-vd.ch/fr-ch/enseignement/Cours/Statistiques.pdf
if __name__ == "__main__":
    # --- CHF:
    chf = {'A': 44.5, 'B': 49.5, 'C': 59.5, 'D': 74.5, 'E': 109.5}
    #print(type(arrangliste(['A','B','C','D','E'],2)))
    l2_a = arrangliste(['A','B','C','D','E'], 2)
    l3_a = arrangliste(['A','B','C','D','E'], 3)
    #myprint_chf_l2(l2_a)
    #myprint_chf_l3(l3_a)

    # --- EUR:
    eur = {'A': 41.5, 'B': 39.5, 'C': 44.5, 'D': 59.5, 'E': 59.5}
    l2_a = arrangliste(['A','B','C','D','E'], 2)
    l3_a = arrangliste(['A','B','C','D','E'], 3)
    myprint_eur_l2(l2_a)
    myprint_eur_l3(l3_a)

# ----------------------------
#                 CHF  -10%
# 0 B A 49.5 44.5 94.0 84.6
# 1 C A 59.5 44.5 104.0 93.6
# 2 C B 59.5 49.5 109.0 98.1
# 3 D A 74.5 44.5 119.0 107.1
# 4 D B 74.5 49.5 124.0 111.6
# 5 D C 74.5 59.5 134.0 120.6
# 6 E A 109.5 44.5 154.0 138.6
# 7 E B 109.5 49.5 159.0 143.1
# 8 E C 109.5 59.5 169.0 152.1
# 9 E D 109.5 74.5 184.0 165.6
# ----------------------------
# 0 C B A 59.5 49.5 44.5 153.5 138.15
# 1 D B A 74.5 49.5 44.5 168.5 151.65
# 2 D C A 74.5 59.5 44.5 178.5 160.65
# 3 D C B 74.5 59.5 49.5 183.5 165.15
# 4 E B A 109.5 49.5 44.5 203.5 183.15
# 5 E C A 109.5 59.5 44.5 213.5 192.15
# 6 E C B 109.5 59.5 49.5 218.5 196.65
# 7 E D A 109.5 74.5 44.5 228.5 205.65
# 8 E D B 109.5 74.5 49.5 233.5 210.15
# 9 E D C 109.5 74.5 59.5 243.5 219.15
# ----------------------------
