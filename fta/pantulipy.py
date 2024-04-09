# -*- coding:utf-8 -*-
import inspect as insp

import numpy as np
import pandas as pd
import tulipy

_OHLCV = ['open', 'high', 'low', 'close', 'volume']
_FUNCS = sorted([f for f in dir(tulipy) if f[0].islower() and 'lib' not in f])
_FUNCTIONS_REFERENCES = {fn: n for n, fn in enumerate(_FUNCS)}

# Added so you can loop through the rest by just inputting a dataframe
# These don't have useful default params we can put in.
_DEFAULTLESS_INDICATORS = ['decay', 'edecay', 'lag', 'volatility']

__all__ = ['ad', 'adosc', 'adx', 'adxr', 'ao', 'apo', 'aroon', 'aroonosc', 'atr', 'avgprice', 'bbands', 'bop', 'cci',
           'cmo', 'crossany', 'crossover', 'cvi', 'decay', 'dema', 'di', 'dm', 'dpo', 'dx', 'edecay', 'ema', 'emv',
           'fisher', 'fosc', 'hma', 'kama', 'kvo', 'lag', 'linreg', 'linregintercept', 'linregslope', 'macd',
           'marketfi', 'mass', 'md', 'mfi', 'mom', 'msw', 'natr', 'nvi', 'obv', 'ppo', 'psar', 'pvi', 'qstick',
           'roc', 'rocr', 'rsi', 'sma', 'stderr', 'stoch', 'tema', 'tr', 'trima', 'trix', 'tsf', 'typprice', 'ultosc',
           'vhf', 'vidya', 'volatility', 'vosc', 'vwma', 'wad', 'wcprice', 'wilders', 'willr', 'wma', 'zlema']

_fx_column_names = {
    'DI': ['PLUS', 'MINUS'],
    'DM': ['PLUS', 'MINUS'],
    'MSW': ['SINE', 'LEAD'],
    'AROON': ['DOWN', 'UP'],
    'BBANDS': ['LOWER', 'MIDDLE', 'UPPER'],
    'FISHER': ['LINE', 'SIGNAL'],
    'MACD': ['LINE', 'SIGNAL', 'HISTOGRAM'],
    'STOCH': ['LINE', 'MA']
}


def _get_ohlcv_arrays(fn, ohlc):
    sign = list(insp.signature(fn).parameters.keys())
    params = ['close' if 'real' in p else p
              for p in sign if p in _OHLCV or 'real' in p]
    if isinstance(ohlc, pd.Series):
        assert len(params) == 1, \
            ('{} requires pd.DataFrame with columns {}, not pd.Series'
             .format(fn.__name__, params))
        return np.asarray([ohlc.values])
    else:
        return ohlc[params].T.values


def _tup(fn, ohlc, *args, **kwargs):
    """
    Calculate any function from "Tulipy" library from a OHLC Pandas DataFrame.

    :param function fn: the "Tulipy" function to call
    :param pd.DataFrame ohlc: a Pandas DataFrame type with open, high, low, close and or volume columns.
    :param args: function positional params.
    :param kwargs: function key pair params.
    :return pd.Series: a Pandas Series with data result.
    """
    fn_params = list(args) + list(kwargs.values())
    fn_name = fn.__name__.upper()
    data = fn(*_get_ohlcv_arrays(fn, ohlc), *fn_params)
    if data is not None:
        if type(data) == tuple:
            data_tmp = pd.DataFrame()
            i = 0
            for arr in data:
                num_rows = len(ohlc) - len(arr)
                result = list((np.nan,) * num_rows) + arr.tolist()
                suffix = _fx_column_names[fn_name][i] if fn_name in _fx_column_names.keys() else i
                data_tmp = pd.concat([
                    data_tmp,
                    pd.Series(result,
                              index=ohlc.index,
                              name=f'{fn_name.lower()}_{suffix.lower()}').bfill()
                ], axis=1)
                i += 1
            data = data_tmp.copy()
        else:
            num_rows = len(ohlc) - len(data)
            result = list((np.nan,) * num_rows) + data.tolist()
            data = pd.Series(result, index=ohlc.index, name=fn_name.lower()).bfill()
    return data


def ad(data):
    """
    Accumulation/Distribution Line.
    https://tulipindicators.org/ad

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'ad'), data)


def adosc(data, short_period=3, long_period=10):
    """
    Accumulation/Distribution Oscillator:
        The Accumulation/Distribution Oscillator is also known
        as the Chaikin Oscillator, after its inventor.
    https://tulipindicators.org/adosc

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param short_period: TODO
    :param long_period: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'adosc'), data, short_period, long_period)


def adx(data, period=14):
    """
    Average Directional Movement Index.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'adx'), data, period)


def adxr(data, period=14):
    """
    Average Directional Movement Rating.
    https://tulipindicators.org/adxr

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'adxr'), data, period)


def ao(data):
    """
    Awesome Oscillator.
    https://tulipindicators.org/ao

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'ao'), data)


def apo(data, short_period=20, long_period=26):
    """
    Absolute Price Oscillator.
    https://tulipindicators.org/apo

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param short_period: TODO
    :param long_period: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'apo'), data, short_period, long_period)


def aroon(data, period=14):
    """
    Aroon.
    https://tulipindicators.org/aroon

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'aroon'), data, period)


def aroonosc(data, period=14):
    """
    Aroon Oscillator.
    https://tulipindicators.org/aroonosc

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'aroonosc'), data, period)


def atr(data, period=14):
    """
    Average True Range:
        Average True Range is a measure of volatility. It represents roughly how much you can expect a security to change in price on any given day. It is often used in position sizing formulas.
        Average true range is calculated by applying Wilders Smoothing to True Range.

        True range for each day is the greatest of:
        Day's high minus day's low
        The absolute value of the day's high minus the previous day's close
        The absolute value of the day's low minus the previous day's close
    https://tulipindicators.org/atr

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'atr'), data, period)


def avgprice(data):
    """
    Average Price:
        The average price indicator calculates the mean of the open, high, low, and close of a bar.
    https://tulipindicators.org/avgprice

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'avgprice'), data)


def bbands(data, period=20, stddev=2):
    """
    Bollinger Bands:
        The Bollinger Bands indicator calculates three results.
        A middle band, which is a Simple Moving Average
        Also an upper and lower band, which are spaced off the middle band
        and calculated using standard deviations.
    https://tulipindicators.org/bbands

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :param stddev: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'bbands'), data, period, stddev)


def bop(data):
    """
    Balance Of Power:
        Balance of Power compares the strength of buyers and sellers.
    https://tulipindicators.org/bop

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'bop'), data)


def cci(data, period=20):
    """
    Commodity Channel Index.

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'cci'), data, period)


def cmo(data, period=14):
    """
    Chande Momentum Oscillator:
        The Commodity Channel Index indicator is used to detect trends.
        It works by taking a Simple Moving Average of the Typical Price
        and comparing it to the amount of volatility in Typical Price.
    https://tulipindicators.org/cci

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'cmo'), data, period)


def crossany(data):
    """
    Crossany:
        Crossany is a simple function that indicates when two input arrays cross each other.
        When given two inputs, A and B, cross returns 1 for the periods that A crosses above B.
    https://tulipindicators.org/crossany

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'crossany'), data)


def crossover(data):
    """
    Crossover:
        Crossover is a simple function that indicates when two input arrays crossover each other.
        When given two inputs, A and B, cross returns 1 for the periods that A crosses above B.
    https://tulipindicators.org/crossover

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'crossover'), data)


def cvi(data, period=14):
    """
    Chaikin's Volatility:
           Chaikins Volatility quantifies volatility by comparing the high and low prices.
           It uses the period but also passes it into the EMA it uses.
    https://tulipindicators.org/cvi

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'cvi'), data, period)


def decay(data, period):
    """
    Linear Decay:
        Decay is a simple function used to propagate signals from the past into the future.
        It is useful in conjunction with algorithm trading and machine learning functions.
    https://tulipindicators.org/decay

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'decay'), data, period)


def dema(data, period=50):
    """
    Double Exponential Moving Average.
    https://tulipindicators.org/dema

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'dema'), data, period)


def di(data, period=14):
    """
    Directional Indicator.
    https://tulipindicators.org/di

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'di'), data, period)


def dm(data, period=14):
    """
    Directional Movement.
    https://tulipindicators.org/dm

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'dm'), data, period)


def dpo(data, period=100):
    """
    Detrended Price Oscillator.
    https://tulipindicators.org/dpo

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'dpo'), data, period)


def dx(data, period=14):
    """
    Directional Movement Index.
    https://tulipindicators.org/dx

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'dx'), data, period)


def edecay(data, period):
    """
    Exponential Decay.
    https://tulipindicators.org/edecay

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'edecay'), data, period)


def ema(data, period=100):
    """
    Exponential Moving Average.
    https://tulipindicators.org/ema

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'ema'), data, period)


def emv(data):
    """
    Ease Of Movement.
    https://tulipindicators.org/emv

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'emv'), data)


def fisher(data, period=10):
    """
    Fisher Transform.
    https://tulipindicators.org/fisher

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'fisher'), data, period)


def fosc(data, period=14):
    """
    Forecast Oscillator.
    https://tulipindicators.org/fosc

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'fosc'), data, period)


def hma(data, period=200):
    """
    Hull Moving Average.
    https://tulipindicators.org/hma

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'hma'), data, period)


def kama(data, period=10):
    """
    Kaufman Adaptive Moving Average.
    https://tulipindicators.org/kama

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'kama'), data, period)


def kvo(data, short_period=34, long_period=55):
    """
    Klinger Volume Oscillator.
    https://tulipindicators.org/kvo

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param short_period: TODO
    :param long_period: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'kvo'), data, short_period, long_period)


def lag(data, period):
    """
    Lag.
    https://tulipindicators.org/lag

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'lag'), data, period)


def linreg(data, period=50):
    """
    Linear Regression.
    https://tulipindicators.org/linreg

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'linreg'), data, period)


def linregintercept(data, period=10):
    """
    Linear Regression Intercept.
    https://tulipindicators.org/linregintercept

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'linregintercept'), data, period)


def linregslope(data, period=50):
    """
    Linear Regression Slope.
    https://tulipindicators.org/linregslope

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'linregslope'), data, period)


def macd(data, short_period=12, long_period=26, signal_period=9):
    """
    Moving Average Convergence/Divergence.
    https://tulipindicators.org/macd

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param short_period: TODO
    :param long_period: TODO
    :param signal_period: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'macd'), data, short_period, long_period, signal_period)


def marketfi(data):
    """
    Market Facilitation Index.
    https://tulipindicators.org/marketfi

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'marketfi'), data)


def mass(data, period=25):
    """
    Mass Index.
    https://tulipindicators.org/mass

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'mass'), data, period)


def md(data, period=14):
    """
    Mean Deviation Over Period.
    https://tulipindicators.org/md

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'md'), data, period)


def mfi(data, period=14):
    """
    Money Flow Index.
    https://tulipindicators.org/mfi

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'mfi'), data, period)


def mom(data, period=9):
    """
    Momentum.
    https://tulipindicators.org/mom

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'mom'), data, period)


def msw(data, period=25):
    """
    Mesa Sine Wave.
    https://tulipindicators.org/msw

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'msw'), data, period)


def natr(data, period=14):
    """
    Normalized Average True Range.
    https://tulipindicators.org/natr

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'natr'), data, period)


def nvi(data):
    """
    Negative Volume Index:
        tries to show what smart investors are doing
        by staying flat on up-volume days
        and only changing on down-volume days.
    https://tulipindicators.org/nvi

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'nvi'), data)


def obv(data):
    """
    On Balance Volume.
    https://tulipindicators.org/obv

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'obv'), data)


def ppo(data, short_period=12, long_period=26):
    """
    Percentage Price Oscillator.
    https://tulipindicators.org/ppo

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param short_period: TODO
    :param long_period: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'ppo'), data, short_period, long_period)


def psar(data, acceleration_factor_step=0.02, acceleration_factor_maximum=0.21):
    """
    Parabolic Sar:
        lower factor_step = less sensitive SAR
        lower factor_maximum = less sensitivity
        https://school.stockcharts.com/doku.php?id=technical_indicators:parabolic_sar
    https://tulipindicators.org/psar

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param acceleration_factor_step: TODO
    :param acceleration_factor_maximum: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'psar'), data, acceleration_factor_step, acceleration_factor_maximum)


def pvi(data):
    """
    Positive Volume Index:
        Positive Volume Index is very similar to Negative Volume Index,
        but changes on volume-up days instead.
    https://tulipindicators.org/pvi

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'pvi'), data)


def qstick(data, period=200):
    """
    Qstick:
        Qstick can be used to quantify the ratio of recent up-bars to down-bars
    https://tulipindicators.org/qstick

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'qstick'), data, period)


def roc(data, period=9):
    """
    Rate Of Change:
           The Rate of Change indicator calculates the change
           between the current price and the price n bars ago.
    https://tulipindicators.org/roc

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'roc'), data, period)


def rocr(data, period=9):
    """
    Rate Of Change Ratio:
        The Rate of Change Ratio indicator calculates the change
        between the current price and the price n bars ago
    https://tulipindicators.org/rocr

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'rocr'), data, period)


def rsi(data, period=14):
    """
    Relative Strength Index.
    https://tulipindicators.org/rsi

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'rsi'), data, period)


def sma(data, period=200):
    """
    Simple Moving Average.
    https://tulipindicators.org/sma

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'sma'), data, period)


def stderr(data, period=50):
    """
    Standard Error Over Period.
        Standard Error, for a specified period, measures how far prices have deviated from a
        Linear Regression Line for the same period. ... If all the closing prices equaled the
        corresponding values of the Linear Regression Line, Standard Error would be zero.
    https://tulipindicators.org/stderr

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'stderr'), data, period)


def stoch(data, pct_k_period=14, pct_k_slowing_period=3, pct_d_period=3):
    """
    Stochastic Oscillator.
    https://tulipindicators.org/stoch

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param %k_period: TODO
    :param %k_slowing_period: TODO
    :param %d_period: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'stoch'), data, pct_k_period, pct_k_slowing_period, pct_d_period)


def tema(data, period=200):
    """
    Triple Exponential Moving Average.
    https://tulipindicators.org/tema

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'tema'), data, period)


def tr(data):
    """
    True Range.
    https://tulipindicators.org/tr

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'tr'), data)


def trima(data, period=100):
    """
    Triangular Moving Average:
        The Triangular Moving Average is similar to the Simple Moving Average but instead
        places more weight on middle portion of the smoothing period and less weight
        on the newest and oldest bars in the period.

        It takes one parameter, the period n.
        Larger values for n will have a greater smoothing effect on the input data.
    https://tulipindicators.org/trima

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'trima'), data, period)


def trix(data, period=14):
    """
    Trix.
    https://tulipindicators.org/trix

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'trix'), data, period)


def tsf(data, period=10):
    """
    Time Series Forecast.
    https://tulipindicators.org/tsf

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'tsf'), data, period)


def typprice(data):
    """
    Typical Price.
    https://tulipindicators.org/typprice

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'typprice'), data)


def ultosc(data, short_period=7, medium_period=14, long_period=28):
    """
    Ultimate Oscillator.
    https://tulipindicators.org/ultosc

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param short_period: TODO
    :param medium_period: TODO
    :param long_period: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'ultosc'), data, short_period, medium_period, long_period)


def vhf(data, period=50):
    """
    Vertical Horizontal Filter:
        Vertical Horizontal Filter (VHF) is a trending and ranging indicator authored by Adam White.
        The VHF uses the highest close minus the lowest close divided by the sum of the absolute value
        of the difference of the highest and lowest over a user defined time period.
    https://tulipindicators.org/vhf

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'vhf'), data, period)


def vidya(data, short_period=14, long_period=34, alpha=0.2):
    """
    Variable Index Dynamic Average:
        The Variable Index Dynamic Average indicator modifies the Exponential Moving Average
        by varying the smoothness based on recent volatility.
    https://tulipindicators.org/vidya

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param short_period: TODO
    :param long_period: TODO
    :param alpha: Smoothing factor
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'vidya'), data, short_period, long_period, alpha)


def volatility(data, period):
    """
    Annualized Historical Volatility:
        The Annualized Historical Volatility indicator calculates the volatility over a moving window.
    https://tulipindicators.org/volatility

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'volatility'), data, period)


def vosc(data, short_period=14, long_period=28):
    """
    Volume Oscillator.
    https://tulipindicators.org/vosc

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param short_period: TODO
    :param long_period: TODO
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'vosc'), data, short_period, long_period)


def vwma(data, period=100):
    """
    Volume Weighted Moving Average:
        The Volume Weighted Moving Average is similar to a Simple Moving Average,
        but it weights each bar by its volume.
    https://tulipindicators.org/vwma

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'vwma'), data, period)


def wad(data):
    """
    Williams Accumulation/Distribution.
    https://tulipindicators.org/wad

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'wad'), data)


def wcprice(data):
    """
    Weighted Close Price.
    https://tulipindicators.org/wcprice

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'wcprice'), data)


def wilders(data, period=50):
    """
    Wilders Smoothing:
           Larger values for period will have a greater smoothing effect on the input data
           but will also create more lag.
    https://tulipindicators.org/wilders

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'wilders'), data, period)


def willr(data, period=14):
    """
    Williams %R.
    https://tulipindicators.org/willr

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'willr'), data, period)


def wma(data, period=50):
    """
    Weighted Moving Average:
        The Weighted Moving Average is similar to the Simple Moving Average but instead
        places more weight on more recent bars in the smoothing period
        and less weight on the oldest bars in the period.

        It takes one parameter, the period.
        Larger values for period will have a greater smoothing effect on the input data.

        It is calculated for each bar as the weighted arithmetic mean of the previous n bars.
        For example, the weights for an n of 4 are: 4, 3, 2, 1.
        The weights w for a n of 7 are: 7, 6, 5, 4, 3, 2, 1.
        So in that example, the most recent bar influences the average 7 times as much as the oldest bar.
    https://tulipindicators.org/wma

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'wma'), data, period)


def zlema(data, period=200):
    """
    Zero-Lag Exponential Moving Average.
    https://tulipindicators.org/zlema

    :param pd.DataFrame data: a DataFrame instance with data columns (open, high, low, close, volume).
    :param int period: number of period used for indicators calcs.
    :return pd.Series: indicator results as pandas Series instance.
    """
    return _tup(getattr(tulipy, 'zlema'), data, period)
