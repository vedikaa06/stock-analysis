import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from datetime import datetime

# 1. Configuration
TICKERS = ["AAPL", "TSLA", "BTC-USD"]
HISTORY_DAYS = 10
REFRESH_INTERVAL = 30  # Seconds
MEAN_WINDOW = 10       # Calculate mean over last 10 data points

# Flag to control the live loop
is_running = True

def exit_program(event):
    global is_running
    print("\nExit command received. Closing dashboard...")
    is_running = False
    plt.close()

# 2. Setup the Visualization
plt.ion() # Interactive mode on
fig, axes = plt.subplots(3, 1, figsize=(10, 10))
plt.subplots_adjust(bottom=0.15, hspace=0.4) # Make room for the button

# Create the Exit Button at the bottom of the window
ax_exit = plt.axes([0.45, 0.02, 0.1, 0.05]) # [left, bottom, width, height]
btn_exit = Button(ax_exit, 'EXIT', color='lightcoral', hovercolor='red')
btn_exit.on_clicked(exit_program)

def update_plots():
    for i, ticker in enumerate(TICKERS):
        # Fetch 10 days of hourly data
        df = yf.download(ticker, period=f"{HISTORY_DAYS}d", interval="60m", progress=False)
        
        if not df.empty:
            prices = df['Close']
            
            # --- MEAN ANALYSIS ---
            # Calculating the rolling average to identify the trend
            rolling_mean = prices.rolling(window=MEAN_WINDOW).mean()

            # Plotting
            axes[i].clear()
            axes[i].plot(prices.index, prices, label="Live Price", color='dodgerblue', alpha=0.5)
            axes[i].plot(rolling_mean.index, rolling_mean, label="Mean Trend", color='crimson', linewidth=2)
            
            axes[i].set_title(f"Live Analysis: {ticker}")
            axes[i].set_ylabel("Price (USD)")
            axes[i].legend(loc='upper left')
            axes[i].grid(True, linestyle='--', alpha=0.6)

    plt.draw()



# 3. Main Live Loop
print(f"Dashboard started. Refreshing every {REFRESH_INTERVAL}s.")
try:
    while is_running:
        update_plots()
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] Successfully refreshed all 3 stocks.")
        
        # We use a short-loop pause so the Exit button stays responsive
        for _ in range(REFRESH_INTERVAL):
            if not is_running: break
            plt.pause(1) 
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Process Finished.")