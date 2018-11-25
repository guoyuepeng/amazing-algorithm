# https://github.com/statsmodels/statsmodels

# very powerful!

# Linear regression models(Quantile regression,Weighted least squares...)
# Mixed Linear Model with mixed effects and variance components
# GLM: Generalized linear models with support for all of the one-parameter exponential family distributions
# Time Series Analysis: models for time series analysis(Seasonal ARIMA and ARIMAX models,Dynamic Factor models)
# Survival analysis

import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Load data
dat = sm.datasets.get_rdataset("Guerry", "HistData").data

# Fit regression model (using the natural log of one of the regressors)
results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=dat).fit()

# Inspect the results
print(results.summary())