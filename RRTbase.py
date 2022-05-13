from curses.textpad import rectangle
from pickle import GLOBAL
import random
import math
from tracemalloc import start
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from numpy import true_divide

class RRTmap:
    def __init__ (self,start,goal,mapdims,obsdims,obsnum):
        self.start=start

        self.goal=goal

        self.mapdims=mapdims

        self.maph,self.mapw=self.mapdims

        self.obsdims=obsdims
        self.obsnum=obsnum


        self.noderad=0
        self.nodethickness=0
        self.edgethickness=0

        self.obstacles = []



    def drawmap(self):
        startnode=plt.Circle(self.start,2,color='darkgreen')
        goalnode=plt.Circle(self.goal,2,color='red')
        self.ax.draw_patch(startnode)
        self.ax.draw_patch(goalnode)


    def drawpath(self):

    def drawobj(self):



class RRTgraph:
    def__init__(self,start,goal,mapdims,obsdims,obsnum):
        (x,y)=start
        self.start=start
        self.goal=goal 
        self.goalflag=False
        self.maph , self.mapw =mapdims
        self.x=x
        self.y=y
        self.parent=parent 
#initialize the tree
        self.x.append(x)
        self.y.append(y)
        self.parent.append(0)
#the obstacles
        self.obstacles=[]


#path
        self.goalstate = None
        self.path=[]



    def makeobs(self):
        obs= [[(40,0),(40,40),(50,50),(60,40),(50,40)],
        [(10,10),(20,20),(10,30),(0,20)],
        [(50,60),(70,80),(60,100),(40,80),(45,100)],
        [(70,20),(90,20),(80,40)],[(30,40),(40,50),(50,60),(70,75),(80,45)]]

        polygon= [Polygon(obstacles[i]) for i in range ]

        graph.dr


    def addnode(self):
    
        


    def remnode(self):            
        pass


    def addedge(self):
        pass


    def remedge(self):
        pass


    def num_of_nodes(self):            
        return len()


    def distance(self):


    def nearest(self):


    def isfree(self):


    def crossobs(self):

    def connect(self):


    def step(self):


    def path_to_goal(self):


    def getpathcoords(self):


    def bias(self):


    def expand(self):


    def cost(self):

