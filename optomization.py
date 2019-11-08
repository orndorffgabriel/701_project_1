# -*- coding: utf-8 -*-

#Optomization file
import scipy as sp
from scipy import signal

print('dabo')

def sys_vals(Mp,ts):
    """Returns the damping ratio(zeta) and natural
    fequency(wn) of the desired 2nd order response
    given the user's desired overshoot(Mp) and 
    2% settling time(ts) values."""
    zeta = (-sp.log(Mp/100))/sp.sqrt((sp.pi)^2+(sp.log(Mp/100))^2)
    wn = 4/(zeta*ts)
    return zeta,wn

def place_poles(zeta, wn):
    """Returns the required system poles to achieve
    the desired 2nd order response."""
    s = sp.ndarray([-zeta*wn+1j*wn*sp.sqrt(1-zeta^2),
         -zeta*wn-1j*wn*sp.sqrt(1-zeta^2)])
    return s

def for_the_gui(Mp,ts):
    """Calculates the system gains to place the poles at 
    the desired locations. This is the only function
    that the GUI will need to call and give to the user.
    The matrices are assumed to be for a motor with a 
    transfer function of a/(s(s+b))."""
    a = 1
    b = 2
    
    """The matrices are for state-space form Ax + Bu = x_dot, where A is the"
       state coefficient matrix, and B is the input coefficient matrix. a and b are                       
       arbitrary values for the motor dynamics"""
    A = sp.ndarray([[0, 1],
                    [0, -b]])            
    B = sp.ndarray([[0],             
                   [a]])             
    
    zeta,wn = sys_vals(Mp,ts)
    poles = place_poles(zeta,wn)
    
    """The scipy function that creates
    controller gains for the system"""
    k = signal.place_poles(A,B,poles)   
    return k                            