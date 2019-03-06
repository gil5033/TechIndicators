from Indicators.TechIndicator import TechnicalIndicator
from talib import WMA
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorWMA(TechnicalIndicator):
    """
    Wrapper for the Weighted Moving Average period from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/WMA.htm
    """

    def __init__(self, timeperiod=30):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorWMA, self).__init__()
        self.__timeperiod = timeperiod

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Weighted Moving Average technical indicator using a wrapper for the TA-lib

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

        output = DataFrame(WMA(close, self.__timeperiod))
        output.columns = ['WMA%d' % self.__timeperiod]
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application
        return self.__timeperiod
