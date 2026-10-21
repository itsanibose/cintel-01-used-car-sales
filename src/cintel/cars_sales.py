"""cars_sales.py - This file contains data logic for the project.

Author: Anindya Bose
Date: 2026-10

Purpose:
    This file is part of the cintel-01-used-car-sales project. This will read a CSV file containing used car sales data
    in the United States. We will use pandas to analyze the data and matplotlib to visualize the results.
    The main focus will be to understand how different module functions work together to read, process, and visualize data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# === DECLARE GLOBAL CONSTANTS FOR FOLDER PATHS (directories) ===
ROOT_DIR: Path = Path.cwd()
DATA_FILE: Path = ROOT_DIR / "data" / "used_car_sales.csv"


# == DEFINE FUNCTION TO PLOT SALES BY MAKER ===


def plot_sales_by_maker(top_n=5):
    """Plot count of sales by car maker.

    Args:
        top_n: Number of top-selling manufacturers to display.
    """
    # Read data into a DataFrame using pandas.
    df_sales = pd.read_csv(DATA_FILE)

    # Count sales for each manufacturer (largest first).
    maker_sales = df_sales.groupby("manufacturer").size().sort_values(ascending=False)

    # Select top N manufacturers
    top_makers = maker_sales.head(top_n)

    # Create vertical bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(top_makers.index, top_makers.values, color="teal")

    plt.title(f"Top {top_n} Car Makers by Total Sales")
    plt.xlabel("Car Maker")
    plt.ylabel("Total Number of Sales")
    plt.tight_layout()
    plt.show()
