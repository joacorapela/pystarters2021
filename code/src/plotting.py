
import statsmodels.api as sm

def plot_panel(condition, data, ax, title=None, region="V1"):
    # Extract the subset of the data corresponding to the condition
    # and recordings from V1
    dataSubset = data.loc[(data["Trial Condition"]==condition) &
                          (data["Region"]==region),:]
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
    title = "{:s}: {:s}".format(region, condition)
    ax.set_title(title)

