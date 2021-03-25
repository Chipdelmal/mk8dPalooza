#!/bin/bash

# Data processing -------------------------------------------------------------
python preProcess.py
python similarity.py
# Plotting --------------------------------------------------------------------
python matrix.py
python dendrogram.py
python chord.py
python waffles.py
