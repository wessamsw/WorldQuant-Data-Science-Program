from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_absolute_error

# Use AR model to predict PM2.5 readings
# Hyperparameter --> p
p_params = range(1, 31)
maes = []
for p in p_params:
    #Train model
    model = AutoReg(y_train, lags=p).fit()
    
    #Generate in-sample pred
    y_pred = model.predict().dropna()
        
    #Calculate mae
    mae = mean_absolute_error(y_train.iloc[p:], y_pred)
    maes.append(mae)
    
mae_series = pd.Series(maes, name="mae", index=p_params)
mae_series.head()

# sample output
1    0.947888
2    0.933894
3    0.920850
4    0.920153
5    0.919519
Name: mae, dtype: float64
