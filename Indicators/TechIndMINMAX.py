from Indicators.TechIndicator import TechnicalIndicator
from talib import MINMAX
from pandas import DataFrame
from pandas import concat
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorMINMAX(TechnicalIndicator):
    """
    Wrapper for the Lowest and highest values over a specified period from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/HT_SINE.htm
    """

    def __init__(self, timeperiod=30):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorMINMAX, self).__init__()
        self.__timeperiod = timeperiod

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Lowest and highest values over a specified period technical indicator using a wrapper for the
        TA-lib

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

        min, max = MINMAX(close, self.__timeperiod)

        min = DataFrame(min)
        max = DataFrame(max)

        min.columns = ['MINMAX_MIN%d' % self.__timeperiod]
        max.columns = ['MINMAX_MAX%d' % self.__timeperiod]

        output = concat([min, max], axis=1, ignore_index=True)
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return self.__timeperiod
