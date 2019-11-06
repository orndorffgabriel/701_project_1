# -*- coding: utf-8 -*-

#Import Statements
import unittest
import scipy as sp

val = 23 #stand in value

class Testing_foos(unittest.TestCase):
    '''
    This class is used in order to test the
    functions that return the Overshoot and
    Time to Settle values when given a zeta and
    Wn.
    '''
    
    def test_ts(self):
        '''
        Check to make sure that the time to 
        settle is being calculated correctly.
        '''
        zeta  = -0.2
        wn = -3
        
        ts_val = 4/(zeta*wn)
        self.assertAlmostEqual(val,ts_val,places = 14)
        
    def test_os(self):
        '''
        Check to make sure that the percent
        overshoot is being calculated correctly.
        '''
        zeta  = -0.2
        
        os_val = 100*sp.exp((-zeta*sp.pi)/sp.sqrt(1-zeta**2))
        self.assertAlmostEqual(val,os_val,places = 14)

class Testing_opto_ts(unittest.TestCase):
    '''
    This class is used to test the optimization of the
    time to settle when given a percent overshoot to avoid.
    '''
    
    def test_zeta(self):
        '''
        checking to make sure the zeta values are valid
        '''
        pass
    
    def test_wn(self):
        '''
        checking to make sure that the wn values are valid
        '''
        pass
    
    pass