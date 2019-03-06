from Indicators.TechIndicator import TechnicalIndicator
from talib import MACDEXT
from pandas import DataFrame
from pandas import concat
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorMACDEXT(TechnicalIndicator):
    """
    Wrapper for theMoving Average Convergence/Divergence from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/MACD.htm
    """

    def __init__(self, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorMACDEXT, self).__init__()
        self.__fastperiod = fastperiod
        self.__fastmatype = fastmatype
        self.__slowperiod = slowperiod
        self.__slowmatype = slowmatype
        self.__signalperiod = signalperiod
        self.__signalmatype = signalmatype

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Moving Average Convergence/Divergence using a wrapper for the TA-lib

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

        macd, macdsignal, macdhist = MACDEXT(close, self.__fastperiod, self.__fastmatype, self.__slowperiod,
                                             self.__slowmatype, self.__signalperiod, self.__signalmatype)

        macd = DataFrame(macd)
        macdsignal = DataFrame(macdsignal)
        macdhist = DataFrame(macdhist)

        return concat([macd, macdsignal, macdhist], axis=1, ignore_index=True)

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return int(max(self.__fastperiod, self.__fastmatype, self.__slowperiod, self.__slowmatype, self.__signalperiod,
                       self.__signalmatype))
