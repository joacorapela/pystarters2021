
import pdb
import sys
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def main(argv):
    dataFilename = "../../data/All_three_exp_conditions_4.csv"
    figFilename = "../../figures/spikeRateVsabsSpeedV1_allConditions.png"
    data = pd.read_csv(dataFilename, index_col=0)

    fig, axs = plt.subplots(3)

    ### Visual
    condition = "Visual"
    axes_index = 0

    # Extract the subset of the data corresponding to the condition
    # and recordings from V1
    dataSubset = data.loc[(data["Trial Condition"]==condition) &
                          (data["Region"]=="V1"),:]
    x = abs(dataSubset["Speed"])
    y = dataSubset["Spike Rate"]

    # Plot the spikes rate as a function of the absolute value of the
    # stimulation speed
    axs[axes_index].scatter(x=x, y=y, c="lightgray")
    axs[axes_index].set_title(condition)

    # Estimate the regression line
    regressors = sm.add_constant(x)
    # fit.params contains the regression coefficients
    # fit.pvalues contains the regression coefficients pvalues
    fit = sm.OLS(endog=y, exog=regressors).fit()

    # Plot the regression line
    legend = "p={:.4f}".format(fit.pvalues[1])
    predicted = fit.params[0]+x*fit.params[1] # line equation
    axs[axes_index].plot(x, predicted, color="red", label=legend)
    axs[axes_index].legend(loc="upper left")
    axs[axes_index].set_xlabel("Abs(Speed)")
    axs[axes_index].set_ylabel("Spike Rate")

    ### Vestibular
    condition = "Vestibular"
    axes_index = 1

    # Extract the subset of the data corresponding to the condition
    # and recordings from V1
    dataSubset = data.loc[(data["Trial Condition"]==condition) &
                          (data["Region"]=="V1"),:]
    x = abs(dataSubset["Speed"])
    y = dataSubset["Spike Rate"]

    # Plot the spikes rate as a function of the absolute value of the
    # stimulation speed
    axs[axes_index].scatter(x=x, y=y, c="lightgray")

    # Estimate the regression line
    regressors = sm.add_constant(x)
    # fit.params contains the regression coefficients
    # fit.pvalues contains the regression coefficients pvalues
    fit = sm.OLS(endog=y, exog=regressors).fit()

    # Plot the regression line
    legend = "p={:.4f}".format(fit.pvalues[1])
    predicted = fit.params[0]+x*fit.params[1] # line equation
    axs[axes_index].plot(x, predicted, color="red", label=legend)
    axs[axes_index].legend(loc="upper left")
    axs[axes_index].set_xlabel("Abs(Speed)")
    axs[axes_index].set_ylabel("Spike Rate")
    axs[axes_index].set_title(condition)

    ### VisVes
    condition = "VisVes"
    axes_index = 2

    # Extract the subset of the data corresponding to the condition
    # and recordings from V1
    dataSubset = data.loc[(data["Trial Condition"]==condition) &
                          (data["Region"]=="V1"),:]
    x = abs(dataSubset["Speed"])
    y = dataSubset["Spike Rate"]

    # Plot the spikes rate as a function of the absolute value of the
    # stimulation speed
    axs[axes_index].scatter(x=x, y=y, c="lightgray")

    # Estimate the regression line
    regressors = sm.add_constant(x)
    # fit.params contains the regression coefficients
    # fit.pvalues contains the regression coefficients pvalues
    fit = sm.OLS(endog=y, exog=regressors).fit()

    # Plot the regression line
    legend = "p={:.4f}".format(fit.pvalues[1])
    predicted = fit.params[0]+x*fit.params[1] # line equation
    axs[axes_index].plot(x, predicted, color="red", label=legend)
    axs[axes_index].legend(loc="upper left")
    axs[axes_index].set_xlabel("Abs(Speed)")
    axs[axes_index].set_ylabel("Spike Rate")
    axs[axes_index].set_title(condition)

    plt.savefig(figFilename)

    plt.show()

    pdb.set_trace()

if __name__=="__main__":
    main(sys.argv)
