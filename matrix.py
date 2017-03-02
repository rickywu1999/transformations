import math


def print_matrix( matrix ):
    for row in matrix:
        s = ""
        for a in row:
            s += str(a) + " "
        print(s)

def ident( matrix ):
    for a in range(len(matrix)):
        for b in range(len(matrix[0])):
            if a == b:
                matrix[a][b] = 1
            else:
                matrix[a][b] = 0

def scalar_mult( matrix, s ):
    for row in matrix:
        for a in row:
            a *= s

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m = new_matrix (len(m1),len(m2[0]))
    for a in range(len(m1)):
        for d in range(len(m2[0])):
            for c in range(len(m2)):
                m[a][d] += m1[a][c] * m2[c][d]
    return m



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
