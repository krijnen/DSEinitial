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
        
  
    def setV(self, V):
        self.V = V

    def weights(self, MTOW):
        self.W = MTOW
        self.W_f = 1561*9.81 #Derived from average fuel consumption k-maxx * expected mission time
        self.W_payload = self.container.weight
        self.W_empty = self.W - self.W_f - self.W_payload
        self.N = 3
        self.W_wing = 0  
       
    def transition(self):
        pass
        #rotate engines...
        #set thrustlvl
        #get thrust
        #get fueleconomy
        #usefuel
        #get acceleration
        #updatespeed

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
        Mx = -self.weight() * self.cg()[0]
        for i in self.rotors: Mx += i.st_thrust(self) * i.location[0]    
        return Mx

    def atmosphere(self):
        self.rho = 1.1      
        
    def diskloading(self):
        a_rotors = 0
        for x in self.rotors: a_rotors+= (x.diameter/2)**2*pi
        return self.weight()/a_rotors
    
