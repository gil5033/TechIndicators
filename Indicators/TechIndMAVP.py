from Indicators.TechIndicator import TechnicalIndicator
from talib import MAVP
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorMAVP(TechnicalIndicator):
    """
    Wrapper for the Moving average with variable period from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
    """

    def __init__(self, periods=14, minperiod=2, maxperiod=30):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorMAVP, self).__init__()
        self.__periods = periods
        self.__minperiod = minperiod
        self.__maxperiod = maxperiod

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Moving average with variable period technical indicator using a wrapper for the TA-lib

        Args:
            :param OHLCV_input:  the dataframe with the Open, High, Low, Close and Volume values
            :type OHLCV_input: pandas DataFrame

        Returns:
            DataFrame with the indicators values.
        """
        try:
            close = OHLCV_input['close'].values[:, 0]
        except IndexError:
            close = OHLCV_input['close'].values

        return DataFrame(MAVP(close, periods=self.__periods, minperiod=self.__minperiod,
                              maxperiod=self.__maxperiod))

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return int(max(self.__periods, self.__minperiod, self.__maxperiod, self.__matype))
