import math
import pygame
import numpy as np
from pygame.locals import *
from sys import exit

pygame.init() # Inicializa funções e variáveis do módulo pygame
WIN = (800,640) #Dimensões da tela do jogo(x,y)
FPS = pygame.time.Clock()
acceleration = False

screen = pygame.display.set_mode((WIN)) #Inicializa a tela
pygame.display.set_caption('AERO PENDULO') #Define o titulo da aplicação
base = pygame.image.load('base.jpg').convert_alpha()    
base = pygame.transform.scale(base, (WIN))


home = (WIN[0]/2, 100) # Ponto de apoio do pendulo

kp = 0.800790963328250
ki = 23.210845838850050
kd = 0.006906966805523

Black = (0,0,0)
Green = (0,128,0)
Red = (205,0,20)
Gray = (150, 150, 150)

def f(t, x, u):
# State vector
# x = [x2 x1]^T
    x1 = x[0]
    x2 = x[1]
    l1 =.75
    l2 = 1.2
    J = 1e-2
    p = 0.85*9.81
    ua = .1
    x_dot = np.array( [0 + x2, (((10)*((-p*l1/J)*np.sin(x1) + (-ua/J)*x2 + (l2/J)*u))) ], dtype='float64')

    return x_dot

# Runge Kutta de 4ª órdem
def rk4(tk, h, xk, uk):
    #xk = xk.reshape([2,1])
    #uk = uk.reshape([1,1])
    k1 = f(tk , xk , uk)
    k2 = f(tk + h/2.0, xk + h*k1/2.0, uk)
    k3 = f(tk + h/2.0, xk + h*k2/2.0, uk)
    k4 = f(tk + h , xk + h*k3 , uk)
    xkp1 = xk + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)
    return xkp1 #.reshape([2,])

def simulacao():
    
    
    # PARÂMETROS DE SIMULAÇÃO
    ek_1 = 0
    h = 1e-4 # Sample time
    t = np.arange(0,5,h) # vetor tempo
    tam = len(t)
    # Vetor de estados
    x = np.zeros([2, tam],dtype='float64')
    e = np.zeros([tam],dtype='float64')
    # x[:,0] = np.array([20*np.pi/180.,0]) # Condição Inicial

    # Determinar um valor para a força de controle de equilíbrio
    l1 =.75
    l2 = 1.2
    J = 1e-2
    p = 0.85*9.81
    u_eq = 0.2*np.sin(30*np.pi/180)*p*l1/l2
    # Vetor de entrada
    u = u_eq*np.ones([tam],dtype='float64')


    # Execução da simulação
    for k in range(tam-1):
        
        # Atualização do estado
        e[k] = u_eq - x[0][k]
        u[k] = kp*e[k] + ki*(e[k] + ek_1) + kd*(e[k] - ek_1) + u_eq
        ek_1 = e[k]
        x[:,k+1] = rk4(t[k], h, x[:,k], (u[k]))
    
    return t,x

class pendulum():
   
    def __init__(self, XY):
        self.x = XY[0]
        self.y = XY[1]
        self.length = 1.2*300
        self.radius = 20
        
    def draw(self, screen):
        pygame.draw.circle(screen, Green, (WIN[0]/2, home[1]), 4)
        pygame.draw.line(screen, Green,home, (self.x, self.y))
        pygame.draw.circle(screen, Green, (self.x, self.y), self.radius)
        pygame.draw.circle(screen, Gray, (self.x, self.y), self.radius-2)

def fundo():
    screen.blit(base, (0,0))
    

def redraw():
    fundo()
    pendulo.draw(screen)

def angle():
    angle = math.asin((pendulum.x - 800/2)/ 600)
    return (angle)

def get_position(x):
    pendulo.x = round(home[0] + pendulo.length*math.sin(x))
    pendulo.y = round(home[1] + pendulo.length*math.cos(x))


t,x = simulacao()
i=0
pendulo = pendulum((400,300))

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()   
            
            
    get_position(x[0,i])
    i+=1
    redraw()           
    
    pygame.display.update()