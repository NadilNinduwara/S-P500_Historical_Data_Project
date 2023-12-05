# S&P500 Historical Data Project

This repository contains a Python script for downloading historical stock data of companies listed in the S&P 500 index. The data is sourced from Yahoo Finance using the `yfinance` library.

## Usage

1. **Clone the repository, navigate to the project directory, and run the script:**

    ```bash
    git clone https://github.com/NadilNinduwara/S&P500_Historical_Data_Project.git
    cd S&P500_Historical_Data_Project
    python snp.py
    ```

    The script will create a 'data' directory (if not present) and download historical stock data for S&P 500 companies, saving individual CSV files for each company in the 'data' directory.

## Dependencies

- Python 3.x
- pandas
- yfinance

## How to Install Dependencies

If you haven't already, you can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
