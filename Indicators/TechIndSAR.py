from Indicators.TechIndicator import TechnicalIndicator
from talib import SAR
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorSAR(TechnicalIndicator):
    """
    Wrapper for the SAR - Parabolic SAR period from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/SAR.htm
    """

    def __init__(self, acceleration=0, maximum=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorSAR, self).__init__()
        self.__acceleration = acceleration
        self.__maximum = maximum

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the SAR - Parabolic SAR technical indicator using a wrapper for the TA-lib

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

        output = DataFrame(SAR(high, low, self.__acceleration, self.__maximum))
        output.columns = ['SAR%d' % self.__acceleration]
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return int(max(self.__acceleration, self.__maximum))
