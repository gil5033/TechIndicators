from TechIndicator import TechnicalIndicator
from talib import ADD
from pandas import DataFrame
__author__ = 'Pedro Veronezi'


class TechnicalIndicatorADD(TechnicalIndicator):
    """
    Wrapper for the ADD - Vector Arithmetic Add from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
    """

    def __init__(self, timeperiod=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorADD, self).__init__()
        self.__timeperiod = timeperiod

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the ADD - Vector Arithmetic Add using a wrapper for the TA-lib

        Args:
            :param OHLCV_input:  the dataframe with the Open, High, Low, Close and Volume values
            :type OHLCV_input: pandas DataFrame

        Returns:
            DataFrame with the indicators values.
        """
        try:
            high = OHLCV_input['high'].values[:, 0]
        except IndexError:
            high = OHLCV_input['high'].values

        try:
            low = OHLCV_input['low'].values[:, 0]
        except IndexError:
            low = OHLCV_input['low'].values

        output = DataFrame(ADD(high, low))
        output.columns = ['ADD%d' % self.__timeperiod]
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application
        return self.__timeperiod
