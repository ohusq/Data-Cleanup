# Data Cleanup Tool

This tool cleans up supermarket sales data to make it easier to analyze and use.

## What it does

The script processes the raw sales data and:

1. **Removes incomplete records** - Deletes rows with missing information
2. **Removes duplicates** - Keeps only unique sales records
3. **Standardizes text formatting** - Makes all text consistent:
   - Removes extra spaces from text fields
   - Capitalizes city names properly (e.g., "Yangon")
   - Formats customer types ("Member", "Normal")
   - Formats gender ("Male", "Female")
   - Formats product lines ("Sports And Travel", "Fashion Accessories")
   - Formats payment methods ("Credit Card", "Cash", "Ewallet")
   - Makes branch codes uppercase ("A", "B", "C")
4. **Fixes date formats** - Converts dates to a standard format

## How to use

1. Place your raw sales data in `supermarket_sales_dirty.csv`
2. Run the cleanup script using `uv`:
   ```bash
   uv run python cleanup.py
   ```
3. The cleaned data will be saved as `supermarket_sales_cleaned.csv`

## Requirements

This script uses `uv` for Python package management. Make sure you have `uv` installed:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
or
```
# Fedora based
sudo dnf install uv
```

## Dataset used
[Supermarket sales by alexhuitron and `supermarket_sales_dirty` by Claude](https://www.kaggle.com/datasets/alexhuitron/supermarket-sales)

## Input and Output

**Input:** `supermarket_sales_dirty.csv` - Raw sales data with possible errors <br>
**Output:** `supermarket_sales_cleaned.csv` - Clean, standardized data ready for analysis