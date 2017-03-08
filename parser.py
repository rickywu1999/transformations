from display import *
from matrix import *
from draw import *
import time

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 translate: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    fd = open(fname,'r')
    data = (fd.read()).splitlines()
    i = 0
    ident(transform)
    while i < len(data):
        if data[i] == "ident":
            ident(transform)
        if data[i] == "clear":
            points = []
        if data[i] == "line":
            i += 1
            a = data[i].split(" ")
            if len(a) != 6:
                print("Not enough data: line " + str(i))
                break
            add_edge(points,float(a[0]),float(a[1]),float(a[2]),float(a[3]),float(a[4]),float(a[5]))
        if data[i] == "scale":
            i += 1
            a = data[i].split(" ")
            if len(a) != 3:
                print("Not enough data: line " + str(i))
                break
            m = make_scale(float(a[0]),float(a[1]),float(a[2]))
            matrix_mult(m,transform)
        if data[i] == "move":
            i += 1
            a = data[i].split(" ")
            if len(a) != 3:
                print("Not enough data: line " + str(i))
                break
            m = make_translate(float(a[0]),float(a[1]),float(a[2]))
            matrix_mult(m,transform)
        if data[i] == "rotate":
            i += 1
            a = data[i].split(" ")
            if len(a) != 2:
                print("Not enough data: line " + str(i))
                break
            if a[0] == "x":
                m = make_rotX(float(a[1]))
            if a[0] == "y":
                m = make_rotY(float(a[1]))
            if a[0] == "z":
                m = make_rotZ(float(a[1]))
            matrix_mult(m,transform)
        if data[i] == "apply":
            matrix_mult(transform,points)
        if data[i] == "display":
            draw_lines(points,screen,color)
            display(screen)
            time.sleep(.1)
        if data[i] == "save":
            draw_lines(points,screen,color)
            i += 1
            a = data[i].split(".")
            if len(a) != 2:
                print("Not enough data: line " + str(i))
                break
            save_ppm(screen,data[i])
            save_extension(screen,a[0])
        i+=1

























