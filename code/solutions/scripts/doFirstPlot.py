
import pdb
import sys
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def main(argv):
    if len(argv)!=2 or argv[1] not in ("Visual", "Vestibular", "VisVes"):
        raise ValueError("Invalid invokation. It should be: {:s} <Visual|Vestibular|VisVes>".format(argv[0]))

    condition = argv[1]
    dataFilename = "../../data/All_three_exp_conditions_4.csv"
    figFilename = "../../figures/spikeRateVsabsSpeedV1{:s}.png".format(condition)
    data = pd.read_csv(dataFilename, index_col=0)

    # Extract the subset of the data corresponding to vestibular-only stimulation
    # and recordings from V1
    dataSubset = data.loc[(data["Trial Condition"]==condition) &
                          (data["Region"]=="V1"),:]
    x = abs(dataSubset["Speed"])
    y = dataSubset["Spike Rate"],

    # Plot the spikes rate as a function of the absolute value of the
    # stimulation speed
    plt.scatter(x=x, y=y, c="lightgray")
    plt.title(condition)

    # Estimate the regression line
    regressors = sm.add_constant(x)
    # fit.params contains the regression coefficients
    # fit.pvalues contains the regression coefficients pvalues
    fit = sm.OLS(endog=y, exog=regressors).fit()

    # Plot the regression line
    legend = "p={:.4f}".format(fit.pvalues[1])
    predicted = fit.params[0]+x*fit.params[1] # line equation
    plt.plot(x, predicted, color="red", label=legend)
    plt.legend(loc="upper left")
    plt.xlabel("Abs(Speed)")
    plt.ylabel("Spike Rate")

    plt.savefig(figFilename)

    plt.show()

    pdb.set_trace()

if __name__=="__main__":
    main(sys.argv)
