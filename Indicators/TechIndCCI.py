from TechIndicator import TechnicalIndicator
from talib import CCI
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorCCI(TechnicalIndicator):
    """
    Wrapper for the Commodity Channel Index from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/CCI.htm
    """

    def __init__(self, timeperiod=14):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorCCI, self).__init__()
        self.__timeperiod = timeperiod

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Commodity Channel Index using a wrapper for the TA-lib

        Args:
            :param OHLCV_input:  the dataframe with the Open, High, Low, Close and Volume values
            :type OHLCV_input: pandas DataFrame

        Returns:
            DataFrame with scaled features with size (n_observations, n_features).
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

        output = DataFrame(CCI(high, low, close, self.__timeperiod))
        output.columns = ['CCI%d' % self.__timeperiod]
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application
        return self.__timeperiod
