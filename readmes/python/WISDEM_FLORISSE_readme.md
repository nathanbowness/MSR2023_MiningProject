
DEPRECATED
----------

**THIS REPOSITORY IS DEPRECATED AND WILL BE DELETED AT THE END OF 2019. UNTIL THEN, IT WILL BE KEPT IN READ-ONLY MODE AND NO LONGER MAINTAINED.**

The active FLORIS can be found at https://github.com/nrel/floris



---------------------------------------
  WISDEM FLORISSE 'release version'
---------------------------------------

This version is intended to provide a ''lean'' version of the WISDEM FLORISSE model, based on the OpenMDAO model structure. We will be adding more features and examples in the near future.

## Installation / requirements

This release version of WISDEM FLORIS-SE requires OpenMDAO 0.13 to be installed.  OpenMDAO 0.13 can be downloaded at:
  http://openmdao.org/downloads/archive/
This version of FLORISSE is not compatible with earlier or later versions of OpenMDAO.

## Example scripts

The example script FLORISvsSOWFA.py gives an example of a FLORIS-SE run with some default parameter settings, and compares the result to the SOWFA power results as  obtained in the paper:

P. Fleming, P. Gebraad, S. Lee, J.W. van Wingerden, K. Johnson, M. Churchfield, J. Michalakes, P. Spalart, and P. Moriarty.Simulation comparison of wake mitigation control strategies for a two-turbine case. Wind Energy, 2014.

In addition to Python packages already required by OpenMDAO (Numpy, Scipy, Matplotlib) this example requires the Pickle package.

## More information on the model

Relevant papers on the FLORIS model are:

P.M.O. Gebraad, F.W. Teeuwisse, J.W. van Wingerden, P.A. Fleming, S.D. Ruben, J.R. Marden, and L.Y. Pao. "Wind plant power optimization through yaw control using a parametric model for wake effects - a CFD simulation study." Wind Energy, 2014.

.. which gives a description of the model and its parameters.

Pieter M.O. Gebraad, Jared J. Thomas, Andrew Ning, Paul A. Fleming, and Katherine Dykes. "Maximization of the annual energy production of wind power plants by optimization of layout and yaw-based wake control" (Pre-publication)

.. which gives a description of the rotor coupling included in this version of
FLORISSE.
