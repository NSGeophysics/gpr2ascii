import gprpy.gprpy as gp
import sys
import numpy as np
import os

###### Defining some helper functions ######
 
def writeAscii(mygpr,fileout):
    np.savetxt(fileout+".txt",mygpr.data)

    # Now write file information in a separate header file
    headname = fileout+".hdr"
    # Write each important variable
    with open(headname, "w") as header:
        header.write("min two-way travel time [ns] : %g\n" %(np.min(mygpr.twtt)))
        header.write("max two-way travel time [ns] : %g\n" %(np.max(mygpr.twtt)))
        header.write("number of time points : %d\n" %(len(mygpr.twtt)))  
        header.write("start profile position [m] : %g\n" %(np.min(mygpr.profilePos)))
        header.write("end profile position [m] : %g\n" %(np.max(mygpr.profilePos)))
        header.write("number of traces : %g\n" %(len(mygpr.profilePos)))
        header.write("velocity used [m/ns] : %s\n" %(str(mygpr.velocity)))
        header.write("min topography [m] : %s\n" %(str(mygpr.minTopo)))
        header.write("max topography [m] : %s\n" %(str(mygpr.maxTopo)))
        
    

###### This is the main code ######

filein = sys.argv[1]

if len(sys.argv) > 2:
    fileout = sys.argv[2]
else:
    fileout = filein

# Remove file extension from filein
fileout = os.path.splitext(fileout)[0]

# Load the GPRPy file
mygpr = gp.gprpyProfile()
mygpr.importdata(filein)

# Write the data and header
writeAscii(mygpr,fileout)








    





