from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math
import random

import pygame


from pygame.locals import *



def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-500,500.0,-500,500.0)

def plotaxes():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_LINES)
    glVertex2f(0,-500)
    glVertex2f(0,500)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(500,0)
    glVertex2f(-500,0)
    glEnd()

def triplotaxes():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.184314,0.309804,0.309804)
    glBegin(GL_LINES)
    glVertex3f(0,-3,0)
    glVertex3f(0,3,0)
    glEnd()
    glBegin(GL_LINES)
    glVertex3f(3,0,0)
    glVertex3f(-3,0,0)
    glEnd()
    glBegin(GL_LINES)
    glVertex3f(0,0,3)
    glVertex3f(0,0,-3)
    glEnd()

def plotgrid():
    glColor3f(0.202, 0.202, 0.202)
    for i in range(-500,500,50):
        if i != 0:
            glBegin(GL_LINES)
            glVertex2f(i,500)
            glVertex2f(i,-500)
            glEnd()
            glBegin(GL_LINES)
            glVertex2f(500,i)
            glVertex2f(-500,i)
            glEnd()
        # glBegin(GL_LINES)
        # glVertex2f(-100,x)
        # glVertex2f(100,x)
        # glEnd()



    
def fan(lista):
    
    #x=int(0)
    #y=int(0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,len(lista),1):
        
        glVertex2f(lista[i][0],lista[i][1])
    glEnd()

    
def aristas(lista):
    glBegin(GL_LINES)
    for i in range(0,len(lista),1):
        
        glVertex2f(lista[0][0],lista[0][1])
        glVertex2f(lista[i][0],lista[i][1])
    glEnd()


def fancom(lista):
    plotaxes()
    plotgrid()
    glColor3f(0, 0, 1)
    fan(lista)
    glColor3f(0, 1, 1)
    aristas(lista)
    glFlush()

def pfan(lista):
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("TRIANGLE FAN DELUXE FFM-Ver2.5")
    glutDisplayFunc(lambda: fancom(lista))
    init()
    glutMainLoop()

        




def drawTranslated(lista,tx,ty,tresde):
    
    newpoints=[]
    for i in lista:
        newpoints.append([i[0]+tx,i[1]+ty])
    print(newpoints)

    if tresde=="si":
        main3d(newpoints)
    else:
        
        plotaxes()
        plotgrid()

        glColor3f(0.8, 0.8, 0.8)
        fan(lista)
        glColor3f(0, 1, 1)
        aristas(lista)
    
        glColor3f(1, 0.5, 0)
        fan(newpoints)
        glColor3f(0.5, 1, 0.5)
        aristas(newpoints)
        glFlush()
    
def drawScaled(lista,tx,ty,tresde):
    
    newpoints=[]
    for i in lista:
        newpoints.append([i[0]*tx,i[1]*ty])
    print(newpoints)

    if tresde=="si":
        main3d(newpoints)
    else:
        
        plotaxes()
        plotgrid()

        glColor3f(0.8, 0.8, 0.8)
        fan(lista)
        glColor3f(0, 1, 1)
        aristas(lista)
    
        glColor3f(1, 0.5, 0)
        fan(newpoints)
        glColor3f(0.5, 1, 0.5)
        aristas(newpoints)
        glFlush()

def drawReflected(lista,op,tresde):

    newpoints=[]
    for i in lista:
        if(op==1):
            newpoints.append([i[0], -i[1]])
        elif(op==2):
            newpoints.append([-i[0], i[1]])
        elif(op==3):
            newpoints.append([-i[0], -i[1]])
        elif(op==4):
            newpoints.append([i[1], i[0]])
        elif(op==5):
            newpoints.append([-i[1], -i[0]])

        
    if tresde=="si":
        main3d(newpoints)
    else:
        
        plotaxes()
        plotgrid()

        glColor3f(0.8, 0.8, 0.8)
        fan(lista)
        glColor3f(0, 1, 1)
        aristas(lista)
    
        glColor3f(1, 0.5, 0)
        fan(newpoints)
        glColor3f(0.5, 1, 0.5)
        aristas(newpoints)
        glFlush()

def drawRotated(lista,theta,tresde):

    newpoints=[]
    for i in lista:
        newpoints.append([round(i[0]* math.cos(theta) - i[1] * math.sin(theta)), round(i[0] * math.sin(theta) + i[1] * math.cos(theta))])
    print(newpoints)

    if tresde=="si":
        main3d(newpoints)
    else:
        
        plotaxes()
        plotgrid()

        glColor3f(0.8, 0.8, 0.8)
        fan(lista)
        glColor3f(0, 1, 1)
        aristas(lista)
    
        glColor3f(1, 0.5, 0)
        fan(newpoints)
        glColor3f(0.5, 1, 0.5)
        aristas(newpoints)
        glFlush()

def rotate(lista):
    theta= (math.pi/180) * float(input("\nGrados en sexagesimal(360°): "))
    tresde=str(input("Desea graficar en 3d? si/no "))
    if tresde=="no":
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(50,50)
        glutCreateWindow("TRIANGLE FAN DELUXE FFM-Ver2.5")
        glutDisplayFunc(lambda: drawRotated(lista,theta,tresde))
        init()
        glutMainLoop()
    else:
        drawRotated(lista,theta,tresde)
        
def scale(lista):
    tx= int(input("\nIndique un escalar para x: "))
    ty= int(input("\nIndique un escalar para y: "))
    tresde=str(input("Desea graficar en 3d? si/no "))
    if tresde=="no":
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(50,50)
        glutCreateWindow("TRIANGLE FAN DELUXE FFM-Ver2.5")
        glutDisplayFunc(lambda: drawScaled(lista,tx,ty,tresde))
        init()
        glutMainLoop()
    else:
        drawScaled(lista,tx,ty,tresde)
        

def reflect(lista):
    print("Seleccione su tipo de reflexion: ")
    op = int(input("1.Reflexion respecto al eje x\n2. Reflexion respecto al eje y\n3.Reflexion respecto al origen\n4.Reflexion diagonal respecto a la linea x=y \n5. Reflexion diagonal respecto a la linea x=-y \n"))
    tresde=str(input("Desea graficar en 3d? si/no "))
    if tresde=="no":
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(50,50)
        glutCreateWindow("TRIANGLE FAN DELUXE FFM-Ver2.5")
        glutDisplayFunc(lambda: drawReflected(lista,op,tresde))
        init()
        glutMainLoop()
    else:
        drawReflected(lista,op,tresde)
        

def translate(lista):
    
    tx=int(input("\n translacion en x: "))
    ty=int(input("\n translacion en y: "))
    tresde=str(input("Desea graficar en 3d? si/no "))
    if tresde=="no":
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(50,50)
        glutCreateWindow("TRIANGLE FAN DELUXE FFM-Ver2.5")
        glutDisplayFunc(lambda: drawTranslated(lista,tx,ty,tresde))
        init()
        glutMainLoop()
    else:
        drawTranslated(lista,tx,ty,tresde)

def trd(lista,z):

    lista3d0=[]
    lista3d1=[]
    for i in lista:
        lista3d0.append([i[0]/50,i[1]/50,0])
        lista3d1.append([i[0]/50,i[1]/50,z])
    
    #glColor3f(1, 0.5, 0) naranjo
    glBegin(GL_LINES)#lados 
    glColor3f(0, 1, 0)#rojo
    for i in range(0,len(lista)-1,1):
        glVertex3f(lista3d0[i][0],lista3d0[i][1],lista3d0[i][2])
        glVertex3f(lista3d1[i][0],lista3d1[i][1],lista3d1[i][2])
        glVertex3f(lista3d0[i+1][0],lista3d0[i+1][1],lista3d0[i+1][2])
        glVertex3f(lista3d1[i+1][0],lista3d1[i+1][1],lista3d1[i+1][2])
    glEnd()
    #caras
    glBegin(GL_LINES)
    glColor3f(0, 1, 0)
    for i in range(0,len(lista)-1,1):
        
        glVertex3f(lista[i][0]/50,lista[i][1]/50,0)
        glVertex3f(lista[i+1][0]/50,lista[i+1][1]/50,0)
    glVertex3f(lista[-1][0]/50,lista[-1][1]/50,0)
    glVertex3f(lista[0][0]/50,lista[0][1]/50,0)
    glEnd()
    
    glColor3f(0, 1, 0)#verde
    glBegin(GL_LINES)
    for i in range(0,len(lista)-1,1):
        glVertex3f(lista[i][0]/50,lista[i][1]/50,z)
        glVertex3f(lista[i+1][0]/50,lista[i+1][1]/50,z)
    glVertex3f(lista[-1][0]/50,lista[-1][1]/50,z)
    glVertex3f(lista[0][0]/50,lista[0][1]/50,z)
    glEnd()

    
    glBegin(GL_LINES)
    glColor3f(0, 1, 0)
    for i in range(0,len(lista),1):
        
        glVertex3f(lista[i][0]/50,lista[i][1]/50,0)
    glEnd()

def ask(lista):
    op3d=str(input("desea graficar en 3d? si/no "))
    if op3d=="si":
        main3d(lista)
    else:
        print("proyectando en 2d...")
def main3d(lista):
    
    z=int(input("Ingrese la profundidad z: "))

    pygame.init()
    display = (1280,720)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(150, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(-6,-4, -6)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        triplotaxes()
        trd(lista,z)
        pygame.display.flip()
        pygame.time.wait(10)

def main():
    print("\n----------------------------------------")
    print("----------TRIANGLE FAN DELUXE-----------")
    print("-----------------------------FFM-Ver2.5-")
    op0=str(input("\nDesea usar el poligono de prueba? si/no :"))

    

    
    if op0=="si":
        lista = [[50,50],[150,50],[300,150],[150,300],[50,300],[-150,150]]
        print(lista)

    else:
        print("\nIngrese coordenadas del poligono: ")
        num=int(input("Numero de vertices: "))
        lista = []
        x=int(0)
        y=int(0)
        for i in range(0,num):
            x=int(input("ingrese la x del punto "+ str(i)+" "))

            y=int(input("ingrese la y del punto "+ str(i)+" "))
            lista.append([x,y])
        print(lista)
    print("\n¿Desea aplicar una transformacion a estas coordenadas?")
    bol=str(input("\nOpcion si/no: "))
    if bol=="si":
            print("\nElija una transformacion:\n\t1.Traslacion\n\t2.Rotacion\n\t3.Escalado\n\t4.Reflexion")
            op=int(input("\nTu opcion: "))
            if op == 1:
                translate(lista)
            elif op == 2:
                rotate(lista) 
            elif op == 3:
                scale(lista)
            elif op == 4:
                reflect(lista)
    elif bol=="no":
        ask(lista)
        pfan(lista)
    else:
        print("lo tomaré como un no, proyectando figura...")
        ask(lista)
        pfan(lista)
    

main()
