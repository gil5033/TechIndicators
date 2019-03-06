from Indicators.TechIndicator import TechnicalIndicator
from talib import MAMA
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorMAMA(TechnicalIndicator):
    """
    Wrapper for the MESA Adaptive Moving Average from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/MAMA.htm
    """

    def __init__(self, fastlimit=0, slowlimit=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorMAMA, self).__init__()
        self.__fastlimit = fastlimit
        self.__slowlimit = slowlimit

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the EMA technical indicator using a wrapper for the TA-lib

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

        return DataFrame(MAMA(close, self.__fastlimit, self.__slowlimit))

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return int(max(self.__fastlimit, self.__slowlimit))
