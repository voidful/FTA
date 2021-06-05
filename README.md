# CryptoTA

Technical Analysis on Cryptocurrency

## install

`pip install cta`

## usage

```python
import cta
import vectorbt as vbt

binance_data = vbt.BinanceData.download(
    "BTCUSDT",
    start='1 day ago UTC',
    end='now UTC',
    interval='15m'
)
binance_data = binance_data.update()
price = binance_data.get()

ta = cta.TA_Features()
ta.get_all_indicators(price)
```

## Metric
ref: https://tulipindicators.org/list  
ref: https://github.com/twopirllc/pandas-ta  

### **Momentum** 
* _Awesome Oscillator_: **ao**
* _Absolute Price Oscillator_: **apo**
* _Balance of Power_: **bop**
* _Commodity Channel Index_: **cci**
* _Chande Momentum Oscillator_: **cmo**
    * A wrapper for ```ta.linreg(series, r=True)```
* _Momentum_: **mom**
* _Percentage Price Oscillator_: **ppo**
* _Rate of Change_: **roc**
* _Relative Strength Index_: **rsi**
    * Default is John Carter's. Enable Lazybear's with ```lazybear=True```
    * Excluded from ```df.ta.strategy()```.
* _Trix_: **trix**
* _Williams %R_: **willr**

<br/>

### **Overlap**
* _Double Exponential Moving Average_: **dema**
* _Exponential Moving Average_: **ema**
    * Commonly known as 'Typical Price' in Technical Analysis literature
* _Hull Exponential Moving Average_: **hma**
    * Use: help(ta.ichimoku). Returns two DataFrames.
    * Drop the Chikou Span Column, the final column of the first resultant DataFrame, remove potential data leak.
* _Kaufman's Adaptive Moving Average_: **kama**
* _Linear Regression_: **linreg**
* _Simple Moving Average_: **sma**
* _Triple Exponential Moving Average_: **tema**
* _Triangular Moving Average_: **trima**
* _Variable Index Dynamic Average_: **vidya**
* _Volume Weighted Moving Average_: **vwma**
* _Weighted Moving Average_: **wma**

<br/>

### **Trend**
* _Average Directional Movement Index_: **adx**
* _Detrended Price Oscillator_: **dpo**
    * Set ```centered=False``` to remove potential data leak.
* _Parabolic Stop and Reverse_: **psar**
* _Q Stick_: **qstick**
* _Vertical Horizontal Filter_: **vhf**

<br/>

### **Volatility**
* _Average True Range_: **atr**
* _Normalized Average True Range_: **natr**

<br/>

### **Volume**
* _Accumulation/Distribution Index_: **ad**
* _Accumulation/Distribution Oscillator_: **adosc**
* _Klinger Volume Oscillator_: **kvo**
* _Money Flow Index_: **mfi**
* _Negative Volume Index_: **nvi**
* _On-Balance Volume_: **obv**
* _Positive Volume Index_: **pvi**
* _Price-Volume_: **pvol**
* _Price Volume Trend_: **pvt**

<br/>

# **Indicator**
* _Average Directional Movement Rating_: **adxr**
* _Aroon_: **aroon**
* _Chaikins Volatility_: **cvi**
* _Directional Movement Index_: **dx**
* _Ease of Movement_: **emv**
* _Forecast Oscillator_: **fosc**
* _Linear Regression Intercept_: **linregintercept**
* _Linear Regression Slope_: **linregslope**
* _Market Facilitation Index_: **marketfi**
* _Mass Index_: **mass**
* _Rate of Change Ratio_: **rocr**
* _True Range_: **tr**
* _Ultimate Oscillator_: **ultosc**
* _Volume Oscillator_: **vosc**
* _Williams Accumulation/Distribution_: **wad**

<br/>

# **Overlay**
* _Average Price_: **avgprice**
* _Bollinger Bands_: **bbands**
* _Time Series Forecast_: **tsf**
* _Typical Price_: **typprice**
* _Weighted Close Price_: **wcprice**
* _Wilders Smoothing_: **wilders**
* _Zero-Lag Exponential Moving Average_: **zlema**

<br/>

# **Math**
* _Mean Deviation Over Period_: **md**
* _Standard Error Over Period_: **stderr**

<br/>