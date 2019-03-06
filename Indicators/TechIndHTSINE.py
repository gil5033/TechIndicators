from TechIndicator import TechnicalIndicator
from talib import HT_SINE
from pandas import DataFrame
from pandas import concat
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorHTSINE(TechnicalIndicator):
    """
    Wrapper for the Hilbert Transform - SineWave period from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/HT_SINE.htm
    """

    def __init__(self, timeperiod=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorHTSINE, self).__init__()
        self.__timeperiod = timeperiod

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Hilbert Transform - SineWave technical indicator using a wrapper for the TA-lib

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

        sine, leadsine = HT_SINE(close)

        sine = DataFrame(sine)
        leadsine = DataFrame(leadsine)

        sine.columns = ['HTSINE_sine%d' % self.__timeperiod]
        leadsine.columns = ['HTSINE_leadsine%d' % self.__timeperiod]

        output = concat([sine, leadsine], axis=1)

        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return self.__timeperiod
