
import statsmodels.api as sm

def plot_panel(condition, region, data, ax,
               xlabel="abs(Speed)", ylabel="Spike Rate",
               title=None, data_color="gray", regression_line_color="red",
               line_style="solid", legend_loc="upper left",
               legend_label_pattern="p={:.04f}"):
    # Extract the subset of the data corresponding to the condition
    # and recordings from V1
    dataSubset = data.loc[(data["Trial Condition"]==condition) &
                          (data["Region"]==region),:]
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
    if ax.is_last_row():
        ax.set_xlabel(xlabel)
    if ax.is_first_col() and not ax.is_first_row() and not ax.is_last_row():
        ax.set_ylabel(ylabel)
    if title is None:
        title = "{:s}: {:s}".format(condition, region)
    ax.set_title(title)
