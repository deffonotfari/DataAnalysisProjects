# Bestseller Books Analysis

This Python script performs basic data analysis on a dataset of best-selling books, including cleaning, transformation, and aggregation operations.

## Dataset

The script expects a CSV file named `bestsellers.csv` in the same directory. The dataset should include at least the following columns:
- `Name`: Title of the book  
- `Author`: Author of the book  
- `User Rating`: Rating given by users  
- `Reviews`: Number of reviews  
- `Price`: Price of the book  
- `Year`: Year of publication  
- `Genre`: Fiction or Non Fiction

## Requirements

- Python 3.x  
- pandas  

You can install the required libraries using:

```bash
pip install pandas
```

## How It Works

1. Loads the dataset into a Pandas DataFrame.
2. Displays the first five rows, shape, column names, and summary statistics.
3. Removes duplicate entries from the dataset.
4. Converts the `Price` column to float.
5. Renames columns for clarity:
   - `Name` → `Title`
   - `Year` → `Publication Year`
   - `User Rating` → `Rating`
6. Counts the number of appearances for each author and prints the result.
7. Calculates the average user rating grouped by genre.
8. Exports the top 10 most frequent authors to a CSV file named `top_authors.csv`.

## Output

- Console output showing:
  - First five rows of the dataset
  - Dataset shape and column names
  - Summary statistics
  - Author appearance counts
  - Average rating by genre
- A new CSV file: `top_authors.csv` listing the top 10 most frequent authors.

## Acknowledgements

- [Kaggle Datasets](https://www.kaggle.com/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## Author

- [@deffonotfari](https://www.github.com/deffonotfari)
