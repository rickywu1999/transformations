import math

def make_translate( x, y, z ):
    matrix = [[1,0,0,0],
              [0,1,0,0],
              [0,0,1,0],
              [x,y,z,1]]
    return matrix

def make_scale( x, y, z ):
    matrix = [[x,0,0,0],
              [0,y,0,0],
              [0,0,z,0],
              [0,0,0,1]]
    return matrix

def make_rotX( theta ):    
    rad = theta/180.0 * math.pi
    matrix = [[1,0,0,0],
              [0,math.cos(rad),math.sin(rad),0],
              [0,math.sin(rad)*-1,math.cos(rad),0],
              [0,0,0,1]]
    return matrix

def make_rotY( theta ):
    rad = theta/180.0 * math.pi
    matrix = [[math.cos(rad),0,math.sin(rad)*-1,0],
              [0,1,0,0],
              [math.sin(rad),0,math.cos(rad),0],
              [0,0,0,1]]
    return matrix

def make_rotZ( theta ):
    rad = theta/180.0 * math.pi
    matrix = [[math.cos(rad),math.sin(rad),0,0],
              [math.sin(rad)*-1,math.cos(rad),0,0],
              [0,0,1,0],
              [0,0,0,1]]
    return matrix

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
