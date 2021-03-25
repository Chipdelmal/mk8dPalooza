#!/bin/bash

# Data processing -------------------------------------------------------------
python preProcess.py
python similarity.py
# Plotting --------------------------------------------------------------------
python pltWaffle.py
