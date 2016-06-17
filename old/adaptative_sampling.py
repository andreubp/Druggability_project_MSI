#from htmd import *
#from htmd.protocols.production_v1 import Production
#from natsort import natsorted#

#adapt = Production()
#adapt.acemd.show()#

##adapt.acemd.bincoordinates = '/docked/equil/1/output.coor'
##adapt.acemd.extendedsystem  = '/docked/equil/1/output.xsc'
#adapt.acemd.run='50ns'
#adapt.temperature = 300#
#

#equils = natsorted(glob('docked/equil/*/'))
#print(len(equils))#

#for i, b in enumerate(equils):
#    print(b)
#    adapt.write(b,'docked/generators/{}'.format(i+1))

adapt = AdaptiveRun()
adapt.nmin = 2
adapt.nmax = 3
adapt.nepochs = 2
adapt.ticadim = 0
adapt.metricsel1 = 'name CA'
adapt.generatorspath = docked/generators/*/'
adapt.app = AcemdLocal()
adapt.run()