# -*- coding: utf-8 -*-


#Import Statements
import unittest
import scipy as sp
import optomization
from scipy import signal

class Testing_foos(unittest.TestCase):
    '''
    This class is used in order to test the
    functions that return the Zeta and
    Wn values when given a percent overshoot
    and time to settle.
    '''
    
    def test_zeta_wn(self):
        '''
        Check to make sure that the Zeta
        and Wn values are correct.
        '''
        #Values for the test
        os = 30
        ts = 3
        
        #Getting the correct values
        test_z = (-sp.log(os/100))/sp.sqrt(sp.pi**2+sp.log(os/100)**2)
        test_wn = 4/(ts*test_z)
        
        #Getting output from the file
        z,wn = optomization.sys_vals(os,ts)
        
        #Comparing the test to the actual
        print(test_z, z, test_wn, wn)
        self.assertAlmostEqual(z,test_z,places = 14)
        self.assertAlmostEqual(wn,test_wn,places = 14)
        

class Testing_poles(unittest.TestCase):
    '''
    This class is used to test the feedback gains that
    should be outputted to the GUI
    '''
    
    def test_K_gains(self):
        '''
        Check the gain matrix
        '''
        
        #Values for the test
        os = 30
        ts = 3
        
        #Actual value
        zeta = (-sp.log(os/100))/sp.sqrt(sp.pi**2+sp.log(os/100)**2)
        wn = 4/(ts*zeta)
        
        P= sp.array([-zeta*wn+1j*wn*sp.sqrt(1-zeta**2), -zeta*wn-1j*wn*sp.sqrt(1-zeta**2)])
        
        A = sp.array([[0, 1],
                    [0, -2]])            
        B = sp.array([[0],             
                      [1]])  
        test_K = signal.place_poles(A,B,P).gain_matrix[0]
        
        #Getting output from file
        K = optomization.for_the_gui(os,ts)
        
        print(test_K, K)
        for i in range(len(test_K)):
            self.assertAlmostEqual(K[i],test_K[i], places = 14)
    
if __name__ == '__main__':
    unittest.main()
