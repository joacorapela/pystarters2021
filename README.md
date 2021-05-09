# PyStarters 2021: hands-on practice with git/Github, Python functions and neural data analysis (May 13)

## Material

This session will only use a text editor to write code and a terminal to run it (no PyCharm needed). We will cover:

1. Basic use of git and Github (clone, commit, status, checkout, push, pull).

2. Python functions, positional and keyword arguments.

3. Use of functions to visualize electrophysiological recordings and linear regression to learn about them.

We will experiment with the following packages:

- `pandas` for data manipulation
- `matplotlib` for visualizations
- `statsmodels` for linear regression

and with code organization in modules.

## Neural recordings

We will characterize electrophysiological recordings from mice in the experiment depicted in the figure below probing the integration of visual and vestibular information across the brain.

![visVesIntegration](doc/figures/visVesIntegration.png)

## Pre-session setup

Please before the session do the following:

1. install git following the instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

2. in a terminal type `conda activate pystarters` (change `pystarters` with the name that you used for the conda environment you created for the course).

3. in the terminal type `conda install statsmodels`

4. in the terminal type `cd <pystarters directory>` where `<pystarters directory>` is the directory you created for the course.

5. in the terminal type `git clone git@github.com:joacorapela/pystarters2021.git`

6. in the terminal type `cd pystarters2021/code/scripts`

5. in the terminal type `python doFirstPlot.py Visual`.

If your setup is correct, the last command command should create the plot ../../figures/spikeRateVsabsSpeedV1Visual.png If this plot is not created please email [Joaquin Rapela](mailto:j.rapela@ucl.ac.uk)

