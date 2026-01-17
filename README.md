# 📈 Live Stock Trend Analyzer

A real-time financial dashboard built with Python that monitors stock prices and cryptocurrency trends. This tool uses `yfinance` to fetch live market data and `matplotlib` to visualize price movements alongside a dynamic **Mean Trend** line for momentum analysis.

## 📌 Features

* 🔄 **Live Data Refresh**: Automatically updates stock prices every 30 seconds.
* 📊 **Technical Analysis**: Calculates a rolling average (Mean Trend) over the last 10 data points to identify price direction.
* 📉 **Multi-Asset Monitoring**: Tracks Apple (AAPL), Tesla (TSLA), and Bitcoin (BTC-USD) simultaneously.
* 🛑 **Interactive UI**: Features a built-in interactive "EXIT" button to safely terminate the live loop and close the visualization.
* 🛠️ **Real-time Logs**: Console-based timestamps to confirm successful data refreshes.

## 🖼️ Demo



* **Blue Line**: Live Price Action (Hourly intervals for the last 10 days).
* **Red Line**: Mean Trend (Rolling window average).

## ⚙️ Installation Instructions

### ✅ 1. Clone the Repository
```bash
git clone [https://github.com/your-username/stocks-analyzer.git](https://github.com/your-username/stocks-analyzer.git)
cd stocks-analyzer
```
### ✅ 2. Install Dependencies
Ensure you have Python installed, then run:

```Bash

pip install yfinance pandas matplotlib
```
### ✅ 3. Run the Dashboard
Execute the script to start the live visualization:

```Bash

python stocks.py
```
## 📦 Project Structure
stocks.py: The core application containing the interactive plotting logic and live data loop.

README.md: Project documentation and setup guide.

## 📋 Technical Stack
Python 🐍

yfinance: Market data extraction.

Pandas: Data manipulation and rolling mean calculations.

Matplotlib: Interactive real-time visualization.

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request for features like RSI indicators, Bollinger Bands, or email alerts.

## 👤 Author
Vedika Agarwal 📧 vedikaa006@gmail.com
🌐 LinkedIn : www.linkedin.com/in/vedika-agarwal-032909273
