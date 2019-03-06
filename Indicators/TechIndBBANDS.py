from TechIndicator import TechnicalIndicator
from talib import BBANDS
from pandas import DataFrame
from pandas import concat
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorBBANDS(TechnicalIndicator):
    """
    Wrapper for the Bollinger Bands from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.investopedia.com/terms/b/bollingerbands.asp
        http://www.tadoc.org/indicator/BBANDS.htm
    """

    def __init__(self, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorBBANDS, self).__init__()
        self.__timeperiod = timeperiod
        self.__nbdevup = nbdevup
        self.__nbdevdn = nbdevdn
        self.__matype = matype

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Bollinger bands technical indicator using a wrapper for the TA-lib

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
        upperband, middleband, lowerband = BBANDS(close, self.__timeperiod, self.__nbdevup, self.__nbdevdn,
                                                  self.__matype)
        upperband = DataFrame(upperband)
        middleband = DataFrame(middleband)
        lowerband = DataFrame(lowerband)

        return concat([upperband, middleband, lowerband], axis=1, ignore_index=True)

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application
        return int(max(self.__timeperiod, self.__nbdevup, self.__nbdevdn, self.__matype))

