from Indicators.TechIndicator import TechnicalIndicator
from talib import ULTOSC
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorULTOSC(TechnicalIndicator):
    """
    Wrapper for the Ultimate Oscillator Rating from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/TRIX.htm
    """

    def __init__(self, timeperiod1=7, timeperiod2=14, timeperiod3=28):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorULTOSC, self).__init__()
        self.__timeperiod1 = timeperiod1
        self.__timeperiod2 = timeperiod2
        self.__timeperiod3 = timeperiod3

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Ultimate Oscillator technical indicator using a wrapper for the TA-lib

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

        try:
            close = OHLCV_input['close'].values[:, 0]
        except IndexError:
            close = OHLCV_input['close'].values

        output = DataFrame(ULTOSC(high, low, close, self.__timeperiod1, self.__timeperiod2, self.__timeperiod3))
        output.columns = ['ULTOSC%d_%d_%d' % (self.__timeperiod1, self.__timeperiod2, self.__timeperiod3)]
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return int(max(self.__timeperiod1, self.__timeperiod2, self.__timeperiod3))
