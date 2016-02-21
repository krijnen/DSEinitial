from math import *

#Inputs
NR = 4                                      #Number of rotors
MTOW = 14000                                #Maximum Take Off Weight in kg  0.5 since 2 rotors are assumed
radius = 7.5                                  #Total radius of the disk in meters
rho = 1.225                                 #Air density in kg/m2
C = 12                                      #Rate of Climb
M = 0.7                                     #Figure of Merit
N = 3                                       #Number of blades
v_tip = 220                                 #Maximum tip speed m/s, M = 0.65
sigma = 0.07                                #Solidity of the rotor blades
A = 17.5                                    #Aspect Ratio Blade

W_MTOW = (1/NR)*MTOW*9.81 
c = (radius) / A 
Omega = v_tip / radius 
RPM = Omega * 60 / (2*pi) 
A_disk = pi*radius**2 
DL = (W_MTOW*9.81) / A_disk                 #per disk


v_i_hover = sqrt((W_MTOW) / (2*rho*pi*radius**2)) 
C_bar = C/v_i_hover                           #Dimensionless rate of climb
v_i = -C_bar/2 + v_i_hover                    #True induced velocity


P_ideal_hover = NR * sqrt(W_MTOW / (2*rho*pi*radius**2)) * W_MTOW     
P_hover = NR * (W_MTOW/M) * sqrt(W_MTOW/(2*rho*pi*radius**2))    #Total needed power for hover
shp_hover = P_hover * 1.34102209 / 1000 
round(shp_hover)

#multipe engines:
T = (2*rho*pi*radius**2*(C+v_i)*v_i )       #necessary thrust per rotor
round(T) 
phi = atan((C+v_i)/Omega*radius)                #Some sort of angle.....

#C_T = T / (rho*(Omega*radius)**2*pi*radius**2)
#C_T = (W_MTOW*9.81) / (pi*radius**2*rho*v_tip**2)
C_T = 2*(v_i / v_tip)**2
C_L = (C_T * 6.6) / sigma
#C_L = T / (N*0.5*rho*Omega**2*c*(0.97*radius)**3 / 3)
#C_T = sigma * C_L / 6.6
C_P = (C_T / M) * sqrt(C_T / 2) 
labda = sqrt(C_T / 2) 

P_total = NR * (W_MTOW * C / 2 + P_hover / NR ) 
shp = P_total * 1.34102209 / 1000 
round(shp)
print (shp)
