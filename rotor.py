class rotor(object):            #engine, diameter, location, mass, merit, thrustlv; Functions: st_thrust(a), set_thrust(tl), tilt(dtetha)
    def __init__(self, location = (0,0,0), mass = 200, merit = 0.7, thrustlv = 1, diameter = 8, t=0,c=0):         #DOF, Angle, Angle adjustment speed
        self.diameter = diameter
        self.location = location
        self.merit = merit
        self.tl = thrustlv
        self.weight = mass *9.81
        self.mass = mass
        self.theta = 0
        self.beta = 0
        self.t = t
        self.c = c

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
        
