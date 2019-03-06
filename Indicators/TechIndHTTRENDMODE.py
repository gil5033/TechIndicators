from TechIndicator import TechnicalIndicator
from talib import HT_TRENDMODE
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorHTTRENDMODE(TechnicalIndicator):
    """
    Wrapper for the Hilbert Transform - Trend vs Cycle Mode period from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/HT_TRENDMODE.htm
    """

    def __init__(self, timeperiod=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorHTTRENDMODE, self).__init__()
        self.__timeperiod = timeperiod

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Weighted Hilbert Transform - Trend vs Cycle Mode technical indicator using a wrapper for the TA-lib

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

        output = DataFrame(HT_TRENDMODE(close))
        output.columns = ['HT_TRENDMODE']
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return self.__timeperiod
