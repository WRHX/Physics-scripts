import numpy as np
import matplotlib.pyplot as plt

class FabryPerotCavity(object):
    def __init__(self):

        #FP settings
        self.R1 = 0.99
        self.R2 = 0.99
        self.d = 1E6  #m
        self.c = 3E8 #m/s

        # create frequency arrays: optical regime first
        self.start_lambda = 300E-9 #m
        self.stop_lambda = 800E-9 #m
        self.step_lambda = 0.0001E-9 #m Make sure this is small enough ! otherwise resonances don't show correctly

        self.lambdas = np.arange( self.start_lambda, self.stop_lambda + self.step_lambda , self.step_lambda )
        self.omegas = ( 2 * np.pi ) / self.lambdas

    def CalculateInternalCavityField(self):
        '''Calculate P_cav / P_in '''
        phi_array = ( self.omegas * self.d )  / self.c
        power_ratios = ( 1 - self.R1 ) / ( np.absolute( 1 + ( np.exp( 1j * phi_array ) ) * np.sqrt( self.R1 * self.R2 ) )**2 )
        return phi_array, power_ratios

if __name__ == '__main__':
    FPcav = FabryPerotCavity()
    phi_array, power_ratios = FPcav.CalculateInternalCavityField()


    plt.plot( phi_array , power_ratios, color = 'b' )
    plt.show()
