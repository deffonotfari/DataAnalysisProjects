
# Student Dropout Database

This Python script performs a basic data analysis on the dataset related to student dropout and academic success.

It shows the distribution of student outcomes pie chart. 



## Dataset
The script expects a CSV file named `students_dropout_academic_success.csv` in the same directory. The file should include at least the following columns:
- `target`: Indicates the academic outcome (e.g., dropout, success).
## Requirements
- Python 3.x
- pandas
- matplotlib

You can install the required libraries using pip:

```bash
pip install pandas matplotlib
```
## How It Works

    1. Loads the dataset into a Pandas DataFrame.

    2. Displays the first few rows and column names.

    3. Computes the frequency of values in the target and Marital Status columns.

    4. Displays a pie chart showing the distribution of student academic outcomes (target).


## Output
The output is a pie chart titled "Student Target Classes", showing the percentage of students in each outcome category.
## Acknowledgements

 - [Kaggle.com](https://www.kaggle.com/datasets/adilshamim8/predict-students-dropout-and-academic-success)
 - [Pandas API](https://pandas.pydata.org/docs/reference/index.html)



## Authors

- [@deffonotfari](https://www.github.com/deffonotfari)

