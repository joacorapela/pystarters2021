
. describe experiment

. doInspectData.py
. doFirstPlot.py: describe the code in some detail
    . python doFirstPlot.py Visual
    . python doFirstPlot.py Vestibular
    . python doFirstPlot.py VisVes
. three panels in one plot:
    . doPlotsCodeFromHell.py
. cp ./doPlotsCodeFromHell.py ./doPlotsCodeFromHellImproved.py
    Exercise:
        . create function plot_panel and modify the code to use it
        . git status
        . git add and commit ./doPlotsCodeFromHellImproved.py

. talk about code organization and modules
  create plotting module
  move plot_panel to plotting
  import plotting into ./doPlotsCodeFromHellImproved.py
    Exercise:
        . git status
        . add and commit ../src/plotting.py
        . add and commit ./doPlotsCodeFromHellImproved.py

. Exercise:
    . replace the three calls to plot_panel with a for loop
    . git status
    . add and commit ./doPlotsCodeFromHellImproved.py

. Exercise:
    . generate a plot with three rows and two columns. In the left column show Region=V1 and in the right column show Region=RSPg. For this you could to add a parameter region to plot_panel.
    . git status
    . add and commit ../src/plotting.py
    . add and commit ./doPlotsCodeFromHellImproved.py

. Show:
    . git diff: compare the version of ./doPlotsCodeFromHellImproved.py in the working directory with that in the previous commit.
    . git checkout: go back to the previous version.
    . git push
