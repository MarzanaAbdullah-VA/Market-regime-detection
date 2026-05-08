import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def load_data():
    df = yf.download(
        "ORCL",
        start="2023-05-08",
        end="2026-05-08"
    )

    df.columns = df.columns.get_level_values(0)

    df.reset_index(inplace=True)

    return df


OracleData = load_data()



def create_features(df):
    # Daily returns
    df['Returns'] = df['Close'].pct_change()

    # Rolling volatility
    df['Volatility_20'] = (
        df['Returns']
        .rolling(20)
        .std()
    )

    # Momentum
    df['Momentum_20'] = (
        df['Close']
        .pct_change(20)
    )

    # Moving average ratio
    ma20 = df['Close'].rolling(20).mean()
    ma100 = df['Close'].rolling(100).mean()

    df['MA_Ratio'] = ma20 / ma100

    # Drawdown
    df['Rolling_Max'] = df['Close'].cummax()

    df['Drawdown'] = (
                             df['Close'] / df['Rolling_Max']
                     ) - 1

    df.dropna(inplace=True)

    return df


def detect_regimes(df):
    features = df[
        [
            'Returns',
            'Volatility_20',
            'Momentum_20',
            'Drawdown'
        ]
    ]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(features)

    model = KMeans(
        n_clusters=3,
        random_state=42
    )

    df['Regime'] = model.fit_predict(X_scaled)
    # print(f"these are regime values:\n{df['Regime']}")

    return df


def regime_statistics(df):
    Analysis1 = df.groupby('Regime')[
        ['Returns', 'Volatility_20']
    ].agg(
        ['mean', 'std', 'min', 'max']
    )
    print(Analysis1)

    Analysis2 = df.groupby('Regime')[
        [
            'Returns',
            'Volatility_20',
            'Momentum_20',
            'Drawdown'
        ]
    ].mean()
    print(Analysis2)


import matplotlib.pyplot as plt


def plot_regimes(df):
    regime_labels = {
        0: 'Stable Bull',
        1: 'Bear Crisis',
        2: 'Recovery Rally'
    }

    df['Regime_Name'] = (
        df['Regime']
        .map(regime_labels)
    )

    colors = {
        'Stable Bull': 'green',
        'Bear Crisis': 'red',
        'Recovery Rally': 'orange'
    }

    plt.figure(figsize=(15, 7))

    for regime_name, color in colors.items():
        subset = df[
            df['Regime_Name'] == regime_name
            ]

        plt.scatter(
            subset['Date'],
            subset['Close'],
            color=color,
            label=regime_name,
            s=12
        )

    plt.plot(
        df['Date'],
        df['Close'],
        color='gray',
        alpha=0.3
    )

    plt.title('Oracle Market Regimes')

    plt.xlabel('Date')
    plt.ylabel('Price')

    plt.legend()

    plt.grid(alpha=0.2)

    plt.show()


def main():
    df = load_data()

    df = create_features(df)

    df = detect_regimes(df)

    regime_statistics(df)
    plot_regimes(df)


if __name__ == "__main__":
    main()