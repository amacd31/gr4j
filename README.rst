Python GR4J
===============

Pure Python implementation of the GR4J hydrologic rainfall-runoff model.

Dependencies
------------

Requires Python 2.6 or greater (mostly tested with Python 2.7 on Linux).

If Cython is available the Python code will be compiled by Cython during
installation. Running the unit tests requires numpy and pandas. These
dependencies are all optional as the base code is pure Python.

Installation
------------

Install from Github::

 pip install git+https://github.com/amacd31/gr4j.git


Usage
-----

A single method that takes input rainfall and potential evapotranspiration data, a parameters dictionary and optional starting state.

See Perrin et al. 2003 paper (referenced below) on the parameters for the model.

::

 from gr4j import gr4j
 params = { 'X1': 303.627616, 'X2': 0.32238919, 'X3': 6.49759466, 'X4': 0.294803885 }
 states = { 'production_store': 0.60 * params['X1'], 'routing_store': 0.70 * params['X3'] }
 rainfall = [ 14.1, 3.7, 7.1, 9.3 ]
 potential_evap = [ 0.46, 0.46, 0.47, 0.47 ]

 simulated_flow = gr4j(rainfall, potential_evap, params, states)

Notes
-----

Implemented as a learning exercise. Code based on the paper 2003 paper by
Perrin et al. and the website summary of the model. Initial results compared to
the output of the Excel version of GR4J:
https://gitlab.irstea.fr/HYCAR-Hydro/ExcelGR/raw/master/GR4J/GR4J_EN.xlsx

The design of a single functional method was chosen as part of this learning
exercise with a mind to later implement an OpenCL version in C for parallel
usage. Later work may update the design of this package, but that is not
currently planned for the near future.

References
----------

Perrin, Charles, Claude Michel, and Vazken Andréassian. "Improvement of a parsimonious model for streamflow simulation." Journal of Hydrology 279, no. 1 (2003): 275-289.

Operation of GR4J: https://webgr.inrae.fr/en/models/daily-hydrological-model-gr4j/description-of-the-gr4j-model/
