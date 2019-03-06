from Indicators.TechIndicator import TechnicalIndicator
from talib import STOCHF
from pandas import DataFrame
from pandas import concat
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorSTOCHF(TechnicalIndicator):
    """
    Wrapper for the Stochastic from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/STOCHF.htm
    """

    def __init__(self, fastk_period=5, fastd_period=3, fastd_matype=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorSTOCHF, self).__init__()
        self.__fastk_period = fastk_period
        self.__fastd_period = fastd_period
        self.__fastd_matype = fastd_matype

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Stochastic technical indicator using a wrapper for the TA-lib

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

        fastk, fastd = STOCHF(high, low, close, self.__fastk_period, self.__fastd_period, self.__fastd_matype)

        fastk = DataFrame(fastk)
        fastd = DataFrame(fastd)

        fastk.columns = ['fastk%d_%d' % (self.__fastk_period, self.__fastd_period)]
        fastd.columns = ['fastd%d_%d' % (self.__fastk_period, self.__fastd_period)]

        output = concat([fastk, fastd], axis=1, ignore_index=True)
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return int(max(self.__fastk_period, self.__fastd_period, self.__fastd_matype))
