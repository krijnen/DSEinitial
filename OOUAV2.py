# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 12:38:37 2015

@author: Hielke
"""
from math import *
import numpy as np
import matplotlib.pyplot as plt


def main():
    a1 = design1()    
    a12 = design1_2()
    a2 = design2()
    #a2.rho = 1.225    
    #print (mindrag(a1), mindrag(a12), mindrag(a2,1))
    #print (a1.cg(), a12.cg(), a2.cg())
    print (mindrag(a2,1))
    #print (a2.cg())
    #print (a2.cg())
    #a2.setV(40)
    #print (a1.cg())
    #print (a2.cruise()[3])
    #print (a2.wings[1].Cl)    
    #mindrag(a2,1)
    #print (a1.cruise()[4])
    
    #print (a2.staticstability(1))
    #print ("tail ",taillocation(a2))
    #print (round(a1.weight()), round(a12.weight()), round(a2.weight()))    
    #print (round(a2.weight()))
    #print (round(a2.wings[0].weight))
    #print (round(a2.power()),round(a2.power()/4))
    #a2.setV(30)
    #print (round(a2.cruise()[3]))
    #print (a2.wings[0].S)
    #print (a2.wings[0].Cl)
    #print (round (a2.weight()/9.81),round((a2.W-a2.weight())/9.81))
    
def design1():                  #2 engine tiltrotor, 
    rotors = []
    engine1 = engine(312, (-2.5,13,-1),1400)           #mass, cg, power(kw)
    engine2 = engine(312, (-2.5,-13,-1),1400)
    engine3 = engine(200, (-9,0, 0),300)
    rotors.append(rotor(engine1,13,(-2.5,13,-0.5), 150, 0.65))    #engine, rotor diameter, cg, weight, Merit
    rotors.append(rotor(engine2,13,(-2.5,-13,-0.5), 150, 0.65))
    rotors.append(rotor(engine3,4,(-12,0,0), 75, 0.8))
    wings = []
    fueltanks  = []
    fueltanks.append(fueltank(1560,(-2.5,0,-0.5)))                #fuelmass, cg
    fuselage1 = [fuselage(2000)]
    wings.append(wing(airfoil(), (-2.50,0,-0.5),24,5))             #airfoil, cg, b, c, t/c
    wings.append(wing(airfoil(), (-15,0,0), 10,2,0.4))
    return UAV(rotors, wings, container(5000, (-2.5,0,1.25), 1.2), fueltanks, fuselage1)

def design1_2():                  #2 engine tiltrotor, 
    rotors = []
    engine1 = engine(272, (0,14,-1),1192)           #weight, cg, power(kw)
    engine2 = engine(272, (0,-14,-1),1192)
    engine3 = engine(200, (-9,0, 0),300)
    rotors.append(rotor(engine1,15.5,(0,14,-0.5), 150, 0.65))    #engine, rotor diameter, cg, weight, Merit
    rotors.append(rotor(engine2,15.5,(0,-14,-0.5), 150, 0.65))
    rotors.append(rotor(engine3,4,(-12,0,0), 75, 0.8))
    wings = []
    fueltanks  = []
    fueltanks.append(fueltank(1560,(-2,0,-0.5)))                #fuelmass, cg
    wings.append(wing(airfoil(), (-1,0,-0.5),21,5))             #airfoil, cg, b, c, t/c
    wings.append(wing(airfoil(), (-15,0,0), 10,3,0.4))
    return UAV(rotors, wings, container(5000, (-4,0,1.25), 1.2), fueltanks, [fuselage()])

def design2():
    rotors = []
    engine1 = engine(207, (-1.5,14,-1), 400)
    engine2 = engine(207, (-1.5,-14,-1), 400)
    engine3 = engine(207, (-17,-10,-1), 400)
    engine4 = engine(207, (-17,10,-1), 400)
    rotors.append(rotor(engine1, 12,engine1.cg, 120, 0.65))
    rotors.append(rotor(engine2, 12,engine2.cg, 120, 0.65))
    rotors.append(rotor(engine3, 12,engine3.cg, 120, 0.65))
    rotors.append(rotor(engine4, 12,engine4.cg, 120, 0.65))
    wings = []
    fueltanks = []
    wings.append(wing(airfoil(), (-1.5,0,-1), 20,3))
    wings.append(wing(airfoil(),(-15,0,-3), 20,3))
    fueltanks.append(fueltank(900,(0,0,-1)))
    fueltanks.append(fueltank(660,(-15,0,-3)))
    return UAV(rotors, wings, container(5000, (-8.5,0,1.25),1.2), fueltanks, [fuselage()],95000)

class UAV(object):              #rotors(engine), wings(airfoil), container, fueltanks
    def __init__(self, rotors, wings, container, fueltanks, fuselage, MTOW = 120000.):
        self.container = container
        self.weights(MTOW)
        self.atmosphere()
        self.rotors = rotors
        self.wings = wings
        self.container = container
        self.fueltanks = fueltanks
        self.updateweight()
        self.state()
        self.fuselage = fuselage
        
    def addrotor(self,rotor):
        self.rotors.append(rotor)

    def addwing(self,wing):
        self.wings.append(wing)
    
    def setV(self, V):
        self.V = V

    def weights(self, MTOW):
        self.W = MTOW
        self.W_f = 1561*9.81 #Derived from average fuel consumption k-maxx * expected mission time
        self.W_payload = self.container.weight
        self.W_empty = self.W - self.W_f - self.W_payload
        self.N = 3
        self.W_wing = 0  
    
    def updateweight(self):
        for wing in self.wings:
            self.W_wing += wing.wingweight(self)
            #print (wing.weight)

    def takeoff(self):
        T = 0
        for i in self.rotors: T += i.st_thrust(self)
        self.z__ = (T - self.W)/self.W*9.81         #a = (T-W)/ m
        if self.z__ >0: print("TAKEOFF!!!")

    def cruise(self):
        cg = self.cg()[0]
        W = self.W
        ac1 = cg - self.wings[0].location[0]       
        ac2 = self.wings[1].location[0] -cg
        l2 = ac1 * self.W / (ac1 + ac2)
        l1 = W - l2        
        self.wings[0].cl_l(self, l1)
        self.wings[1].cl_l(self, l2)
        D1 = self.wings[0].drag(self)
        D2 = self.wings[1].drag(self)
        D3 = self.container.drag(self)
        self.D = D1+D2+D3
        #print (l2)
        return D1, D2, D3, D1+D2+D3, (D1+D2+D3)*self.V/1000
    
  
    def climb(self):
        drag = self.cruise()[3]
        prop = 0.7
        power = 0
        for i in self.rotors: power += i.engine.power
        power  = power *1000 #watt
        rc = prop * power/self.W - drag/self.W * self.V
        return rc
        
             
    def staticstability(self, out = 0):
        tl = 0        
        while self.Mx() < 0:
            tl = self.rotors[2].tl
            self.rotors[2].set_thrust(tl-.05)
            if self.rotors[3]: self.rotors[3].set_thrust(tl-.05)                       
        if out == 1: print (tl,"      ", self.Mx())
        while self.Mx() > 0:
            tl = self.rotors[2].tl
            self.rotors[2].set_thrust(tl+.0005)
            if self.rotors[3]: self.rotors[3].set_thrust(tl+.0005)              
        if out == 1: print (tl,"      ", self.Mx())
        return tl
        
    def weight(self):
        w = self.container.weight
        for i in self.rotors: w += i.weight + i.engine.weight
        for i in self.fueltanks: w += i.weight
        for i in self.wings: w += i.weight
        for i in self.fuselage: w+= i.weight
        return w

    def cg(self):
        w = self.weight()
        cg = [0,0,0]
        for n in range (0,3):
            x = self.container.cg[n] * self.container.weight
            for i in self.rotors: x += (i.location[n] * i.weight + i.engine.cg[n] * i.engine.weight)
            for i in self.fueltanks: x += i.cg[n] * i.weight
            for i in self.wings: x += i.location[n] * i.weight
            for i in self.fuselage: x += i.cg[n] * i.weight
            cg[n] = x/w
        return cg

    def Mx(self):
        Mx = -self.W * self.cg()[0]
        for i in self.rotors: Mx += i.st_thrust(self) * i.location[0]    
        return Mx

    def atmosphere(self):
        self.rho = 1.1      

        
    def state(self):
        self.x = 0
        self.y = 0
        self.z = 0        
        self.x_ = 0
        self.y_ = 0
        self.z_ = 0
        self.x__ = 0
        self.y__ = 0
        self.z__ = 0
        self.V = 0    
            
    def diskloading(self):
        a_rotors = 0
        for x in self.rotors: a_rotors+= (x.diameter/2)**2*pi
        return self.W/a_rotors
    
    def power(self):
        Merit = 0.7
        return (self.W*1.2*sqrt(self.diskloading()/2/self.rho)/Merit)/1000
    
class rotor(object):            #engine, diameter, location, mass, merit, thrustlv; Functions: st_thrust(a), set_thrust(tl), tilt(dtetha)
    def __init__(self, engine, diameter = 1, location = (0,0,0), mass = 200, merit = 0.7, thrustlv = 1):         #DOF, Angle, Angle adjustment speed
        self.diameter = diameter
        self.location = location
        self.merit = merit
        self.tl = thrustlv
        self.weight = mass *9.81
        self.mass = mass
        self.engine = engine
        self.theta = 0
        self.beta = 0

    def tilt(self, dtheta, dbeta):
        self.theta += dtheta
        self.beta += dbeta

    def st_thrust(self, a):
        #v = 1
        v = (self.merit * self.tl * self.engine.power *1000 /(pi*(self.diameter/2.))**2*a.rho)**(1./3)
        m = v * a.rho * (pi*(self.diameter/2.))**2
        #m = 1
        #print (m*v)
        return m*v

    def set_thrust(self, tl):
        self.tl = tl

class wing(object):             #airfoil, location, b, c, t_c, labda, Labda, e ; Functions: setlocation(location), wingloading(weight), lift(self, a, cl), drag(a), cl_l(a,L)
    def __init__(self, airfoil, location = (0,0,0), b = 28, c = 5, t_c =.23, Labda =0, labda= 1,  e = 0.85):
        self.e = e
        self.b = b
        self.c = c
        self.S = self.b*self.c        
        self.labda = labda  #taper
        self.Labda = Labda  #sweep
        self.A = self.b/self.c
        self.t_c = t_c
        self.location = location
        self.airfoil = airfoil               # weight, inertia,
        self.Cl = self.airfoil.cl_max
        self.weight = 0
        self.mass = 0


    def setlocation(self, location):
        self.location = location
    
    def wingloading(self, weight):
        return weight/self.S

    def lift(self, a, cl): #a = uav
        return 0.5*a.rho*a.V**2*self.S*cl

    def drag(self, a):
        Cd = self.airfoil.Cd0 + self.Cl**2/pi/self.A/self.e
        return 0.5*a.rho*a.V**2*self.S*Cd

    def cl_l(self,a, L):
        self.Cl = L/(0.5*a.rho*a.V**2 * self.S)
        #print (self.Cl)
        return self.Cl

    def wingweight(self,a):
        self.mass = a.W_empty/9.81*0.0017*a.N**(0.55)*self.t_c**(-0.3)*(self.b/cos(self.Labda))**(1.05)*(1+sqrt(6.25*cos(self.Labda)/self.b))*(a.W_empty/9.81/self.S)**(-0.3)
        self.weight = 9.81 * self.mass
        return self.weight
        #return 0.0051*(self.EW* self.N)**(0.557)*self.S_wing**0.649*self.A_wing**0.5*self.t_c**(-0.4)*(1+self.labda)**0.1 * cos(self.Labda)**(-1.0)*(self.S_wing*0.05)**0.1

class airfoil(object):          #Cd0, cl_max, cl_0; Functions: Cl_lvl(a, wing), Cl_alpha(a)
    def __init__(self, Cd0 = 0.315, cl_max = 1.5, cl_0 = 0):
        self.Cd0 = .03
        self.cl_max = 1.5
        self.cl_0 = cl_0        
    def Cl_lvl(self, a,wing):
       return a.W / 0.5/a.rho/a.V**2/wing.S
    def Cl_alpha(self, a):
        return self.cl_0 + 2*pi*a.alpha
        
class fuselage(object):
    def __init__(self, mass = 2000, cg = (0,0,0), cd = 0.6, A = 3*3):
        self.mass = mass
        self.weight = mass*9.81
        self.cg = cg
        self.cd = cd
        self.A = A
    
    def drag(self, a):
        return 0.5*a.rho*a.V**2*self.A*self.cd
        
    

class container(object):        #mass, cg, cd ; Functions: drag(a)
    def __init__(self, mass = 5000, cg = (0,0,0), cd = 2):
        self.cg = cg
        self.cd = cd
        self.mass = mass
        self.weight = mass *9.81
    def drag(self, a):
        return 0.5*a.rho*a.V**2*(2.5*2.5)*self.cd
    def setcg(self, cg):
        self.cg = cg

class fueltank(object):         #mass, cg ; Functions: usefuel(amount)
    def __init__(self, mass = 1560, cg =(0,0,0), emptymass = 10):
        self.weight = mass * 9.81
        self.mass = mass
        self.cg = cg
        self.empty = False
        
    def usefuel(self, amount):      #amount in kg
        self.mass = self.mass - amount
        if self.mass < emptymass:
            self.mass = emptymass
            self.empty = True
        self.weight = self.mass * 9.81
        
        #cg?

class engine(object):           #mass, cg, power(kw)
    def __init__(self, mass= 200, cg = (0,0,0), power = 200):
        self.mass = mass
        self.weight = 9.81*mass
        self.cg = cg
        self.power = power

def test():
    a = design1()
   # print (a.Mx())    
    #a.staticstability()
    #a.takeoff()
    #print (a.z__)
    #print (a.cg())
    #print ("lift= ",a.cruise(), "   weight= ", a.W)
    #print (a.rotors[2].tl)
    #print (a.power())
    #for l in a.rotors: print( l.st_thrust(a))
   #print (a.wingweight()) 
   # print (a.W_f/9.81)
   # print (a.W * 1.2)
    #print (a.drag(35))
    #for i in range(1,5):
    #    a.W_0()
    #    print (a.W0)
    #print (sqrt(14.5**2+16.5**2))
    #r= [8,8,3]
    #a.setrotors(r)
    #print (a.diskloading())
    #print (a.power())
    #print (a.A_wing)    
    #print (a.drag())
    #print(120000*1.1*sqrt(a1.diskloading()/2/1.225)/0.7/1000)
    #a.takeoff()
    #mindrag(a1)    
    #a2 = design2()
    #print(a1.rotors[0].st_thrust(a1))
    #a1.setV(35)
    #print(a1.rotors[0].st_thrust(a1))
    #print (a1.cruise())
    #a.takeoff()
    #taillocation(a1)
    #print(a1.cg())
    #print(a1.wings[1].weight)
    
    #taillocation(a2)
    #mindrag(a2)
    #print (" ")
    #print (a1.W_wing, a2.W_wing)
    #print (a1.cg(), a2.cg())

def taillocation(a, x=0):
    vmax, d, cl, tail = [],[],[],[]
    for i in range(-300,-50):
        a.wings[1].setlocation((i/10.,0,0))
        x = mindrag(a)
        vmax.append(x[0])
        d.append(x[1])
        cl.append(x[2])
        tail.append(i/10.)
    if x==1:
        plt.plot(tail, vmax)
        plt.show()
        plt.plot(tail, d)
        plt.show()
        plt.show(tail, cl)
        plt.show()
    return tail[(d.index(min(d)))], min(d)
    #print (cl)
    
def mindrag(a, x = 0):
    V,d1,d2,d3,d4, cl1, cl2, pr, rc = [],[],[],[],[],[],[],[],[]
    for i in range (20,60):
        a.setV(i)
        c=a.cruise()
        d1.append(c[0])
        d2.append(c[1])
        d3.append(c[2])
        d4.append(c[3])
        V.append(i)
        cl1.append(a.wings[0].Cl)
        cl2.append(a.wings[1].Cl)
        pr.append(c[4])
        rc.append(a.climb())
    if x == 1:
        plt.plot(V,d1,color = "blue")
        plt.plot(V,d2,color = "red")
        plt.plot(V,d3,color = "green")
        plt.plot(V,d4,color = "purple")
        plt.show()
        plt.plot(V, cl1, color = "blue")
        plt.plot(V, cl2, color = "red")
        plt.show()
        plt.plot(V, pr, color = "purple")
        plt.show()
        plt.plot(V, rc, color = "green")
        plt.show()
        print ("Min:", V[(d4.index(min(d4)))], " m/s",  '{0:.3g}'.format(min(d4)), " N", min(pr), "kW")
        #print (pr)
    return V[(d4.index(min(d4)))], min(d4), cl1[(d4.index(min(d4)))], min(pr)




if __name__ == "__main__":
    main()