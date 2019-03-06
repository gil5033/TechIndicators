from Indicators.TechIndicator import TechnicalIndicator
from talib import STOCHRSI
from pandas import DataFrame
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorSTOCHRSI(TechnicalIndicator):
    """
    Wrapper for the Stochastic from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/STOCHRSI.htm
    """

    def __init__(self, fastk_period=5, fastd_period=3, fastd_matype=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorSTOCHRSI, self).__init__()
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
            close = OHLCV_input['close'].values[:, 0]
        except IndexError:
            close = OHLCV_input['close'].values

        output = DataFrame(STOCHRSI(close, self.__fastk_period, self.__fastd_period, self.__fastd_matype))
        output.columns = ['STOCHRSI%d_%d' % (self.__fastk_period, self.__fastd_period)]
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return int(max(self.__fastk_period, self.__fastd_period, self.__fastd_matype))
