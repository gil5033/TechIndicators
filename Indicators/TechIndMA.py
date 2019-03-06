from Indicators.TechIndicator import TechnicalIndicator
from talib import MA
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorMA(TechnicalIndicator):
    """
    Wrapper for the MA from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/MA.htm
    """

    def __init__(self, timeperiod=30, matype=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorMA, self).__init__()
        self.__timeperiod = timeperiod
        self.__matype = matype

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

        output = DataFrame(MA(close, self.__timeperiod, self.__matype))
        output.columns = ['MA%d' % self.__timeperiod]

        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return self.__timeperiod
