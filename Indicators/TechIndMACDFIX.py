from Indicators.TechIndicator import TechnicalIndicator
from talib import MACDFIX
from pandas import DataFrame
from pandas import concat
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorMACDFIX(TechnicalIndicator):
    """
    Wrapper for the Moving Average Convergence/Divergence from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/MACD.htm
    """

    def __init__(self, signalperiod=9):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorMACDFIX, self).__init__()
        self.__signalperiod = signalperiod

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

        macd, macdsignal, macdhist = MACDFIX(close, self.__signalperiod)

        macd = DataFrame(macd)
        macdsignal = DataFrame(macdsignal)
        macdhist = DataFrame(macdhist)

        macd.colmuns = ['macd%d' % self.__signalperiod]
        macdsignal.colmuns = ['macdsignal%d' % self.__signalperiod]
        macdhist.colmuns = ['macdhist%d' % self.__signalperiod]

        return concat([macd, macdsignal, macdhist], axis=1, ignore_index=True)

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return self.__signalperiod
