This is the README file for the code grtrans, which performs polarized general relativistic 
radiative transfer via ray tracing. The code is described in Dexter (2016), and uses geokerr 
(Dexter & Agol 2009). If you use grtrans in your own work, please cite those two papers.

This package contains the Fortran source code files (upper level routines in f90 with 
geodesic calculations, integration, and some other pieces in f77). In addition to these files, 
cfitsio must be installed. The Makefile.top.sample file should be edited and renamed to Makefile.top. 
It should include the desired f90 compiler and options, as well as the location of grtrans and the
cfitsio library if it is not in the standard library path. The code can then be compiled with make.

For using the Python module, pyfits should also be installed.

QUICK START

Examples of running the code can be found in run_grtrans_test_problems_public.py. The examples called 
THINDISK, BL09JET, and HARM were used to make Figures 5, 6, and 8 respectively (although for the HARM 
problem with polarization the argument nvals=4 is needed to use all 4 Stokes parameters).

The test problems script uses both of the methods for running grtrans through Python, as its own module 
(pgrtrans) or by using input files. See below for more detailed instructions and information on variable names.

RUNNING GRTRANS WITH PYTHON SCRIPT

The easiest way to run grtrans is with the included python script, grtrans_batch.py. From the 
Python / iPython command line, do:

import grtrans_batch as gr
x=gr.grtrans()
x.compile_grtrans()
x.write_grtrans_inputs('inputs.in')
x.run_grtrans()
x.read_grtrans_output()
x.disp_grtrans_image(0)

All of the inputs are set by write_grtrans_inputs, which can be changed from their default 
values with keywords, e.g. here are some sample runs you could try (with x.run_grtrans() etc. after each one): 

Standard thin disk (stellar mass black hole x-ray images / spectra)
x.write_grtrans_inputs('inputs.in',nfreq=25,nmu=1,fmin=2.41e17,fmax=6.31e18,fname="THINDISK")

Numerical inhomogeneous disk model from Dexter & Agol (2011) (toy model so completely pixellated disk)
x.write_grtrans_inputs('inputs.in',fname="NUMDISK",nfreq=25,nmu=1,fmin=2.41e17,fmax=6.31e18,ename="BB")

Semi-analytic model for M87 jet by Broderick & Loeb (2009)
x.write_grtrans_inputs('inputs.in',fname="FFJET",nfreq=25,nmu=1,fmin=2.41e10,fmax=6.31e14,ename="POLSYNCHPL",nvals=4,spin=0.998,standard=1,nn=[100,100,100],uout=0.01,mbh=6.4e9)

Bondi spherical accretion problem but in GR
x.write_grtrans_inputs('inputs.in',fname="SPHACC",nfreq=25,nmu=1,fmin=2.41e10,fmax=6.31e14,ename="POLSYNCHTH",nvals=4,spin=0.,standard=1,nn=[100,100,100])

read_grtrans_output() reads the output into the grtrans object variables ab, nu, spec, ivals 
which contain the alpha and beta values of the image (camera pixel locations in x and y), observed frequencies, observed spectrum, and observed intensities. The number of Stokes parameters (1 or 4) is set by the input parameter nvals. 

INPUT PARAMETERS

The file files.in tells the code the name of the input and output files, set in the python script by iname and oname and using the method set_grtrans_input_file(iname,oname).

The main input file has the following namelists / variables:

geodata -- geodesic-related parameter namelist

standard -- method for computing geodesics. =2 for tracing in polar angle (e.g., to the 
equatorial plane of a thin disk) and =1 for tracing in radius (e.g., through an extended 
accretion flow).

mumin, mumax, nmu -- Minimum/maximum/number of mu = cos(i) of observer camera(s). mu=1,0 corresponds to face-on, edge-on.

spin -- dimensionless black hole spin -1 < spin < 1.

uout, uin -- When standard=1, npts points are saved evenly spaced between uout and uin. uout should correspond to the outermost
 location to use for calculating radiation, and uin=1 traces up to the event horizon.

rcut, nrotype -- camera shape parameters, should = 1.0, 2.

gridvals -- Camera extent in impact parameters alpha and beta.

nn -- number of x pixels, y pixels, and points along each pixel (npts). The camera pixel spacing
is set by (gridvals(2)-gridvals(1))/nn(1), (gridvals(4)-gridvals(3))/nn(2). The geodesic 
resolution is similarly (uout-uin)/nn(3) when standard=1.

i1, i2 -- starting and ending geodesic index. By default these values are 1 and nn(1)*nn(2) so 
that intensities will be calculated for the entire camera. Instead setting these values to span
a smaller range is useful for debugging (e.g. i1=i2=some index that is of interest to study in detail).

extra -- output a large number of quantities as function of geodesic position to the file geodebug.out. 
This is used for debugging, especially in combination with i1=i2 to run only a single geodesic and 
study the output in detail. The current variables that are output to that file can be found in 
read_geodebug_file.py and used in python as e.g. import read_geodebug_file as d after the file is created.

debug -- calculates "images" of many other ray-averaged or ray-integrated quantities, which are stored 
in the output as though they are additional Stokes parameters. These are:

\tau_I
\tau_Q
\tau_U
\tau_V
\tau_\rhoQ
\tau_\rhoV

which are the total optical depth along the ray for the transfer coefficients \alpha_I,Q,U,V and \rho_Q,V.
In addition the following quantities are unpolarized Stokes I intensity weighted, e.g. 

xbar = \int d\lambda x(\lambda) j e^-\tau / \int d\lambda j e^-\tau

for the quantities x, which are:

r
\theta
\phi
n
T_e
B
\beta

and the last quantity is \beta = p_gas / p_mag.

fluiddata -- Fluid model related parameters

fname -- name of fluid model. Possibilities are:

        "THINDISK" -- Shakura & Sunyaev (1973), Novikov & Thorne (1973) thin accretion disk 
      	solution with Page & Thorne (1974) extension to GR. For this model should use 
	standard=2, muf=0.0, nn(3)=1 (equatorial plane). Emission is usually 
	BB, FBB, BBPOL, FBBPOL.

	"PHATDISK" -- Dexter & Agol (2011) "no-zone" inhomogeneous disk model. The average 
	surface brightness of each annulus is the same as in THINDISK, but the temperature in 
	each annulus is assumed to be log-normally distributed with width 
	\sigma = (log(10) \sigma_T)^2 / 2. Geodesic parameters same as THINDISK, emission 
	from INTERPEMIS.

	"NUMDISK" -- Generic optically thick, geometrically thin disk model specified by 
	Teff(r,\phi). Geodesic parameters and emissivities same as THINDISK. 

	"SPHACC" -- General relativistic version of Bondi (1952) spherical accretion solution 
	based on Michel (1972) (see also Shapiro & Teukolsky 1983). For this model use 
	standard=1, uout > 0.0025 (where stored numerical flow solution begins). Emission 
	is usually synchrotron (SYNCHEMIS, POLSYNCHEMIS, SYNCHPL, POLSYNCHPL).

	"FFJET" -- Semi-analytic jet model of Broderick & Loeb (2009). Quantities are 
	specified numerically. Geodesic parameters are standard=1, uout > umin where umin 
	is determined by outer radius saved for numerical solution. (WHAT IS IT IN MY DEFAULT?) 


	"HARM" -- Numerical general relativistic MHD (GRMHD) accretion flow model from publicly
	available HARM code (Gammie et al. 2003, Noble et al. 2006). Template for other 2D
	numerical models. Requires time-dependent rad trans, coordinate transformations 
	(KS <--> BL), ability to read HARM binary files.

	"HOTSPOT" -- Time-dependent orbiting hotspot model of Schnittman & Bertschinger (2004), 
	Broderick & Loeb (2006), etc. Geodesic parameters are same as THINDISK.

emisdata -- Emissivity related parameters

ename -- Name of emission model. The possibilities so far are:

      "lambda" -- emissivity = affine parameter of ray. Unphysical but useful for geodesic 
      tests.
      
      "INTERP" -- Interpolate numerically stored emission/absorption coefficients to desired 
      observed frequencies. Used i.e. with PHATDISK.

      "INTERPPOL" -- same as INTERP but for polarized case.

      "BB" -- Blackbody emissivity. Also used to compute absorption coefficients for synchrotron
      emissivities from Kirchoff's Law.

      "BBPOL" -- Like BB but with other Stokes parameters (set to zero). Used for polarized 
      thin disk problems for example.

      "FBB" -- Color-corrected blackbody emissivity fbnu(T,f,nu)=f**(-4) bnu(f*T,nu).

      "POLSYNCHTH" -- Polarized synchrotron emission from a thermal particle distribution. 
      Emission coefficients from Huang et al. (2009), Dexter (2011) based on Melrose (1983?). 
      Absorption from Kirchoff's assuming LTE.
      
      "POLSYNCHPL" -- Polarized synchrotron emission from a power law particle distribution. 
      Emission & absorption coefficients from Dexter (2011) based on Melrose (1983?). Take into 
      account lower/upper energy cutoffs to the distribution.

      TO ADD:

      "EMISTABLE" -- Interpolation of emissivity to fluid variables e.g. n, B, T for synchrotron
      radiation for arbitrary distribution function. Could calculate table in advance and store,
      then use EMISTABLE to calculate at observed frequency and fluid vars.

Each fluid model and emissivity has associated parameters, e.g. for specifying the accretion rate
onto the black hole for a numerical simulation or the cutoff Lorentz factors for synchrotron emission
from a power law distributed population of electrons.

OUTPUT FORMAT

Code output is either stored in FITS or plain binary format. 

When using the python as above, you can do

x.read_grtrans_output()

after which the intensity values will be an array x.ivals, and the spectrum will be in x.spec.

In python, you could then do for example

x.disp_grtrans_image(0)

to view the first image, and change the argument 0 to choose different images 
(e.g. with different observed frequencies or other parameters). There is also an optional keyword 
'stokes' to view images of different Stokes parameters in Python (e.g., 
x.disp_grtrans_image(0,2) for Stokes U from the first image calculated).

The binary output format is as follows:

3 integers: nx ny nvals
1 integer: nkey
nkey floats: keyvals
2*nx*ny floats: ab
nvals*nx*ny floats: ivals

This pattern repeats for each observed frequency and mu=cos(i) value. An example for reading 
the plain binary is in grtrans_batch.py read_grtrans_output(). 

RUNNING GRTRANS DIRECTLY THROUGH PYTHON WITH F2PY

Instead of using input files, the code can be compiled as a Python module called pgrtrans ('make pgrtrans'). 
Once compiled, all of the above runs can instead be carried out directly within Python by using pgrtrans objects. 

The keywords passed to write_grtrans_inputs() above can instead be passed directly to run_pgrtrans(). Examples of
this usage can be found e.g. in run_grtrans_test_problems_public.py.

CODE STRUCTURE

The top level of the code is grtrans_main in grtrans.f90. This is where the loops over cos(i)
values occurs, and where the loop over observer times will be added for the time-dependent case.
It is also where the OpenMP directives are, and the entire rest of the code is trivially 
parallel. All fluid model data (e.g., memory intensive simulation data) should be loaded before
the call to grtrans_driver so that the data can be shared between threads (in load_fluid_model).
This routine also initializes the camera, stores the parameters for calculating the geodesics,
and reads the code input files.

The main routine is grtrans_driver. It is encapsulated in the grtrans module, which includes
many others: fluid_model, class_rad_trans, geodesics, emissivity, odepack, ray_trace, 
interpolate, phys_constants, kerr, chandra_tab24. It also consists of several global objects 
from these modules (fluid, rad_trans, geo, emis, emis_params, source_params). These are global
to avoid having to pass them through odepack, which is an old F77 code.

grtrans_driver gets the points along the current geodesic (initialize_geodesic), initializes 
the fluid and emissivity models, calculates the fluid variables along the geodesic 
(get_fluid_vars), calculates the redshift, angle between magnetic field and wave vector, and 
angle between camera Stokes vectors and magnetic field in the comoving orthonormal frame, 
converts (convert_model) the fluid variables (pressure, density, field strength) to cgs 
quantities used for emissivities (e.g., electron density and temperature), assigns any extra 
quantities needed to calculate emissivities (emis_model). 

Then it loops over observed frequency, calculating emissivities at that frequency, applying 
relativistic corrections (e.g., redshift), and integrates the radiative transfer equation 
along the ray at that frequency (grtrans_driver_integrate). If only 1 point on the geodesic is 
used (i.e., thin disk problems), instead the "emissivity" will contain the intensity at that 
point which can be transferred to that at infinity (grtrans_compute_intensity). In this case,
the polarization is parallel transported using transpol.

Then the data are saved using save_raytrace_camera_pixel.

Should write up each of the underlying modules, but instead for now will just give examples 
of how to add new models.

HOW TO ADD FLUID MODELS

A new fluid model should go in its own .f90 file (fluid_model_fname.f90) or similar, where fname
is the name of the fluid model. The fluid model itself can have its own input file or numerical
data to be read/stored when loaded and shared among grtrans threads. It must have some way to 
calculate fluid variables at any point in spacetime. The fluid model itself should be 
its own module and should not use any of the higher level grtrans modules (i.e., fluid_model).

The fluid model can then be implemented in fluid.f90 by adding an integer parameter for it and 
adding appropriate entries to load_fluid_model, initialize_fluid_model, unload_fluid_model, 
del_fluid_model, get_fluid_vars_arr, and convert_fluid_vars_arr.

Finally, the interface get_fname_fluidvars must be added. This routine should accept a 
four-vector x0, spin a, and fluid object f. The get_fname_fluidvars routines then should use 
the routine to calculate fluid variables at points x0 and store those in the fluid object. A 
separate routine convert_fluidvars_fname can be used to convert the fluid variables to cgs 
units if they aren't already.

The existing fluid models should serve as useful examples.

HOW TO ADD EMISSIVITIES

Emissivities can added similarly. As well as a function to calculate the emissivity, a new 
name and corresponding parameter should be added to emis.f90. Then entries for the emissivity 
should be added to select_emissivity_values, initialize_emissivity, calc_emissivity, 
assign_emis_vars, emis_model, and del_emissivity.

Again the existing emissivities can be used as templates.

WHEN YOU FIND BUGS OR HAVE QUESTIONS

Please e-mail jdexter@mpe.mpg.de
