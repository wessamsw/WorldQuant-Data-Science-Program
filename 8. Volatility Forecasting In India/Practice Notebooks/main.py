import os
from glob import glob

import joblib
import pandas as pd
from scipy.stats import norm
import numpy as np
from arch import arch_model
from config import settings
from data import AlphaVantageAPI, SQLRepository


class GarchModel:
    """Class for training GARCH model and generating predictions.

    Atttributes
    -----------
    ticker : str
        Ticker symbol of the equity whose volatility will be predicted.
    repo : SQLRepository
        The repository where the training data will be stored.
    use_new_data : bool
        Whether to download new data from the AlphaVantage API to train
        the model or to use the existing data stored in the repository.
    model_directory : str
        Path for directory where trained models will be stored.

    Methods
    -------
    wrangle_data
        Generate equity returns from data in database.
    fit
        Fit model to training data.
    predict
        Generate volatilty forecast from trained model.
    dump
        Save trained model to file.
    load
        Load trained model from file.
    """

    def __init__(self, ticker,repo,use_new_data):
    
        self.ticker = ticker
        self.repo = repo
        self.use_new_data = use_new_data
        self.model_directory = settings.model_directory

    def wrangle_data(self,n_observations):

        """Extract data from database (or get from AlphaVantage), transform it
        for training model, and attach it to `self.data`.

        Parameters
        ----------
        n_observations : int
            Number of observations to retrieve from database

        Returns
        -------
        None
        """
        if self.use_new_data:
            api=AlphaVantageAPI()
            new_data=api.get_daily(ticker=self.ticker)
            self.repo.insert_table(
                table_name=self.ticker,records=new_data,if_exists="replace")    
        df=self.repo.read_table(table_name = self.ticker, limit=n_observations+1)
        df.sort_index(ascending=True,inplace=True)
        df['return']=df['close'].pct_change()*100
        self.data=df["return"].dropna()

    def calculate_aic(self):
        log_likelihood = self.model.loglikelihood
        num_params = self.model.num_params
        n = len(self.data)
        return -2 * log_likelihood / n + 2 * num_params / n
        
    def calculate_bic(self):
        log_likelihood = self.model.loglikelihood
        num_params = self.model.num_params
        n = len(self.data)
        return -2 * log_likelihood / n + num_params * np.log(n) / n

    def fit(self,p,q):

        """Create model, fit to `self.data`, and attach to `self.model` attribute.
        For assignment, also assigns adds metrics to `self.aic` and `self.bic`.

        Parameters
        ----------
        p : int
            Lag order of the symmetric innovation

        q : ind
            Lag order of lagged volatility

        Returns
        -------
        None
        """
        # Train Model, attach to `self.model`
        self.model = arch_model(self.data, p=p, q=q, rescale=False).fit(disp=0)

        # Calculate AIC and BIC
        aic = self.calculate_aic()
        bic = self.calculate_bic()

        # Add AIC and BIC attributes to the object
        self.aic = aic
        self.bic = bic
        

    def __clean_prediction(self, prediction):

        """Reformat model prediction to JSON.

        Parameters
        ----------
        prediction : pd.DataFrame
            Variance from a `ARCHModelForecast`

        Returns
        -------
        dict
            Forecast of volatility. Each key is date in ISO 8601 format.
            Each value is predicted volatility.
        """
        # Calculate forecast start date
        start= prediction.index[0] + pd.DateOffset(days=1)

        # Create date range
        prediction_dates= pd.bdate_range(start=start, periods=prediction.shape[1])

        # Create prediction index labels, ISO 8601 format
        prediction_index= [d.isoformat() for d in prediction_dates]

        # Extract predictions from DataFrame, get square root
        data = prediction.values.flatten() ** 0.5

        # Combine `data` and `prediction_index` into Series
        prediction_formatted = pd.Series(data, index=prediction_index)

        # Return Series as dictionary
        return prediction_formatted.to_dict()

    
    def predict_volatility(self, horizon):

        """Predict volatility using `self.model`

        Parameters
        ----------
        horizon : int
            Horizon of forecast, by default 5.

        Returns
        -------
        dict
            Forecast of volatility. Each key is date in ISO 8601 format.
            Each value is predicted volatility.
        """
        # Generate variance forecast from `self.model`
        prediction = self.model.forecast(horizon=horizon, reindex=False).variance

        # Format prediction with `self.__clean_predction`
        prediction_formatted = self.__clean_prediction(prediction)

        # Return `prediction_formatted`
        return prediction_formatted
    
    
    def dump(self):

        """Save model to `self.model_directory` with timestamp.

        Returns
        -------
        str
            filepath where model was saved.
        """
        # Create timestamp in ISO format
        timestamp = pd.Timestamp.now().isoformat()
        # Create filepath, including `self.model_directory`
        filepath = os.path.join(self.model_directory, f"{timestamp}_{self.ticker}.pkl")
        # Save `self.model`
        joblib.dump(self.model,filepath)
        # Return filepath
        return filepath
    
    
    def load(self):

        """Load most recent model in `self.model_directory` for `self.ticker`,
        attach to `self.model` attribute.

        """
        # Create pattern for glob search
        pattern = os.path.join(settings.model_directory,f"*{self.ticker}.pkl")
        # Use glob to get most recent model, handle errors
        try:
            model_path = sorted(glob(pattern))[-1]
        except IndexError:
            raise Exception(f"No model trained for '{ticker}'.")    
        # Load model and attach to `self.model`
        self.model = joblib.load(model_path)
