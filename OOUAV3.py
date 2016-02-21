# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 12:38:37 2015

@author: Hielke
"""
from math import *
import numpy as np
import matplotlib.pyplot as plt


def main():
    #test()
    
    a1 = design1()    
    a12 = design1_2()
    a2 = design2()
    a22 = design2_3()
    
    
    #print(taillocation(a1,1))
    #a1.container.empty()
    #mindrag(a1,1)
    #print(taillocation(a1,1))
    #fuelest(a1)
    #print("DRAGON FLY")
    #print(a1.cruisespeed())
    #print(a1.cruiseperformance()[-2])
    #print(a1.mission()[1]/3600)
    #print(a1.maxclimb())
   # print(a22.cruisespeed())
   # print(a22.cruiseperformance()[-1],'kw')
    #a1.container.empty()#
    #print(a22.cruiseperformance())
    #print (a22.maxclimb(), "m/s")
    #print (a22.cruisespeed(), "m/s")    
    #print(a22.weight())
    #print (a1.weight())
    #print (a1.cruisespeed())
    #print (a1.cruiseperformance()[-2])
    #climb, rho = [],[]
    
    #for i in range (10, 123):
    #    a1.rho = i/100.
    #    rho.append(a1.rho)
    #plt.plot(rho,climb)
    #plt.show()
    
    #print (a22.cruiseperformance())
    #print (a2.range(), "km")
    #print (a22.range(), "km")
    #payloadrange(a1)
    #print(fuelest(a22))
    #a22.updateweight()
    #print(a22.fueltanks[0].weight)
    #payloadrange(a22, 'Locust')  
   # 
    print(fuelest(a1), 'kg')
    a1.updateweight()
    fuelest(a1)
    a1.updateweight()
    #mindrag(a1,1, "Dragonfly")
    chordlength(a1, "Dragonfly")
#    a1.rho = 1.056
#    mindrag(a1, 1, 'Dragonfly')
    #print (a22.maxclimb())
    #print(a1.fueltanks[0].weight)
######################################################    
    fuelest(a22)
    a22.updateweight()    
    print(fuelest(a22), 'kg')
    a22.updateweight()
    a22.fueltanks[0].usefuel(40)
    chordlength(a22, "Locust")
    #payloadrange(a22, "Locust")    
    #a22.container.empty()
    #print(a22.cruisespeed())
    #print(a22.maxclimb())
    #print(a22.weight())
   # a1.staticstability(1)
    #a1.container.empty()
   # a1.staticstability(1)
    
    #payloadrange(a1, 'Dragonfly')  
    #mindrag(a1,1, '')
    
    
    
 #   print (a1.weight())
    #print("LOCUST")
    #print(fuelest(a22),"kg")
    #a22.updateweight()
     #print(a22.weight(),"N")
    #a1.container.empty()
 #   print (a1.maxclimb())
 #   print (a1.cruisespeed())
    #a1.cruisespeed()
#    print (a1.setV(40))
 #   print (a1.cruiseperformance()[-1]/0.8)
    #print(a22.cruisespeed(), "m/s")
    #print(chordlength(a1, 'Dragonfly'))
    #print(a22.cruiseperformance()[-2], "N")
    #print(a22.mission()[1]/3600, "s")
    #print(a22.maxclimb(),"m/s")
    #mindrag(a22, 1, 'Locust')
    #mindrag(a1,1)
    

    
 #   payloadrange(a1, 'Dragonfly')
    #payloadrange(a22, 'Locust')
    #print(a1.staticstability())
    #print((a1.weight()*1.1-a1.staticstability()[1])/2)
    #print(6500*9.81)
    #print (a22.wings[1].weight/9.81)
    #print (a22.wings[0].weight/9.81)
    #print (6500/11.)
    #print (a22.range())    
    #clcdplot(a22)
    #a2.rho = 1.225     
    #print (mindrag(a1), mindrag(a12), mindrag(a2,1))
    #print (a1.cg(), a12.cg(), a2.cg())
    #mindrag(a22,1)
    #mindrag(a1,1)
    #print (a1.weight())
    #print (a1.wingloading())
    #a1.container.empty()
    #mindrag(a1,1)
    #print (a1.wingloading())
    
    #print(a1.weight())
    #a1.container.empty()
    #mindrag(a1,1)
    #print (a2.weight())

def design1():                  #2 engine tiltrotor,  Turboshaft
    rotors = []
    engine1 = engine(200, (-2.5,13,-1),1815)           #mass, cg, power(kw)
    engine2 = engine(200, (-2.5,-13,-1),1815)
    engine3 = engine(135, (-12,0, 0), 300)               # tesla
    rotors.append(rotor(engine1,16,(-2.5,13,-0.5), 150, 0.65))    #engine, rotor diameter, cg, weight, Merit
    rotors.append(rotor(engine2,16,(-2.5,-13,-0.5), 150, 0.65))
    rotors.append(rotor(engine3,2,(-15,0,0), 75, 0.8, False))
    airfoil1 = airfoil(0.008, 2.5, 1, (0.28,0,0), 0.119/180*pi, -0.0035/180*pi )  #Cd0, cl_max, cl_0, ac, cl_alfa, cm_alfa
    airfoil2 = airfoil(0.006, 1.5, 0.32, (0.267,0,0), 0.1175/180*pi, -0.0015/180*pi )
    airfoil3 = airfoil(0.004, 2, 1.2, (0.34,0,0), 0.1175/180*pi, -0.0035/180*pi )    
    wings = []
    fueltanks  = []
    fueltanks.append(fueltank(1000,(-2.5,0,-0.5)))                #fuelmass, cg
    fuselage1 = [fuselage(9000,(-5.5,0,0))]
    wings.append(wing(airfoil2, (-2.50,0,-0.5),19,4.4))             #airfoil, cg, b, c, t/c
    wings.append(wing(airfoil2, (-20,0,0), 8,1.5,0.4))
    return UAV(rotors, wings, container(5000, (-2.5,0,1.25), 1.2), fueltanks, fuselage1)
    
def design1_3():                  #2 engine tiltrotor,  Turboshaft
    rotors = []
    engine1 = engine(312, (-2.5,13,-1),4590)           #mass, cg, power(kw)
    engine2 = engine(312, (-2.5,-13,-1),4590)
    rotors.append(rotor(engine1,11.8,(-2.5,13,-0.5), 150, 0.65))    #engine, rotor diameter, cg, weight, Merit
    rotors.append(rotor(engine2,11.8,(-2.5,-13,-0.5), 150, 0.65))
    airfoil1 = airfoil(0.006, 1.5, 0.32, (0.267,0,0), 0.1175/180*pi, -0.0015/180*pi )  #Cd0, cl_max, cl_0, ac, cl_alfa, cm_alfa
    wings = []
    fueltanks  = []
    fueltanks.append(fueltank(1560,(-2.5,0,-0.5)))                #fuelmass, cg
    fuselage1 = [fuselage(15000,(-5.5,0,0))]
    wings.append(wing(airfoil1, (-2.50,0,-0.5),14,2))             #airfoil, cg, b, c, t/c
    wings.append(wing(airfoil1, (-15,0,0), 4,2,0.4))
    return UAV(rotors, wings, container(5000, (-2.5,0,1.25), 1.2), fueltanks, fuselage1)

def design1_2():                  #2 engine tiltrotor, HEMI --> gewicht engines waarschijnlijk te laag
    rotors = []
    engine1 = engine(272, (0,14,-1),1192)           #weight, cg, power(kw)
    engine2 = engine(272, (0,-14,-1),1192)
    engine3 = engine(200, (-9,0, 0),300)
    rotors.append(rotor(engine1,15.5,(0,14,-0.5), 150, 0.65))    #engine, rotor diameter, cg, weight, Merit
    rotors.append(rotor(engine2,15.5,(0,-14,-0.5), 150, 0.65))
    rotors.append(rotor(engine3,4,(-12,0,0), 75, 0.8, False))
    airfoil1 = airfoil(0.006, 1.5, 0.32, (0.267,0,0), 0.1175/180*pi, -0.0015/180*pi )  #Cd0, cl_max, cl_0, ac, cl_alfa, cm_alfa
    wings = []
    fueltanks  = []
    fueltanks.append(fueltank(1560,(-2,0,-0.5)))                #fuelmass, cg
    wings.append(wing(airfoil1, (-1,0,-0.5),21,5))             #airfoil, cg, b, c, t/c
    wings.append(wing(airfoil1, (-15,0,0), 10,3,0.4))
    return UAV(rotors, wings, container(5000, (-4,0,1.25), 1.2), fueltanks, [fuselage()])

def design2():      # 4 LT4 -> 2 wings 2x 20x3 
    rotors = []
    engine1 = engine(240, (-1.5,14,-1), 475)        #0.24kg/kw/h
    engine2 = engine(240, (-1.5,-14,-1), 475)
    engine3 = engine(240, (-17,-10,-1), 475)
    engine4 = engine(240, (-17,10,-1), 475)
    rotors.append(rotor(engine1, 12,engine1.cg, 120, 0.65))
    rotors.append(rotor(engine2, 12,engine2.cg, 120, 0.65))
    rotors.append(rotor(engine3, 12,engine3.cg, 120, 0.65))
    rotors.append(rotor(engine4, 12,engine4.cg, 120, 0.65))
    wings = []
    airfoil1 = airfoil(0.004, 2, 1.2, (0.34,0,0), 0.1175/180*pi, -0.0035/180*pi )  #Cd0, cl_max, cl_0, ac, cl_alfa, cm_alfa
    fueltanks = []
    wings.append(wing(airfoil(), (-1.5,0,-1), 20,3))
    wings.append(wing(airfoil(),(-15,0,-3), 20,3))
    fueltanks.append(fueltank(900,(0,0,-1)))
    fueltanks.append(fueltank(660,(-15,0,-3)))
    return UAV(rotors, wings, container(5000, (-8.5,0,1.25),1.2), fueltanks, [fuselage()],110000)

def design2_2():    # 4 LT4 -> 2 wings 12x3
    rotors = []
    engine1 = engine(240, (-1.5,6.5,-1), 500)        #0.24kg/kw/h
    engine2 = engine(240, (-1.5,-6.5,-1), 500)
    engine3 = engine(240, (-17,-6.5,-1), 500)
    engine4 = engine(240, (-17,6.5,-1), 500)
    rotors.append(rotor(engine1, 16,engine1.cg, 120, 0.65))
    rotors.append(rotor(engine2, 16,engine2.cg, 120, 0.65))
    rotors.append(rotor(engine3, 16,engine3.cg, 120, 0.65))
    rotors.append(rotor(engine4, 16,engine4.cg, 120, 0.65))
    wings = []
    fueltanks = []
    airfoil1 = airfoil(0.008, 2, 1, (0.28,0,0), 0.119/180*pi, -0.0035/180*pi )  #Cd0, cl_max, cl_0, ac, cl_alfa, cm_alfa
    wings.append(wing(airfoil1, (-1.5,0,-1), 22,2.5))
    wings.append(wing(airfoil1,(-15,0,-3), 22,2.5))
    fueltanks.append(fueltank(700,(-1.5,0,-1)))
    fueltanks.append(fueltank(700,(-15,0,-3)))
    return UAV(rotors, wings, container(5000, (-8.5,0,1.25),1.2), fueltanks, [fuselage(5000,(-8.5,0,-1))])

def design2_3():    # 4 LT4 -> 2 wings 12x3
    rotors = []
    engine1 = engine(760, (-1.5,6.5,-1), 715)        #0.24kg/kw/h
    engine2 = engine(760, (-1.5,-6.5,-1), 715)
    engine3 = engine(760, (-17,-6.5,-1), 715)
    engine4 = engine(760, (-17,6.5,-1), 715)
    rotors.append(rotor(engine1, 14,engine1.cg, 120, 0.65))
    rotors.append(rotor(engine2, 14,engine2.cg, 120, 0.65))
    rotors.append(rotor(engine3, 14,engine3.cg, 120, 0.65))
    rotors.append(rotor(engine4, 14,engine4.cg, 120, 0.65))
    wings = []
    fueltanks = []
    airfoil1 = airfoil(0.008, 2.5, 1, (0.28,0,0), 0.119/180*pi, -0.0035/180*pi )  #Cd0, cl_max, cl_0, ac, cl_alfa, cm_alfa
    airfoil2 = airfoil(0.006, 1.5, 0.32, (0.267,0,0), 0.1175/180*pi, -0.0015/180*pi )
    airfoil3 = airfoil(0.004, 2, 1.2, (0.34,0,0), 0.1175/180*pi, -0.0035/180*pi )
    wings.append(wing(airfoil3, (-1.5,0,-1), 20,2.8))
    wings.append(wing(airfoil3,(-15,0,-3), 20,2.8))
    fueltanks.append(fueltank(1000,(-7.5,0,-1)))
    #fueltanks.append(fueltank(0,(-15,0,-3)))
    return UAV(rotors, wings, container(5000, (-8.5,0,1.25),1.2), fueltanks, [fuselage(6200,(-8.5,0,-1))])



class UAV(object):              #rotors(engine), wings(airfoil), container, fueltanks
    def __init__(self, rotors, wings, container, fueltanks, fuselage, MTOW = 150000.):
        self.container = container        
        self.atmosphere()
        self.rotors = rotors
        self.wings = wings
        self.container = container
        self.fueltanks = fueltanks
        self.state()
        self.fuselage = fuselage
        self.weights(MTOW)
        self.updateweight()
        
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
        self.fuselage[0].setweight(0)
        self.fuselage[0].setweight(self.W-self.weight())
        #print (wing.weight)

    def takeoff(self):
        T = 0
        for i in self.rotors: T += i.st_thrust(self)            #dynamic thrust calc?
        self.z__ = (T - self.W)/self.W*9.81         #a = (T-W)/ m
        if self.z__ >0: print("TAKEOFF!!!")
        #update self.z_                                         #
        #update self.z
        #
        
    def powerrequired(self):            #power required in kw
        l = 0
        for wing in self.wings:
            l += wing.lift(self)
        pd = self.cruiseperformance()[4]*self.V/1000
        pv = self.power2(self.weight()-l)
        return pd + pv, pd, pv

    def cruiseperformance(self):
        self.liftdist()
        D1 = self.wings[0].drag(self)
        D2 = self.wings[1].drag(self)
        D3 = self.container.drag(self)
        D4 = self.fuselage[0].drag(self)
        self.D = D1+D2+D3+D4
        #print (l2)
        return D1, D2, D3, D4, D1+D2+D3+D4, (D1+D2+D3+D4)*self.V/1000

    def cruise(self):
        c = self.cruiseperformance()
        #self.getweight()

        #self.                          #set thrust_lvl         engine/rotor
        # empty                         #get fuel economy       engine
        #                               #usefuel                fueltank
        #                               #get speed              self
        #                               #get thrust             rotor
        #                               #get acceleration       self
        #                               #update speed           self
        #                               # attitude control?
        #                               #update location
        pass                              

    #def fly(self,tl):?
        #set thrustlvl(tl)
        #getthrust
        #getfueleconomy
        #get MoM
        #get cg
        #get x__,y__,z__,x_,y_,z_,x,y,z
        #get theta, beta, gamma
        #determine angular acceleration
        #etc.

    def transition(self):
        pass
        #rotate engines...
        #set thrustlvl
        #get thrust
        #get fueleconomy
        #usefuel
        #get acceleration
        #updatespeed

    def landing(self):
        pass

    def availablepower(self):
        power = 0
        for i in self.rotors: 
            if i.tilt: 
                power += i.engine.power 
        return power


    def range(self):
        #takeoff
        ran = 0
        rc = self.maxclimb()
        t_climb = 1000./rc[0]
        self.fueltanks[0].usefuel((t_climb/3600.+3/60.)*self.rotors[0].engine.fuelconsumption*self.availablepower()/self.rotors[0].merit)
        ran += rc[1] * t_climb
        #print (ran)
        for tank in self.fueltanks:
            while tank.mass > 0.1 * tank.originalmass:                
                self.cruisespeed()
                ran += 60 * self.V
                tank.usefuel(1/60.*self.rotors[0].engine.fuelconsumption*self.cruiseperformance()[-1]/self.rotors[0].merit)
            tank.reset()
        return ran/1000

    def mission(self):
        #takeoff
        d = 0
        t = 0
        rc = self.maxclimb()
        t_climb = 1000/rc[0]
        fuel = (t_climb/3600.+3/60.)*self.rotors[0].engine.fuelconsumption*self.availablepower()/self.rotors[0].merit
        self.fueltanks[0].usefuel((t_climb/3600+3/60.)*self.rotors[0].engine.fuelconsumption*self.availablepower()/self.rotors[0].merit)
        #print (fuel)        
        d += rc[1] * t_climb
        t += t_climb
        while d < 250000:                
            self.cruisespeed()
            d += 60. * self.V
            t+=60
            fuel += 1/60.*self.rotors[0].engine.fuelconsumption*self.cruiseperformance()[-1]/self.rotors[0].merit
            self.fueltanks[0].usefuel(1/60.*self.rotors[0].engine.fuelconsumption*self.cruiseperformance()[-1]/self.rotors[0].merit)
        self.container.empty()
        rc = self.maxclimb()
        t_climb = 1000./rc[0]
        fuel += (t_climb/3600.+3/60.)*self.rotors[0].engine.fuelconsumption*self.availablepower()/self.rotors[0].merit
        self.fueltanks[0].usefuel((t_climb/3600+3/60.)*self.rotors[0].engine.fuelconsumption*self.availablepower()/self.rotors[0].merit)
        d -= rc[1] * t_climb
        t+= t_climb
        while d > 0:                
            self.cruisespeed()
            d -= 60. * self.V
            fuel += 1/60.*self.rotors[0].engine.fuelconsumption*self.cruiseperformance()[-1]/self.rotors[0].merit
            self.fueltanks[0].usefuel(1/60.*self.rotors[0].engine.fuelconsumption*self.cruiseperformance()[-1]/self.rotors[0].merit)
            t+=60
        self.container.empty(False)
        return fuel, t


    def cruisespeed(self):
        self.setV(40)
        D = self.cruiseperformance()[2]+self.cruiseperformance()[3]
        cd0 = self.wings[0].airfoil.Cd0 + D/(0.5*self.rho*self.V**2*(self.wings[0].S+self.wings[1].S))
        cl = sqrt(1/3.*cd0*pi*self.wings[0].A*self.wings[0].e)
        self.V = sqrt(self.weight()/(0.5*self.rho*(self.wings[0].S+self.wings[1].S)*cl))
        return self.V

    def liftdist(self):
        cg = self.cg()[0]
        W = self.weight()
        ac1 = cg - self.wings[0].location[0]       
        ac2 = self.wings[1].location[0] -cg
        l2 = ac1 * W / (ac1 + ac2)
        l1 = W - l2
        self.wings[0].cl_l(self, l1)
        self.wings[1].cl_l(self, l2)
        return l1, l2
  
    def climbperformance(self):
        drag = self.cruiseperformance()[4]
        prop = 0.7
        power = self.availablepower()*1000
        rc = prop * power/self.weight() - self.powerrequired()[0]*1000/self.weight()           
        #print (power/self.weight(), drag/self.weight()*self.V)        
        return rc        
    
    def maxclimb(self):
        rc = []
        vm = []
        
        for i in range(10,70):
            self.setV(i)
            rc.append(self.climbperformance())
            vm.append(i)
        rcmax = max(rc)
        self.V = vm[(rc.index(rcmax))]
        return rcmax, self.V

    def staticstability(self, out = 0):
        tl = 0        
        while self.Mx() < 0:
            tl = self.rotors[2].tl
            self.rotors[2].set_thrust(tl-.05)
            #if self.rotors[3]: self.rotors[3].set_thrust(tl-.05)                       
        if out == 1: print (tl,"      ", self.Mx())
        while self.Mx() > 0:
            tl = self.rotors[2].tl
            self.rotors[2].set_thrust(tl+.0005)
            #if self.rotors[3]: self.rotors[3].set_thrust(tl+.0005)              
        if out == 1: print (tl,"      ", self.Mx())
        return tl, self.rotors[2].st_thrust(self)
        
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
    
    def wingloading(self):
        s = 0
        for i in self.wings: s+= i.S        
        return self.weight()/s

    def Mx(self):
        Mx = -self.weight() * self.cg()[0]
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
        return self.weight()/a_rotors
    
    def power(self, W = -1):                 #power required for takeoff
        if W == -1: W = self.W
        Merit = 0.7
        return (W*1.1*sqrt(self.diskloading()/2/self.rho)/Merit)/1000

    def power2(self, W=-1):                  #power required to sustain hover
        if W==-1: W = self.weight()
        return (W*1*sqrt(self.diskloading()/2/self.rho))/1000
    
class rotor(object):            #engine, diameter, location, mass, merit, thrustlv; Functions: st_thrust(a), set_thrust(tl), tilt(dtetha)
    def __init__(self, engine, diameter = 1, location = (0,0,0), mass = 200, merit = 0.7, tilt = True, thrustlv = 1, t=0,c=0):         #DOF, Angle, Angle adjustment speed
        self.diameter = diameter
        self.location = location
        self.merit = merit
        self.tl = thrustlv
        self.weight = mass *9.81
        self.mass = mass
        self.engine = engine
        self.theta = 0
        self.beta = 0
        self.t = t
        self.c = c
        self.tilt = tilt

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
        
    def max_rev_sec(self, a):   #np max np 
        return sqrt(220**2 - a.V) / (pi * self.diameter)
        
    def thick_to_chord(self):
        return t/double(c)

    def rel_chord_lenth(self):
        return self.c / double(self.diameter)
        
    def delta_drag(self, a):
        cd_s = 0.004  # drag coeff induced by rotor wake, set by elements of airplane performace p. 199
        return self.st_thrust(self, a)*cd_s*a.wetted_area/(pi*self.diameter**2/4)
        
class wing(object):             #airfoil, location, b, c, t_c, labda, Labda, e ; Functions: setlocation(location), wingloading(weight), lift(self, a, cl), drag(a), cl_l(a,L)
    def __init__(self, airfoil, location = (0,0,0), b = 28, c = 5, t_c =.23, Labda =0, labda= 1,  e = 0.85, alfa0=0):
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
        self.alfa0 = alfa0
        self.ac = self.ac()
        
    def ac(self):
        ac = []
        for i in range (0,3):
            ac.append(self.location[i]+self.c * (0.5 - self.airfoil.ac[i]))
        return ac

    def setlocation(self, location):
        self.location = location
    
    def wingloading(self, weight):
        return weight/self.S

    def lift(self, a, cl = 0): #a = uav
        if cl == 0: cl = self.Cl
        return 0.5*a.rho*a.V**2*self.S*cl

    def cl_cd(self):
        clcd = []
        c = np.arange(-1,self.airfoil.cl_max, 0.05)
        for cl in c:
            clcd.append(self.airfoil.Cd0 + cl**2/pi/self.A/self.e)
        return c, clcd

    def drag(self, a):
        Cd = self.airfoil.Cd0 + self.Cl**2/pi/self.A/self.e
        return 0.5*a.rho*a.V**2*self.S*Cd

    def moment(self, a):
        Cm = (self.alfa0 + a.theta) * airfoil.cm_alfa
        M = 0.5 * a.rho() * a.V**2 * self.S * Cm
        return M

    def cl_l(self,a, L):
        self.Cl = L/(0.5*a.rho*a.V**2 * self.S)
        #print (self.Cl)
        if self.Cl > self.airfoil.cl_max: self.Cl = self.airfoil.cl_max
        return self.Cl

    def wingweight(self,a):
        self.mass = a.W_empty/9.81*0.0017*a.N**(0.55)*self.t_c**(-0.3)*(self.b/cos(self.Labda))**(1.05)*(1+sqrt(6.25*cos(self.Labda)/self.b))*(a.W_empty/9.81/self.S)**(-0.3)
        self.weight = 9.81 * self.mass
        return self.weight
        #return 0.0051*(self.EW* self.N)**(0.557)*self.S_wing**0.649*self.A_wing**0.5*self.t_c**(-0.4)*(1+self.labda)**0.1 * cos(self.Labda)**(-1.0)*(self.S_wing*0.05)**0.1

    def setchordlength(self, c):
        self.c = c
        self.S = self.b * self.c
        self.A = self.b/self.c

class airfoil(object):          #Cd0, cl_max, cl_0, ac, cl_alfa, cm_alfa; Functions: Cl_lvl(a, wing), Cl_alpha(a)
    def __init__(self, Cd0 = 0.0315, cl_max = 1.5, cl_0 = 0, ac = (0.25,0,0), cl_alfa = 2*pi, cm_alfa = 0.001):
        self.Cd0 = Cd0
        self.cl_max = cl_max
        self.cl_0 = cl_0        
        self.ac = ac
        self.cl_alfa = cl_alfa
        self.cm_alfa = cm_alfa

    def Cl_lvl(self, a,wing):
       if V>0: return a.W / 0.5/a.rho/a.V**2/wing.S
       else: return 0
        
class fuselage(object):
    def __init__(self, mass = 2000, cg = (0,0,0), cd = 0.3, A = 3*3):
        self.mass = mass
        self.weight = mass*9.81
        self.cg = cg
        self.cd = cd
        self.A = A
    
    def drag(self, a):
        return 0.5*a.rho*a.V**2*self.A*self.cd   
        
    def setweight(self, w):
        self.weight = w
        self.mass = self.weight/9.81
        

class container(object):        #mass, cg, cd, A ; Functions: drag(a), empty(e?)
    def __init__(self, mass = 5000, cg = (0,0,0), cd = 2, A = 2.5*2.5):
        self.cg = cg
        self.cd = cd
        self.mass = mass
        self.weight = mass *9.81
        self.A = A
    def drag(self, a):
        return 0.5*a.rho*a.V**2*(self.A)*self.cd
    def setcg(self, cg):
        self.cg = cg
    def empty(self, e = True, m = 5000, A = 2.5*2.5):
        if e: self.A, self.mass, self.weight = 0,0,0
        else: self.A, self.mass, self.weight = A, m, m*9.81 
    def setmass(self, m):
        self.mass = m
        self.weight = 9.81*m

class fueltank(object):         #mass, cg ; Functions: usefuel(amount)
    def __init__(self, mass = 1560, cg =(0,0,0), emptymass = 10):
        self.weight = mass * 9.81
        self.mass = mass
        self.cg = cg
        self.empty = False
        self.emptymass = emptymass
        self.originalmass = self.mass
        
    def usefuel(self, amount):      #amount in kg
        self.mass = self.mass - amount
        if self.mass < self.emptymass:
            self.mass = self.emptymass
            self.empty = True
        self.weight = self.mass * 9.81
    
    def reset(self):
        self.mass = self.originalmass
        self.weight = self.mass * 9.81

    def setfuel(self, m):
        self.mass = m
        self.weight = m*9.81
        self.originalmass = self.mass

        #cg?

class engine(object):           #mass, cg, power(kw), fuelconsumption(kg/kw/h)
    def __init__(self, mass= 200, cg = (0,0,0), power = 200, fuelconsumption = 0.28):
        self.mass = mass
        self.weight = 9.81*mass
        self.cg = cg
        self.power = power
        self.fuelconsumption = fuelconsumption


def test():
    a = design2_2()
    for i in range(15,40):
        a.setV(i)
        #print(round(a.cruiseperformance()[5]), round(a.W-(a.wings[0].lift(a)+a.wings[1].lift(a))), round(a.wings[0].drag(a)))

   
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
    plt.plot(tail, vmax)
    plt.show()
    plt.plot(tail, d)
    plt.show()
    plt.show(tail, cl)
    plt.show()
    return tail[(d.index(min(d)))], min(d)
    #print (cl)
    
def mindrag(a, x = 0, y = ''):
    V,d1,d2,d3,d4, cl1, cl2, pr, rc, d5,l1,l2, pr1, pr2 = [],[],[],[],[],[],[],[],[],[],[],[],[],[]
    for i in range (1,80):
        a.setV(i)
        c=a.cruiseperformance()
        d1.append(c[0])
        d2.append(c[1])
        d3.append(c[2])
        d4.append(c[3])
        d5.append(c[4])
        V.append(i)
        cl1.append(a.wings[0].Cl)
        cl2.append(a.wings[1].Cl)
        l1.append(a.wings[0].lift(a))
        l2.append(a.wings[1].lift(a))
        p = a.powerrequired()
        pr.append(p[0]/0.7)
        pr1.append(p[1]/0.7)
        pr2.append(p[2]/0.7)
        rc.append(a.climbperformance())
    if x == 1:    
        linestyles = ['-', '--', '-.', ':','--']
        fig = plt.figure()
        fig.figsize=(70, 70)
        fig.suptitle('Drag ' + y, fontsize=20)
        plt.xlabel('Velocity (m/s)', fontsize=16)
        plt.ylabel('Drag (N)', fontsize=16)        
        plt.plot(V,d1,color = "blue", label ='front wing', linestyle = linestyles[1])
        plt.plot(V,d2,color = "red", label = 'rear wing/tailplane', linestyle = linestyles[2])
        plt.plot(V,d3,color = "green", label = 'container', linestyle = linestyles[3])
        plt.plot(V,d4,color= "cyan", label = 'fuselage', linestyle = linestyles[4], marker = '.')
        plt.plot(V,d5,color = "purple", label = 'combined drag')
        plt.legend(loc = 'upper left', prop={'size':9})
        plt.show()
        fig.savefig('./figs/drag'+y+'.png', format='png', dpi=900)      
        
        fig2 = plt.figure()
        fig2.figsize=(70, 70)
        fig2.suptitle('Lift coefficients ' + y, fontsize=20)
        plt.xlabel('Velocity (m/s)', fontsize=16)
        plt.ylabel('Lift coefficient', fontsize=16)
        plt.plot(V, cl1, color = "blue", label = 'front wing', linestyle = linestyles[1])
        plt.plot(V, cl2, color = "red", label = 'rear wing/tailplane', linestyle = linestyles[2])
        plt.legend(loc= 'lower left')
        plt.show()        
        fig2.savefig('./figs/Cl'+y+'.png', format = 'png', dpi=900)    

        fig3 = plt.figure()
        fig3.figsize=(70, 70)
        fig3.suptitle('Power required ' + y, fontsize=20)
        plt.xlabel('Velocity (m/s)', fontsize = 16)
        plt.ylabel('Power required (kW)', fontsize = 16)
        plt.plot(V, pr1, color = "cyan", label = 'horizontal power', linestyle = linestyles[1])
        plt.plot(V, pr2, color = "green", label = 'vertical power', linestyle = linestyles[2])
        plt.plot(V, pr, color = "blue", label = 'total power required')
        plt.legend(loc = 'upper left')
        plt.show()
        fig3.savefig('./figs/Pr'+y+'.png', format = 'png', dpi = 900)
        
        fig4 = plt.figure()
        fig4.figsize=(70, 70)        
        fig4.suptitle('Rate of climb '+y, fontsize = 20)     
        plt.xlabel('Velocity (m/s)', fontsize = 16)
        plt.ylabel('Rate of climb (m/s)', fontsize = 16)
        plt.plot(V, rc, color = "green", label = 'rate of climb')
        #plt.legend(loc='upper left')
        plt.show()
        fig4.savefig('./figs/RC'+y+'.png', format = 'png', dpi=900)
        
        #plt.plot(V, l1, color = "blue")
        #plt.plot(V, l2, color = "red")
        #plt.show()
        print ("Min:", V[(pr.index(min(pr)))], " m/s",  '{0:.3g}'.format(d4[pr.index(min(pr))]), " N", min(pr), "kW")
 
        #print (pr)
    return V[(d4.index(min(d4)))], min(d4), cl1[(pr.index(min(pr)))], min(pr)

def clcdplot(a):
    clcd = a.wings[0].cl_cd()
    #print (clcd[0])
    plt.plot(clcd[1],clcd[0], color = "blue")
    plt.show()

def payloadrange(a, y = ''):
    b = a    
    ran = []
    w = np.linspace(0,5000,11)    
    for m in w:
        a = b
        if m == 0:
            a.container.empty()
        else:
            a.container.empty(False)
            a.container.setmass(m)        
        ran.append(a.range())
    fig4 = plt.figure()
    fig4.figsize=(70, 70)        
    fig4.suptitle('Payload vs. range '+y, fontsize = 20)     
    plt.ylabel('Payload (kg)', fontsize = 16)
    plt.xlabel('Range (km)', fontsize = 16)
    plt.plot(ran, w, color = "green", marker = 'o', linestyle = 'none')
    plt.show()
    fig4.savefig('./figs/PayloadRange'+y+'.png', format = 'png', dpi=900)
    
def fuelest(a1):
    a1.fueltanks[0].setfuel(5000)    
    a1.fueltanks[0].setfuel(1.1*a1.mission()[0])
    a1.fueltanks[0].setfuel(1.1*a1.mission()[0])
    a1.fueltanks[0].setfuel(1.1*a1.mission()[0])
    f = 1.1*a1.mission()[0]
    a1.fueltanks[0].setfuel(f)
    return (f)
    
def chordlength(a, y = ''):
    rc = []
    ch = np.linspace(0.5,6,120)
    for c in ch:
        for wing in a.wings:
            a.wings[0].setchordlength(c)
        rc.append(a.maxclimb()[0])
    fig10 = plt.figure()
    fig10.figsize=(70, 70)        
    fig10.suptitle('Chordlength vs rate of climb '+y, fontsize = 20)     
    plt.ylabel('Rate of climb (m/s)', fontsize = 16)
    plt.xlabel('Chordlength (m)', fontsize = 16)    
    plt.plot(ch,rc)
    plt.show()
    fig10.savefig('./figs/ChordRC'+y+'.png', format = 'png', dpi=900)    
    
    return ch[(rc.index(max(rc)))]
    


if __name__ == "__main__":
    main()