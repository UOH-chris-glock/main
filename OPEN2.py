from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from numpy import *
w, h = 500,500

# ---Section 1---
def polygonn():
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_POLYGON) # Begin the sketch
    for i in range(0,len(lista),2):
        glVertex2f(lista[i], lista[i+1])
    glEnd() # Mark the end of drawing


num=int(input("Numero de vertices: "))
lista = []
x=int(0)
y=int(0)
for i in range(0,num):
    x=int(input("ingrese la x del punto "+ str(i)+" "))
    lista.append(x)
    y=int(input("ingrese la y del punto "+ str(i)+" "))
    lista.append(y)
print(lista)






def iterate():
    glViewport(0, 0, 500,500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glLoadIdentity() # Reset all graphic/shape's position
    iterate()
    glColor3f(126, 161, 0) # Set the color to pink
    polygonn() # Draw a square using our function
    glutSwapBuffers()


#---Section 3---

glutInit()
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(1000, 1000)   # Set the w and h of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glutCreateWindow("OpenGL Coding Practice") # Set a window title
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen) # Keeps the window open
glutMainLoop()  # Keeps the above created window displaying/running in a loop


