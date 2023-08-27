from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA

mae_series    # locate best_p
best_p = 28

# build and train model
best_model = AutoReg(y_train, lags=best_p).fit()

# calculate training residuals for best_model
y_train_resid = best_model.resid
y_train_resid.name = "residuals"
y_train_resid.head()

# sample output
timestamp
2018-01-02 07:00:00+03:00    1.732488
2018-01-02 08:00:00+03:00   -0.381568
2018-01-02 09:00:00+03:00   -0.560971
2018-01-02 10:00:00+03:00   -2.215760
2018-01-02 11:00:00+03:00    0.006468
Freq: H, Name: residuals, dtype: float64
