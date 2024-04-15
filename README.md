# FTA

Technical Analysis On Finance Data

## install

`pip install fta`

## example usage

```python
import fta
import vectorbt as vbt

yf_data = vbt.YFData.download(
    "TSLA",
    start='2022-02-25 09:30:00 -0400',
    end='2022-03-01 09:35:00 -0400',
    interval='1m'
)
price = yf_data.get()
ta = fta.TA_Features()
ta.get_all_indicators(price)
```
last 10 result:
|                           |    open |    high |     low |   close |   volume | close time                       |     quote volume |   number of trades |   taker base volume |   taker quote volume |   accbl_20 |   accbm_20 |   accbu_20 |   amate_lr_8_21_2 |   amate_sr_8_21_2 |     obv |   obv_min_2 |   obv_max_2 |   obve_4 |   obve_12 |   aobv_lr_2 |   aobv_sr_2 |    cg_10 |   copc_11_14_10 |   dec_1 |   dcl_20_20 |   dcm_20_20 |   dcu_20_20 |    efi_13 |   eom_14_100000000 |   fwma_10 |   isa_9 |   isb_26 |   its_9 |   iks_26 |   ics_26 |   inc_1 |   kcle_20_2 |   kcbe_20_2 |   kcue_20_2 |   kst_10_15_20_30_10_10_10_15 |   ksts_9 |    kurt_30 |   ldecay_5 |     logret_1 |   mad_30 |   median_30 |   midpoint_2 |   midprice_2 |     pctret_1 |             pvol |     pvt |   pwma_10 |   qtl_30_0.5 |   rma_10 |   rvi_14 |   sinwma_14 |   skew_30 |   slope_1 |   swma_10 |   t3_10_0.7 |   tsi_13_25_13 |   tsis_13_25_13 |   uo_7_14_28 |   var_30 |   vtxp_14 |   vtxm_14 |   low_close |   mean_close |   high_close |   pos_volume |   neg_volume |   total_volume |   vwap_d |    zs_30 |       ad |      adosc |     adx |    adxr |        ao |      apo |   aroon_down |   aroon_up |   aroonosc |     atr |   avgprice |   bbands_lower |   bbands_middle |   bbands_upper |        bop |       cci |      cmo |      cvi |    dema |   di_plus |   di_minus |   dm_plus |   dm_minus |      dpo |      dx |     ema |        emv |   fisher_line |   fisher_signal |       fosc |     hma |    kama |        kvo |   linreg |   linregintercept |   linregslope |   macd_line |   macd_signal |   macd_histogram |   marketfi |    mass |      md |     mfi |     mom |   msw_sine |   msw_lead |      natr |     nvi |   obv_2 |        ppo |    psar |     pvi |   qstick |          roc |     rocr |     rsi |     sma |   stderr |   stoch_line |   stoch_ma |    tema |     tr |   trima |        trix |     tsf |   typprice |   ultosc |      vhf |   vidya |     vosc |    vwma |     wad |   wcprice |   wilders |    willr |     wma |   zlema |
|:--------------------------|--------:|--------:|--------:|--------:|---------:|:---------------------------------|-----------------:|-------------------:|--------------------:|---------------------:|-----------:|-----------:|-----------:|------------------:|------------------:|--------:|------------:|------------:|---------:|----------:|------------:|------------:|---------:|----------------:|--------:|------------:|------------:|------------:|----------:|-------------------:|----------:|--------:|---------:|--------:|---------:|---------:|--------:|------------:|------------:|------------:|------------------------------:|---------:|-----------:|-----------:|-------------:|---------:|------------:|-------------:|-------------:|-------------:|-----------------:|--------:|----------:|-------------:|---------:|---------:|------------:|----------:|----------:|----------:|------------:|---------------:|----------------:|-------------:|---------:|----------:|----------:|------------:|-------------:|-------------:|-------------:|-------------:|---------------:|---------:|---------:|---------:|-----------:|--------:|--------:|----------:|---------:|-------------:|-----------:|-----------:|--------:|-----------:|---------------:|----------------:|---------------:|-----------:|----------:|---------:|---------:|--------:|----------:|-----------:|----------:|-----------:|---------:|--------:|--------:|-----------:|--------------:|----------------:|-----------:|--------:|--------:|-----------:|---------:|------------------:|--------------:|------------:|--------------:|-----------------:|-----------:|--------:|--------:|--------:|--------:|-----------:|-----------:|----------:|--------:|--------:|-----------:|--------:|--------:|---------:|-------------:|---------:|--------:|--------:|---------:|-------------:|-----------:|--------:|-------:|--------:|------------:|--------:|-----------:|---------:|---------:|--------:|---------:|--------:|--------:|----------:|----------:|---------:|--------:|--------:|
| 2022-03-02 06:57:00+00:00 | 43922.6 | 43955.3 | 43880.6 | 43940.5 | 55.8526  | 2022-03-02 06:57:59.999000+00:00 |      2.45229e+06 |               1441 |            26.6534  |          1.17015e+06 |    43921.2 |    44040.9 |    44157.8 |                 0 |                 1 | 654.032 |     598.179 |     654.032 |  647.434 |   659.637 |           0 |           1 | -5.50214 |       -0.342771 |       0 |     43880.6 |     43991.4 |     44102.3 |  -412.507 |       -2.55079e+09 |   43964   |     nan |      nan | 43977.3 |  43991.4 |      nan |       1 |     43930.5 |     44031.4 |     44132.2 |                      -198.256 | -183.229 |  2.28018   |    43940.5 |  0.000406314 |  31.2689 |     44058.7 |      43931.5 |      43926.1 |  0.000406397 |      2.45419e+06 | 257.656 |   44039.5 |      44058.7 |  44028.9 |  39.9081 |     44035.1 | -1.27163  |     17.85 |   44025.7 |     44027.7 |       -25.7024 |        -19.8497 |      47.7871 |  2082.08 |  0.77209  |   1.21082 |         nan |          nan |          nan |          nan |          nan |            nan |  44230.5 | -2.46775 | -694.91  |   8.2407   | 45.6375 | 38.2942 |  -72.372  | -13.9264 |     100      |    0       |  -100      | 48.3004 |    43924.8 |        43948.7 |         44040.9 |        44133.1 |  0.238726  | -232.24   | -36.4605 | 29.4623  | 44012.8 |   8.21072 |    42.4275 |   55.5213 |    286.897 |  47.1054 | 67.5711 | 44148.4 | -245721    |      -1.22179 |        -0.74804 | -0.0964647 | 44071.4 | 44034.5 | -102.792   |  43978.4 |           44062.8 |      -5.18697 |    -34.7959 |      -26.1356 |         -8.66039 |   1.33799  | 25.6649 | 38.0646 | 18.8715 |  -77.1  |  -0.894256 | -0.315864  | 0.109922  | 978.806 | 621.355 | -0.0832833 | 44046.9 | 1031.54 | -2.1725  | -0.00175157  | 0.998248 | 32.1332 | 44266.5 |  11.7552 |      19.3874 |    30.4223 | 44089.9 |  74.73 | 44187.2 | -0.0088084  | 43948.9 |    43925.5 |  47.7871 | 0.373064 | 44004.4 |  9.98053 | 44146.5 | -462.14 |   43929.2 |   44147.6 | -72.0223 | 44063.1 | 44112.4 |
| 2022-03-02 06:58:00+00:00 | 43940.5 | 43964   | 43940.4 | 43950.3 | 23.5556  | 2022-03-02 06:58:59.999000+00:00 |      1.03537e+06 |                845 |             7.73097 |     339787           |    43919.7 |    44036.7 |    44151.1 |                 0 |                 1 | 677.588 |     654.032 |     677.588 |  659.496 |   662.398 |           1 |           0 | -5.50269 |       -0.386562 |       0 |     43880.6 |     43991.4 |     44102.3 |  -320.532 |       -2.30011e+09 |   43958.6 |     nan |      nan | 43977.3 |  43991.4 |      nan |       1 |     43927.9 |     44023.6 |     44119.4 |                      -202.693 | -182.818 |  1.2397    |    43950.3 |  0.000223459 |  34.6982 |     44057.1 |      43945.4 |      43922.3 |  0.000223484 |      1.03528e+06 | 258.183 |   44022.6 |      44057.1 |  44021   |  52.7946 |     44025.9 | -1.0946   |      9.82 |   44013.2 |     44017   |       -26.6921 |        -20.8272 |      49.4287 |  2381.49 |  0.838736 |   1.18733 |         nan |          nan |          nan |          nan |          nan |            nan |  44230   | -2.01187 | -698.775 |   8.83517  | 46.8879 | 39.6449 |  -87.6127 | -14.6109 |      92.8571 |   14.2857  |   -78.5714 | 46.5303 |    43948.8 |        43936.4 |         44036.7 |        44137   |  0.417092  | -146.022  | -30.7245 | 19.8171  | 44005.1 |   9.23905 |    40.8956 |   60.1855 |    266.404 | 123.68   | 63.1431 | 44144.5 |  341832    |      -1.36075 |        -1.22179 | -0.0216988 | 44067   | 44029.8 |  -62.3741  |  43975.5 |           44069.4 |      -4.98999 |    -36.6471 |      -28.2379 |         -8.40924 |   0.998487 | 25.6395 | 43.3941 | 23.7767 |  -73.76 |  -0.83589  | -0.202935  | 0.10587   | 979.025 | 644.91  | -0.0876921 | 44030.3 | 1031.54 | -2.00495 | -0.00167545  | 0.998325 | 34.2879 | 44264.5 |  11.2053 |      23.7458 |    23.2329 | 44084.1 |  23.52 | 44184.6 | -0.00958802 | 43926   |    43951.6 |  49.4287 | 0.357127 | 43993   | 12.1859  | 44142.9 | -452.31 |   43951.2 |   44143.6 | -67.4318 | 44057   | 44107.1 |
| 2022-03-02 06:59:00+00:00 | 43950.3 | 43950.3 | 43926.2 | 43927.3 | 19.4608  | 2022-03-02 06:59:59.999000+00:00 | 855138           |                565 |             8.12693 |     357108           |    43917.7 |    44028.4 |    44140.5 |                 0 |                 1 | 658.127 |     658.127 |     677.588 |  658.948 |   661.741 |           1 |           0 | -5.50324 |       -0.436811 |       1 |     43880.6 |     43991.4 |     44102.3 |  -338.712 |       -1.91856e+09 |   43946.4 |     nan |      nan | 43977.3 |  43991.4 |      nan |       0 |     43923.3 |     44014.5 |     44105.7 |                      -217.516 | -184.606 |  0.696435  |    43950.1 | -0.000523683 |  37.7646 |     44055.5 |      43938.8 |      43945.1 | -0.000523546 | 854858           | 257.164 |   43996.3 |      44055.5 |  44011.6 |  41.9908 |     44015.2 | -1.09861  |    -23.01 |   43995.8 |     44005   |       -28.3483 |        -21.9017 |      46.1062 |  2666.45 |  0.87362  |   1.22762 |         nan |          nan |          nan |          nan |          nan |            nan |  44229.6 | -2.22225 | -716.461 |   2.64788  | 48.1674 | 40.8704 | -103.3    | -15.5682 |      85.7143 |    7.14286 |   -78.5714 | 44.9296 |    43938.5 |        43921   |         44028.4 |        44135.8 | -0.954395  | -141.982  | -48.1493 | -2.61656 | 43996.2 |   8.88477 |    41.5977 |   55.8865 |    261.655 | 175.735  | 64.8005 | 44140.2 | -173271    |      -1.47763 |        -1.36075 | -0.033554  | 44062.3 | 44020.8 |  -52.3341  |  43970.5 |           44073   |      -4.88678 |    -39.4161 |      -30.4735 |         -8.94256 |   1.23942  | 25.557  | 48.3284 | 24.2785 | -128.3  |  -0.760177 | -0.0781073 | 0.102282  | 978.512 | 625.449 | -0.0943223 | 44015.3 | 1031.54 | -2.5215  | -0.00291223  | 0.997088 | 31.7446 | 44261.9 |  10.9126 |      27.4526 |    23.5286 | 44077.7 |  24.12 | 44181.9 | -0.0104296  | 43900.1 |    43934.6 |  46.1062 | 0.314604 | 43979.5 |  9.17662 | 44139.9 | -475.33 |   43932.7 |   44139.3 | -78.1881 | 44050.3 | 44101.4 |
| 2022-03-02 07:00:00+00:00 | 43927.3 | 43965.7 | 43912.4 | 43955.2 | 24.4672  | 2022-03-02 07:00:59.999000+00:00 |      1.07526e+06 |                982 |            13.5451  |     595251           |    43906.8 |    44021.7 |    44137.1 |                 0 |                 1 | 682.594 |     658.127 |     682.594 |  668.406 |   664.949 |           1 |           0 | -5.5029  |       -0.45395  |       0 |     43880.6 |     43991.4 |     44102.3 |  -192.841 |       -2.39934e+09 |   43949.5 |     nan |      nan | 43970.9 |  43991.4 |      nan |       1 |     43916.2 |     44008.8 |     44101.5 |                      -232.917 | -188.755 |  0.124341  |    43955.2 |  0.000634712 |  39.1587 |     44054.5 |      43941.2 |      43939   |  0.000634913 |      1.07546e+06 | 258.717 |   43969.1 |      44054.5 |  44006   |  52.812  |     44004.6 | -1.1249   |     27.89 |   43977.5 |     43992.9 |       -27.7522 |        -22.7375 |      48.6291 |  2624.58 |  0.751293 |   1.19838 |         nan |          nan |          nan |          nan |          nan |            nan |  44229.1 | -1.58174 | -701.649 |   4.58909  | 48.7719 | 41.8146 | -107.24   | -15.6701 |      78.5714 |    0       |   -78.5714 | 45.5253 |    43940.1 |        43913.5 |         44021.7 |        44130   |  0.523559  | -107.98   | -34.666  |  7.51048 | 43989.9 |  10.5553  |    38.1209 |   67.2746 |    242.966 | 148.077  | 56.6306 | 44136.5 |   17526.5  |      -1.56272 |        -1.47763 |  0.0653241 | 44057.4 | 44014.6 |  -22.8256  |  43966.7 |           44054.6 |      -4.7993  |    -39.058  |      -32.1904 |         -6.86757 |   2.1772   | 25.5667 | 48.7906 | 26.5933 |  -98.53 |  -0.657327 |  0.0680788 | 0.103572  | 978.512 | 649.917 | -0.0933878 | 44001.9 | 1032.2  | -2.18045 | -0.00223659  | 0.997763 | 37.7698 | 44259.7 |  10.71   |      30.5698 |    27.2561 | 44072.3 |  53.27 | 44179.1 | -0.011096   | 43900.2 |    43944.4 |  48.6291 | 0.283051 | 43974.8 | 17.0979  | 44136.6 | -432.57 |   43947.1 |   44135.6 | -62.6709 | 44045   | 44096.5 |
| 2022-03-02 07:01:00+00:00 | 43955.2 | 43961.8 | 43946.8 | 43948.8 |  9.45334 | 2022-03-02 07:01:59.999000+00:00 | 415534           |                560 |             4.36364 |     191809           |    43903.9 |    44015.1 |    44128.2 |                 0 |                 1 | 673.141 |     673.141 |     682.594 |  670.3   |   666.209 |           1 |           0 | -5.50241 |       -0.478801 |       1 |     43880.6 |     43991.4 |     44102.3 |  -173.908 |       -2.13829e+09 |   43948.9 |     nan |      nan | 43970.9 |  43991.4 |      nan |       0 |     43916.4 |     44003.1 |     44089.8 |                      -247.574 | -195.689 | -0.38888   |    43955   | -0.000145158 |  41.8082 |     44053   |      43952   |      43939   | -0.000145148 | 415463           | 258.58  |   43950.4 |      44053   |  44000.3 |  43.677  |     43994.3 | -0.9882   |     -6.38 |   43963.1 |     43981.6 |       -27.5289 |        -23.4219 |      48.5768 |  2729.45 |  0.822257 |   1.18353 |         nan |          nan |          nan |          nan |          nan |            nan |  44228.9 | -1.57779 | -708.583 |   2.75972  | 49.3332 | 42.9861 |  -98.9418 | -15.7799 |      71.4286 |    0       |   -71.4286 | 43.3457 |    43953.1 |        43906   |         44015.1 |        44124.1 | -0.425716  |  -84.6171 | -33.7849 |  5.81206 | 43983.6 |  10.2942  |    37.178  |   62.4693 |    225.611 | 103.654  | 56.6306 | 44132.8 |  242139    |      -1.47718 |        -1.56272 |  0.0601552 | 44052.5 | 44008.1 |   -2.02287 |  43961.4 |           44032.5 |      -4.79371 |    -38.8155 |      -33.5154 |         -5.30009 |   1.5878   | 25.4371 | 48.0657 | 29.4644 |  -91.4  |  -0.562495 |  0.186893  | 0.0986277 | 978.37  | 640.463 | -0.09275   | 43989.7 | 1032.2  | -2.5594  | -0.00207538  | 0.997925 | 36.9659 | 44257.2 |  10.6983 |      31.4661 |    29.8295 | 44066.8 |  15.01 | 44176.2 | -0.0116242  | 43903.9 |    43952.4 |  48.5768 | 0.284265 | 43970   | 15.1892  | 44135   | -445.58 |   43951.5 |   44131.9 | -64.7427 | 44039.7 | 44091.2 |
| 2022-03-02 07:02:00+00:00 | 43948.8 | 43948.8 | 43844.6 | 43848.3 | 63.5924  | 2022-03-02 07:02:59.999000+00:00 |      2.79014e+06 |               1337 |            13.7422  |     602949           |    43884.8 |    44004   |    44129.8 |                 0 |                 1 | 609.548 |     609.548 |     673.141 |  645.999 |   657.492 |           0 |           1 | -5.50289 |       -0.5595   |       1 |     43844.6 |     43973.5 |     44102.3 | -1061.98  |       -1.89415e+09 |   43910   |     nan |      nan | 43951.6 |  43973.5 |      nan |       0 |     43890.1 |     43988.4 |     44086.6 |                      -279.549 | -208.423 |  0.781923  |    43948.6 | -0.00228914  |  48.9353 |     44048.2 |      43898.5 |      43903.2 | -0.00228653  |      2.78842e+06 | 244.039 |   43942.6 |      44048.2 |  43985.1 |  35.0663 |     43982.3 | -1.21212  |   -100.49 |   43949.9 |     43968.9 |       -30.9967 |        -24.504  |      42.4063 |  3747.96 |  0.752777 |   1.1705  |         nan |          nan |          nan |          nan |          nan |            nan |  44227.4 | -2.86294 | -767.706 | -17.0515   | 50.7105 | 44.7394 |  -97.2557 | -17.8874 |     100      |   21.4286  |   -78.5714 | 47.6896 |    43897.6 |        43876.1 |         44004   |        44131.8 | -0.964766  | -152.487  | -43.0548 | 22.0116  | 43970   |   8.68822 |    46.6778 |   58.0072 |    311.646 |  69.3892 | 68.6153 | 44127.2 | -943039    |      -1.67408 |        -1.47718 | -0.159911  | 44047.1 | 43981.9 |  -98.723   |  43947.7 |           44024.7 |      -5.0799  |    -45.725  |      -35.9573 |         -9.76763 |   1.63793  | 25.5731 | 54.8722 | 26.2593 | -210.26 |  -0.54735  |  0.204745  | 0.10876   | 978.37  | 576.871 | -0.109426  | 43978.8 | 1029.84 | -3.0886  | -0.00477229  | 0.995228 | 27.1604 | 44254.1 |  11.421  |      24.7275 |    28.9211 | 44058.4 | 104.16 | 44173.2 | -0.0125498  | 43870.9 |    43880.6 |  42.4063 | 0.33565  | 43946.1 | 21.8165  | 44123.8 | -546.08 |   43872.5 |   44126.2 | -98.404  | 44030.7 | 44084.2 |
| 2022-03-02 07:03:00+00:00 | 43848.3 | 43911.6 | 43844.8 | 43890   | 50.8787  | 2022-03-02 07:03:59.999000+00:00 |      2.23206e+06 |               1266 |            13.2695  |     582201           |    43874.7 |    43995.4 |    44120.7 |                 0 |                 1 | 660.427 |     609.548 |     660.427 |  651.77  |   657.944 |           0 |           1 | -5.50227 |       -0.58892  |       0 |     43844.6 |     43969.6 |     44094.5 |  -607.321 |       -1.88425e+09 |   43901.9 |     nan |      nan | 43940.1 |  43973.5 |      nan |       1 |     43877.3 |     43979   |     44080.6 |                      -300.631 | -224.796 |  0.0891079 |    43890   |  0.000950099 |  53.9524 |     44042.1 |      43869.1 |      43896.7 |  0.00095055  |      2.23307e+06 | 248.876 |   43940.3 |      44042.1 |  43975.6 |  47.5464 |     43969.1 | -1.03455  |     41.68 |   43938.1 |     43955.6 |       -30.9027 |        -25.4181 |      45.9952 |  4269.03 |  0.82294  |   1.16598 |         nan |          nan |          nan |          nan |          nan |            nan |  44226.2 | -1.95534 | -749.716 | -17.8818   | 51.9894 | 45.5136 | -105.237  | -18.6446 |      92.8571 |   14.2857  |   -78.5714 | 49.0546 |    43873.6 |        43861.3 |         43995.4 |        44129.6 |  0.623802  | -129.782  | -31.2992 | 20.4564  | 43960.5 |   7.84313 |    42.1375 |   53.8638 |    289.386 |  40.4559 | 68.6153 | 44122.5 | -243548    |      -1.99755 |        -1.67408 |  0.0192141 | 44041.5 | 43971   |  -60.6723  |  43939   |           43992.9 |      -5.17445 |    -47.5171 |      -38.2693 |         -9.24782 |   1.31293  | 25.7056 | 55.5027 | 40.9281 | -145.53 |  -0.462658 |  0.299727  | 0.111767  | 979.3   | 627.75  | -0.113691  | 43962.7 | 1029.84 | -2.66405 | -0.00330483  | 0.996695 | 34.8765 | 44251.4 |  11.6387 |      18.8746 |    25.0227 | 44051.5 |  66.8  | 44170.1 | -0.0134356  | 43872.2 |    43882.1 |  45.9952 | 0.328056 | 43935   |  6.22888 | 44117.8 | -500.87 |   43884.1 |   44121.5 | -80.2294 | 44023.5 | 44078.3 |
| 2022-03-02 07:04:00+00:00 | 43890   | 43905   | 43852   | 43890.6 | 25.6185  | 2022-03-02 07:04:59.999000+00:00 |      1.12432e+06 |                977 |            13.533   |     593920           |    43863.6 |    43987.3 |    44112.5 |                 0 |                 1 | 686.045 |     660.427 |     686.045 |  665.48  |   662.267 |           1 |           0 | -5.50155 |       -0.62855  |       0 |     43844.6 |     43969.6 |     44094.5 |  -518.255 |       -2.41156e+09 |   43897.1 |     nan |      nan | 43908.1 |  43973.5 |      nan |       1 |     43868.5 |     43970.6 |     44072.6 |                      -316.148 | -241.919 | -0.451016  |    43890.6 |  1.4354e-05  |  59.2031 |     44042.1 |      43890.3 |      43878.2 |  1.43541e-05 |      1.12441e+06 | 248.912 |   43936.1 |      44042.1 |  43967.1 |  56.8895 |     43955.4 | -0.87522  |      0.63 |   43928.6 |     43942.3 |       -30.7942 |        -26.1861 |      43.9713 |  4791.76 |  0.768642 |   1.24083 |         nan |          nan |          nan |          nan |          nan |            nan |  44225.6 | -1.76688 | -738.001 | -12.8683   | 53.177  | 46.2287 | -109.75   | -19.1341 |      85.7143 |    7.14286 |   -78.5714 | 49.3385 |    43884.4 |        43848.5 |         43987.3 |        44126.2 |  0.0116915 | -114.483  | -41.5071 | 15.0097  | 43951.6 |   7.24099 |    38.9025 |   50.0164 |    268.715 |  69.5339 | 68.6153 | 44117.9 |    6520.47 |      -2.36691 |        -1.99755 |  0.0622139 | 44035.7 | 43962.8 |  -20.8759  |  43929.8 |           43961.2 |      -5.31925 |    -48.3444 |      -40.2843 |         -8.06007 |   2.06999  | 25.7332 | 51.3538 | 39.5191 |  -77.01 |  -0.421792 |  0.342876  | 0.112413  | 979.314 | 653.368 | -0.115626  | 43948.8 | 1029.84 | -2.7077  | -0.00175152  | 0.998248 | 34.9886 | 44248.7 |  11.9298 |      13.804  |    19.1354 | 44044.7 |  53.03 | 44167   | -0.0142173  | 43878.8 |    43882.5 |  43.9713 | 0.338293 | 43926.6 |  4.57621 | 44114.2 | -462.23 |   43884.5 |   44116.9 | -79.9547 | 44016.7 | 44072.5 |
| 2022-03-02 07:05:00+00:00 | 43890.6 | 43918.4 | 43867.2 | 43918.4 | 29.79    | 2022-03-02 07:05:59.999000+00:00 |      1.30763e+06 |                861 |            20.7488  |     910735           |    43860.3 |    43979.1 |    44100.4 |                 0 |                 1 | 715.835 |     686.045 |     715.835 |  685.622 |   670.508 |           1 |           0 | -5.50106 |       -0.624497 |       0 |     43844.6 |     43969.6 |     44094.5 |  -326.08  |       -2.39413e+09 |   43905   |     nan |      nan | 43905.1 |  43973.5 |      nan |       1 |     43863.5 |     43965.6 |     44067.7 |                      -321.667 | -257.439 | -0.823441  |    43918.4 |  0.000632282 |  62.4329 |     44037.8 |      43904.5 |      43885.2 |  0.000632482 |      1.30833e+06 | 250.797 |   43925   |      44037.8 |  43962.2 |  63.7465 |     43943   | -0.709714 |     27.76 |   43921.5 |     43930.2 |       -29.043  |        -26.5943 |      50.0906 |  5048.31 |  0.749381 |   1.2139  |         nan |          nan |          nan |          nan |          nan |            nan |  44224.9 | -1.27171 | -708.222 |  -0.172569 | 53.7588 | 46.7838 | -112.37   | -18.8216 |      78.5714 |    0       |   -78.5714 | 49.4687 |    43898.6 |        43844.5 |         43979.1 |        44113.7 |  0.542807  |  -85.5094 | -31.968  | 22.1137  | 43945.4 |   8.63806 |    36.0288 |   59.8238 |    249.521 |  39.5779 | 61.3223 | 44113.9 |  245839    |      -2.25915 |        -2.36691 |  0.143825  | 44029.8 | 43961.6 |   26.5431  |  43924.4 |           43944.6 |      -5.31064 |    -46.3689 |      -41.5012 |         -4.8677  |   1.71735  | 25.8226 | 44.2878 | 40.9183 |   -4.25 |  -0.342573 |  0.422085  | 0.112638  | 979.314 | 683.158 | -0.110788  | 43936.3 | 1030.49 | -2.38715 | -9.67611e-05 | 0.999903 | 39.898  | 44246.3 |  11.9129 |      24.6228 |    19.1005 | 44038.9 |  51.16 | 44163.8 | -0.0147103  | 43888.1 |    43901.3 |  50.0906 | 0.337355 | 43925.2 |  6.03304 | 44110.7 | -411.08 |   43905.6 |   44112.9 | -65.9477 | 44011.1 | 44067.9 |
| 2022-03-02 07:06:00+00:00 | 43918.4 | 43932.7 | 43873.1 | 43879   | 18.3777  | 2022-03-02 07:06:59.999000+00:00 | 806809           |                873 |             6.41394 |     281566           |    43846.4 |    43969.3 |    44096.2 |                 0 |                 1 | 697.458 |     697.458 |     715.835 |  690.356 |   674.654 |           1 |           0 | -5.50143 |       -0.617154 |       1 |     43844.6 |     43962.5 |     44080.3 |  -382.728 |       -1.86442e+09 |   43895   |     nan |      nan | 43905.1 |  43973.5 |      nan |       0 |     43853.7 |     43957.4 |     44061   |                      -327.124 | -271.758 | -1.09603   |    43918.2 | -0.000895699 |  66.2828 |     44035.3 |      43898.7 |      43899.9 | -0.000895298 | 806397           | 249.151 |   43909.2 |      44035.3 |  43953.9 |  54.3274 |     43931.7 | -0.571795 |    -39.32 |   43912.5 |     43919   |       -28.9674 |        -26.9333 |      47.2031 |  5504.31 |  0.79521  |   1.16616 |         nan |          nan |          nan |          nan |          nan |            nan |  44224.5 | -1.66708 | -722.956 |   0.348843 | 53.7533 | 46.973  | -118.047  | -19.2593 |      71.4286 |    7.14286 |   -64.2857 | 50.1859 |    43900.8 |        43835.4 |         43969.3 |        44103.3 | -0.660897  |  -84.7912 | -35.8775 | 29.3509  | 43936.7 |   9.93886 |    32.9771 |   69.8307 |    231.698 |  67.8331 | 53.6823 | 44109.3 |  327216    |      -1.89784 |        -2.25915 |  0.043085  | 44023.8 | 43959.6 |   26.5331  |  43916.6 |           43949.1 |      -5.36798 |    -47.2431 |      -42.6496 |         -4.59349 |   3.23816  | 25.9144 | 41.4429 | 40.4695 |  -61.42 |  -0.28713  |  0.4743    | 0.114373  | 978.437 | 664.78  | -0.112875  | 43844.6 | 1030.49 | -2.47375 | -0.0013978   | 0.998602 | 35.7768 | 44243.8 |  12.0407 |      23.33   |    20.5856 | 44032.1 |  59.51 | 44160.5 | -0.0151683  | 43873   |    43894.9 |  47.2031 | 0.325346 | 43918   |  8.89711 | 44107.8 | -464.69 |   43891   |   44108.2 | -84.1077 | 44004.2 | 44063.5 |

## Supported DataSource

### Yfinance
```
yf_data = vbt.YFData.download(
    "TSLA",
    start='2022-02-25 09:30:00 -0400',
    end='2022-03-01 09:35:00 -0400',
    interval='1m'
)
price = yf_data.get()
```

### Binance

```python
import fta
import vectorbt as vbt

binance_data = vbt.BinanceData.download(
  "BTCUSDT",
  start='1 day ago UTC',
  end='now UTC',
  interval='1m'
)
binance_data = binance_data.update()
price = binance_data.get()
```

### Alpaca

```python
import fta
import vectorbt as vbt

alpaca_data = vbt.AlpacaData.download(
  "AAPL",
  start='2 hours ago UTC',
  end='15 minutes ago UTC',
  interval='1m',
)
alpaca_data = alpaca_data.update()
price = alpaca_data.get()
alpaca_data.get()
```

### CCXT
```python
ccxt_data = vbt.CCXTData.download(
     "BTC/USDT",
     start='2 hours ago UTC',
     end='now UTC',
     timeframe='1m'
)
ccxt_data = ccxt_data.update()
price = ccxt_data.get()
```



## Supported Metric

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

### **Indicator**
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

### **Overlay**
* _Average Price_: **avgprice**
* _Bollinger Bands_: **bbands**
* _Time Series Forecast_: **tsf**
* _Typical Price_: **typprice**
* _Weighted Close Price_: **wcprice**
* _Wilders Smoothing_: **wilders**
* _Zero-Lag Exponential Moving Average_: **zlema**

<br/>

### **Math**
* _Mean Deviation Over Period_: **md**
* _Standard Error Over Period_: **stderr**

<br/>

Ref: https://tulipindicators.org/list  
Ref: https://github.com/twopirllc/pandas-ta~~  
