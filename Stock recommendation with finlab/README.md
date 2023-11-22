# Stock Prediction Project

This project includes the use of Neural Networks, Long Short-Term Memory (LSTM), and Convolutional Neural Networks (CNN) for basic stock prediction exercises. It utilizes technical indicators from the TA-Lib package for training.

## Final Project

The final project uses Deep Neural Networks (DNN), LightGBM, and Random Forest models to combine ensemble learning. It then selects the best 20 stock recommendations.

## Technical Indicators

The project uses the following technical indicators:

- Bias (乖離率): Measures the deviation rate of the closing price from a moving average.
- Acceleration (加速度): Measures the rate of change in the closing price.
- RSV: A component of the Stochastic Oscillator, it measures the closing price in relation to the range of prices over a certain period of time.
- Momentum (動能指標): Measures the rate of change in the closing price.

These indicators are calculated over various periods and used as features for the machine learning models.The below is feature importance of technicial indicators

![image](https://github.com/jerryold/Stock-Application/assets/12774427/e2b187df-82c3-4d6a-bbbd-af6683a624fc)


```python
def bias(n):
    return close / close.rolling(n, min_periods=1).mean()

def acc(n):
    return close.shift(n) / (close.shift(2*n) + close) * 2

def rsv(n):
    l = close.rolling(n, min_periods=1).min()
    h = close.rolling(n, min_periods=1).max()
    
    return (close - l) / (h - l)

def mom(n):
    return (rev / rev.shift(1)).shift(n)

features = {
    'mom1': mom(1),
    'mom2': mom(2),
    'mom3': mom(3),
    'mom4': mom(4),
    'mom5': mom(5),
    'mom6': mom(6),
    'mom7': mom(7),
    'mom8': mom(8),
    'mom9': mom(9),
    
    'bias5': bias(5),
    'bias10': bias(10),
    'bias20': bias(20),
    'bias60': bias(60),
    'bias120': bias(120),
    'bias240': bias(240),
    
    'acc5': acc(5),
    'acc10': acc(10),
    'acc20': acc(20),
    'acc60': acc(60),
    'acc120': acc(120),
    'acc240': acc(240),
    
    'rsv5': rsv(5),
    'rsv10': rsv(10),
    'rsv20': rsv(20),
    'rsv60': rsv(60),
    'rsv120': rsv(120),
    'rsv240': rsv(240),
}
```

## Compare with Stock 0050 result
![image](https://github.com/jerryold/Stock-Application/assets/12774427/ad8071ea-9e58-4b65-9e40-f7f330e707a3)




## Usage

To use this project, you will need to install the TA-Lib package and have a basic understanding of the models and technical indicators used.
https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib


