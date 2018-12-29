import math
import time
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

signal_orientation = "vertical"

revolutions_per_second = 30

xgrid_verts = (
    (-4, 0, 5),
    (-4, 0, -5),
    (-3, 0, 5),
    (-3, 0, -5),
    (-2, 0, 5),
    (-2, 0, -5),
    (-1, 0, 5),
    (-1, 0, -5),
    (1, 0, 5),
    (1, 0, -5),
    (2, 0, 5),
    (2, 0, -5),
    (3, 0, 5),
    (3, 0, -5),
    (4, 0, 5),
    (4, 0, -5),
    )
ygrid_verts = (
    (5, 0, -4),
    (-5, 0, -4),
    (5, 0, -3),
    (-5, 0, -3),
    (5, 0, -2),
    (-5, 0, -2),
    (5, 0, -1),
    (-5, 0, -1),
    (5, 0, 1),
    (-5, 0, 1),
    (5, 0, 2),
    (-5, 0, 2),
    (5, 0, 3),
    (-5, 0, 3),
    (5, 0, 4),
    (-5, 0, 4)
    )
bound_verts = (
    (5, 0, 5),
    (-5, 0, 5),
    (5, 0, 5),
    (5, 0, -5),
    (-5, 0, 5),
    (-5, 0, -5),
    (5, 0, -5),
    (-5, 0, -5),
    (0,0,5),
    (0,0,-5),
    (5,0,0),
    (-5,0,0)
    )
bound_edges = (
    (0,1),
    (2,3),
    (4,5),
    (6,7),
    (8,9),
    (10,11)
    )

grid_edges = (
    (0,1),
    (2,3),
    (4,5),
    (6,7),
    (8,9),
    (10,11),
    (12,13),
    (14,15)
    )

def Signal(interval):
    

def Flash():
    if signal_orientation == "vertical":
        signal_orientation = "horizontal"
    else:
        signal_orientation = "vertical"

def Grid():
    glBegin(GL_LINES)
    for edge in bound_edges:
        for vert in edge:
            glVertex3fv(bound_verts[vert])
    glColor(0.6,0.6,0.6)
    glEnd()
    glBegin(GL_LINES)
    for edge in grid_edges:
        for vert in edge:
            glVertex3fv(xgrid_verts[vert])
    glColor((1,0,0))
    glEnd()
    glBegin(GL_LINES)
    for edge in grid_edges:
        for vert in edge:
            glVertex3fv(ygrid_verts[vert])
    glColor((0,1,0))
    glEnd()

def RenderPos():

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,-2, -15)

    orbit = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                orbit = True
            if event.type == MOUSEBUTTONUP:
                orbit = False
        if orbit:
            glRotatef(pygame.mouse.get_rel()[0], 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Grid()
        pygame.display.flip()
        pygame.time.wait(10)

main()
