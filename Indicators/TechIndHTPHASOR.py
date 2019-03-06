from TechIndicator import TechnicalIndicator
from talib import HT_PHASOR
from pandas import DataFrame
from pandas import concat
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorHTPHASOR(TechnicalIndicator):
    """
    Wrapper for the Hilbert Transform - Phasor Components Phase period from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/HT_PHASOR.htm
    """

    def __init__(self, timeperiod=0):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorHTPHASOR, self).__init__()
        self.__timeperiod = timeperiod

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Weighted Hilbert Transform - Phasor Components technical indicator using a wrapper for the TA-lib

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

        inphase, quadrature = HT_PHASOR(close)

        inphase = DataFrame(inphase)
        quadrature = DataFrame(quadrature)

        inphase.columns = ['inphase_HT_PHASOR']
        quadrature.columns = ['quadrature_HT_PHASOR']

        return concat([inphase, quadrature], axis=1, ignore_index=True)

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application

        return self.__timeperiod
