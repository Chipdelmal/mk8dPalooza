# MK8D: Luma Invitational

For a full breakdown of this story, follow: https://chipdelmal.github.io/blog/posts/mk8dsoulmates

![](https://chipdelmal.github.io/blog/uploads/sm_CH.png)

## Instructions

`main.sh` script runs the whole pipeline, which consists of the following steps:

0. `constant.py`: Runs the constants for color, votes, tracks names, and related snips necessary for all the plots.
1. `preProcess.py`: Parses the votes and converts them to a dataframe with some summary statistics.
2. `similarity.py`: Generates the distance matrix between the participant's vectors.
3. `matrix.py`: Plots the distance and relative-rank matrices.
4. `dendrogram.py`: Generates and plots the dendrogram of the participants.
5. `chord.py`: Plots the chord diagram for the participants.
6. `waffle.py`: Plots the votes results for all the tracks and players.

The scripts can be run independently provided that the dataframe has already been exported (and the distance matrix for the matrix plots).


## Dependencies

Required dependencies can be installed into an environment with the `./conda/REQUIREMENTS.txt`, `./conda/REQUIREMENTS.yml` or by running:

```
pip install numpy
pip install pandas
pip install matplotlib
pip install scipy
pip install pywaffle
pip install mpl-chord-diagram
```

<hr>

## Author

<img src="https://raw.githubusercontent.com/Chipdelmal/WaveArt/master/media/pusheen.jpg" height="130px" align="middle"><br>

[Héctor M. Sánchez C.](https://chipdelmal.github.io/)
