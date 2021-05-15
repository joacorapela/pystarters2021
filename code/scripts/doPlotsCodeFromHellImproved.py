
import sys
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def plot_panel(condition, data, ax, xlabel="abs(Speed)", ylabel="Spike Rate", 
               title=None, data_color="gray", regression_line_color="red",
               line_style="solid", legend_loc="upper left",
               legend_label_pattern="p={:.04f}"):
    # Extract the subset of the data corresponding to the condition
    # and recordings from V1
    dataSubset = data.loc[(data["Trial Condition"]==condition) &
                          (data["Region"]=="V1"),:]
    x = abs(dataSubset["Speed"])
    y = dataSubset["Spike Rate"]

    # Plot the spikes rate as a function of the absolute value of the
    # stimulation speed
    ax.scatter(x=x, y=y, color=data_color, linestyle=line_style)

    # Estimate the regression line
    regressors = sm.add_constant(x)
    # fit.params contains the regression coefficients
    # fit.pvalues contains the regression coefficients pvalues
    fit = sm.OLS(endog=y, exog=regressors).fit()

    # Plot the regression line
    legend_label = legend_label_pattern.format(fit.pvalues[1])
    predicted = fit.params[0]+x*fit.params[1] # line equation
    ax.plot(x, predicted, color=regression_line_color, label=legend_label)
    ax.legend(loc=legend_loc)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if title is None:
        title = condition
    ax.set_title(title)

def main(argv):
    dataFilename = "../../data/All_three_exp_conditions_4.csv"
    figFilename = "../../figures/spikeRateVsabsSpeedV1_allConditions.png"
    data = pd.read_csv(dataFilename, index_col=0)

    fig, axs = plt.subplots(3, 1)

    plot_panel(condition="Visual", data=data, ax=axs[0])
    plot_panel(condition="Vestibular", data=data, ax=axs[1])
    plot_panel(condition="VisVes", data=data, ax=axs[2],
               title="Visual + Vestibular")

    plt.savefig(figFilename)

    plt.show()

if __name__=="__main__":
    main(sys.argv)
