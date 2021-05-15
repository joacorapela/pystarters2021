
import sys
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def plot_panel(condition, data, ax):
    # Extract the subset of the data corresponding to the condition
    # and recordings from V1
    dataSubset = data.loc[(data["Trial Condition"]==condition) &
                          (data["Region"]=="V1"),:]
    x = abs(dataSubset["Speed"])
    y = dataSubset["Spike Rate"]

    # Plot the spikes rate as a function of the absolute value of the
    # stimulation speed
    ax.scatter(x=x, y=y, c="lightgray")

    # Estimate the regression line
    regressors = sm.add_constant(x)
    # fit.params contains the regression coefficients
    # fit.pvalues contains the regression coefficients pvalues
    fit = sm.OLS(endog=y, exog=regressors).fit()

    # Plot the regression line
    legend = "p={:.4f}".format(fit.pvalues[1])
    predicted = fit.params[0]+x*fit.params[1] # line equation
    ax.plot(x, predicted, color="red", label=legend)
    ax.legend(loc="upper left")
    ax.set_xlabel("Abs(Speed)")
    ax.set_ylabel("Spike Rate")
    ax.set_title(condition)

def main(argv):
    dataFilename = "../../data/All_three_exp_conditions_4.csv"
    figFilename = "../../figures/spikeRateVsabsSpeedV1_allConditions.png"
    data = pd.read_csv(dataFilename, index_col=0)

    fig, axs = plt.subplots(3, 1)

    plot_panel(condition="Visual", data=data, ax=axs[0])
    plot_panel(condition="Vestibular", data=data, ax=axs[1])
    plot_panel(condition="VisVes", data=data, ax=axs[2])

    plt.savefig(figFilename)

    plt.show()

if __name__=="__main__":
    main(sys.argv)
