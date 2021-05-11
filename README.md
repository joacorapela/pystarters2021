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

We will characterize electrophysiological recordings from mice in the experiment depicted in the figure below probing the integration of visual and vestibular information across the brain ([Keshavarzi, Tyson, Lenzi et al., 2021](https://www.biorxiv.org/content/10.1101/2021.01.22.427789v4.abstract)).

![visVesIntegration](doc/figures/visVesIntegration.png)

## Pre-session setup

Please before the session do the following.

1. create a Github account (if you don't have one) [here](https://github.com/join)

2. install git

    - **Windows**

       Follow the instructions [here](https://phoenixnap.com/kb/how-to-install-git-windows) and **Launch Git Bash Shell** as mentioned in section **How to Launch Git in Windows** of the instructions.

       Use the git bash shell as the terminal in the following instructions.

       Follow the instructions [here](https://discuss.codecademy.com/t/setting-up-conda-in-git-bash/534473) to integrate conda with git.

    - **Linux and Mac** 

        Follow the instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

3. in a terminal (or Git Bash Shell if you use Windows) type `conda activate pystarters` (change `pystarters` to the name that you used for the conda environment you created for the course).

4. in the terminal type:

    - `pip install matplotlib`
    - `pip install statsmodels`
    - `pip install pandas`

5. in the terminal type `cd <pystarters directory>` where `<pystarters directory>` is the directory you created for the course.

6. in the terminal type `git clone https://github.com/joacorapela/pystarters2021.git`

7. in the terminal type `cd pystarters2021/code/scripts`

8. in the terminal type `python doFirstPlot.py Visual`.

If your setup is correct, the last command command should create the plot `<pystarters directory>/figures/spikeRateVsabsSpeedV1Visual.png`. If this plot is not created please email [Joaquin Rapela](mailto:j.rapela@ucl.ac.uk) to troubleshoot the problem.

