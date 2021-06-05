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
