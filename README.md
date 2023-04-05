# gpr2ascii

## Usage

If you have a .gpr file exported from GPRPy, say it is called `mydata.gpr`, you can turn it into an ASCII data file by running
`python gpr2ascii.py mydata.gpr`
The output will be two files `mydata.txt` (the ASCII data file) and `mydata.hdr` (a text file with meta data).

You can also run 
`python gpr2ascii.py mydata.gpr outputname`
to create the two files `outputname.txt` and `outputname.hdr`.

**Note that thefile gpr2ascii.py needs to be in the directory where you run the above commands**

For testing purposes, you can plot the ASCII data using the provided python script ascii2plot.py
`python ascii2plot.py mydata.txt`
