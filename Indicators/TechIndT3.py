from Indicators.TechIndicator import TechnicalIndicator
from talib import T3
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorT3(TechnicalIndicator):
    """
    Wrapper for the Triple Exponential Moving Average (T3) period from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/T3.htm
    """

    def __init__(self, timeperiod=5, vfactor=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorT3, self).__init__()
        self.__timeperiod = timeperiod
        self.__vfactor = vfactor

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Triple Exponential Moving Average (T3) technical indicator using a wrapper for the TA-lib

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

        output = DataFrame(T3(close, self.__timeperiod, self.__vfactor))
        output.columns = ['T3%d' % self.__timeperiod]
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return int(max(self.__timeperiod, self.__vfactor))
