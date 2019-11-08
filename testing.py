# -*- coding: utf-8 -*-


#Import Statements
import unittest
import scipy as sp
import optomize

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
        z,wn = optomize.sys_vals(os,ts)
        
        #Comparing the test to the actual
        print(test_z, z, test_wn, wn)
        self.assertAlmostEqual(z,test_z,places = 14)
        self.assertAlmostEqual(wn,test_wn,places = 14)
        

class Testing_poles(unittest.TestCase):
    '''
    This class is used to test the feedback gains that
    should be outputted to the GUI
    '''
    
    def test_K(self):
        '''
        Check the gain matrix
        '''
        
        #Values for the test
        os = 30
        ts = 3
        
        #Actual value (calculated in MATLAB)
        test_K = sp.array([9.57690, 0.6667])
        K = optomize.for_the_gui(os,ts)
        
        print(test_K, K)
        self.assertAlmostEqual(K,test_K, places = 14)
    
    pass
