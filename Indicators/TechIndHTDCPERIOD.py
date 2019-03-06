from TechIndicator import TechnicalIndicator
from talib import HT_DCPERIOD
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorHTDCPERIOD(TechnicalIndicator):
    """
    Wrapper for the Hilbert Transform - Dominant Cycle Period period from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/HT_DCPERIOD.htm
    """

    def __init__(self, timeperiod=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorHTDCPERIOD, self).__init__()
        self.__timeperiod = timeperiod

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Weighted Hilbert Transform - Dominant Cycle Period technical indicator using a wrapper for the TA-lib

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

        output = DataFrame(HT_DCPERIOD(close))
        output.columns = ['HT_DCPERIOD']
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return self.__timeperiod
