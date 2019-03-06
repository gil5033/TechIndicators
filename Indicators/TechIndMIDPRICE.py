from Indicators.TechIndicator import TechnicalIndicator
from talib import MIDPRICE
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorMIDPRICE(TechnicalIndicator):
    """
    Wrapper for the Midpoint Price over period from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/MIDPRICE.htm
    """

    def __init__(self, timeperiod=14):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorMIDPRICE, self).__init__()
        self.__timeperiod = timeperiod

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Midpoint Price over period technical indicator using a wrapper for the TA-lib

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

        output = DataFrame(MIDPRICE(high, low, self.__timeperiod))
        output.columns = ['MIDPRICE%d' % self.__timeperiod]
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return self.__timeperiod
