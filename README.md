# MK8D: Luma Invitational

`main.sh` script runs the whole pipeline, which consists of the following steps:

0. `constant.py`: Runs the constants for color, votes, tracks names, and related snips necessary for all the plots.
1. `preProcess.py`: Parses the votes and converts them to a dataframe with some summary statistics.
2. `similarity.py`: Generates the distance matrix between the participant's vectors.
3. `matrix.py`: Plots the distance and relative-rank matrices.
4. `dendrogram.py`: Generates and plots the dendrogram of the participants.
5. `chord.py`: Plots the chord diagram for the participants.
6. `waffle.py`: Plots the votes results for all the tracks and players.
