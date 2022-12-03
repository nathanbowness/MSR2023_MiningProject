# T-Flows 

T-Flows (stands for Turbulent Flows) is a Computational Fluid Dynamics (CFD) program, originally developed at Delft University of Technology, the Netherlands.  It features second order accurate, unstructured, cell-centered, finite volume discretization of incompressible Navier-Stokes equations with heat transfer and species transport.  It is written in Fortran 90 and uses Message Passing Interface (MPI) for parallel execution.

## Basic Features: 

*	Unstructured (cell-centered) grid, arbitrary cell shapes, second order accuracy in space 
*	Linear solvers: preconditioned conjugate gradient, bi-conjugate-gradient and conjugate gradient squared
*	Eddy-viscosity and second moment closure Reynolds-Averaged Navier-Stokes (RANS) models
*	Large Eddy Simulation (LES) with Smagorinsky, Dynamic and Wall-Adapting Local Eddy viscosity (WALE) models for sub-grid scales (SGS) 
*	Hybrid RANS/LES methods
*	Conventional and advanced treatment of wall boundary conditions (wall integration, wall functions with roughness, compound wall treatment, blending wall function and wall integration approach)
*	Compatibility with several open-source and commercial grid generators

## Following turbulence models are currently implemented:

* Linear eddy-viscosity k-ε models
  * Standard high-Re
  * Low-Re version (Abe, Kondoh and Nagano) with compound wall treatment
* Elliptic-relaxation eddy-viscosity model
  * Linear ζ − f with compound wall treatment
* Second-moment closures full Reynolds-stress models
  * Elliptic blending model (Manceau-Hanjalic)
  * Hanjalic-Jakirlic model
  * Hybrid linear eddy-viscosity and second-moment closure model (Basara-Jakirlic)
* LES
  * Smagorinsky SGS model
  * Dynamic Smagorinsky SGS model
  * WALE SGS model
* Hybrid LES/RANS
  * Detached eddy simulation (Spalart-Allmaras)
  * Hybrid LES/RANS ζ − f model

All RANS models can be ran in unsteady mode, thus effectively becoming Unsteady RANS (URANS) model.

## Software Requirements

Compilation of the main program and sub-programs depends on the following tools: 
ld, make, gfortran, git and mpi (only for parallel execution).

Compilation was tested with the following tools and versions:
- ld >= 2.24
- gfortran >= 4.8
- mpich >= 3.0.4
- openmpi >= 1.6.5
- make >= 3.81
- git >= 1.91

## Availability

The code is currently available under MIT license.  To download the current version of the code use:

 git clone https://github.com/DelNov/T-Flows/

## Basic Architecture

Code has four sub-programs at the moment and uses own proprietary format for computational grids (.geo, .cns).
- Generate -  use to generate mesh from ASCII .dom to own format.
- Convert  -  use to convert mesh from .neu, .cgns to own format.
- Divide   -  use to partition the mesh for parallel execution.
- Process  -  use to solve discretized Navier-Stokes equations.

Compiled programs are placed in the Binaries/ folder.

Sources are located in
Sources/Generate/
Sources/Convert/
Sources/Divide/
Sources/Process/

Tests/ folder contains files needed to run several standard benchmark cases for RANS, LES and hybrid methods. Xmgrace sources with referent DNS or experimental data are provided for the most of the test cases, as well as user functions for post-processing of data.

The program produces files in vtu format that can be open by ParaView open-source software for postprocessing. 
