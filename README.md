# Decoding Student Performance: Regression and Visualization Techniques

This project investigates the factors influencing student performance using a dataset from Kaggle with 20 columns and 6,607 records. It employs data preprocessing, stepwise regression, polynomial fitting, and various visualizations to explore the impact of factors like attendance, study habits, and parental involvement on exam scores.


## Dataset

The dataset is sourced from Kaggle and includes 20 columns and 6,607 records, capturing variables such as hours studied, attendance, parental involvement, and exam scores. [Link to dataset](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors)

## Methodology

The analysis consists of the following steps:

- **Data Preprocessing**: Cleaning data, removing duplicates, and encoding categorical variables into numeric formats.
- **Stepwise Regression**: Using backward elimination to select significant features, followed by Ridge and Lasso regression to predict exam scores.
- **Polynomial Fitting**: Applying polynomial regression (degree 3) with Ridge regression and cross-validation for enhanced predictions.
- **Visualization**: Generating plots such as heatmaps, regression lines, IQR plots, violin plots, and bubble plots to illustrate findings.

## Key Findings

- **Positive Correlations**: Exam scores show strong positive correlations with hours studied (0.45), attendance (0.58), and parental involvement (0.16).
- **Negative Correlations**: Negative correlations exist with access to resources (-0.17) and learning disabilities (-0.09).
- **Model Performance**: The final stepwise regression model achieves an R-squared value of 0.757, explaining 75.7% of the variance in exam scores, with all predictors statistically significant.

## Installation and Usage

To set up and run this project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LutherYTT/Decoding-Student-Performance-Regression-and-Visualization-Techniques.git
   cd Decoding-Student-Performance-Regression-and-Visualization-Techniques
   ```

2. **Install Dependencies**:
   Create a virtual environment and install required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Analysis**:
   Execute the Jupyter notebooks in the `notebooks/` directory in sequence:
   - `01_data_cleaning.ipynb`
   - `02_eda.ipynb`
   - `03_modeling.ipynb`

## Project Structure

- `data/`: Raw and processed datasets.
- `notebooks/`: Jupyter notebooks for data cleaning, exploratory data analysis (EDA), and modeling.
- `src/`: Python scripts with reusable functions.
- `reports/`: Final report and generated figures.

## Results and Visualizations

The project includes the following visualizations:

- **Heatmap**: Displays correlations between numerical features and exam scores.
  ![Correlation Heatmap](https://github.com/LutherYTT/Decoding-Student-Performance-Regression-and-Visualization-Techniques/blob/main/reports/figures/correlation_heatmap.png)
- **Regression Line**: Shows the relationship between key predictors and exam scores, with density-colored data points.
  ![Regression Line](https://github.com/LutherYTT/Decoding-Student-Performance-Regression-and-Visualization-Techniques/blob/main/reports/figures/regression_line.png)
- **IQR Plots**: Illustrate the distribution of exam scores relative to attendance rates.
  ![Attendance IQR Plot](https://github.com/LutherYTT/Decoding-Student-Performance-Regression-and-Visualization-Techniques/blob/main/reports/figures/boxplot_attendance.png)
  ![Hours_Studied IQR Plot](https://github.com/LutherYTT/Decoding-Student-Performance-Regression-and-Visualization-Techniques/blob/main/reports/figures/boxplot_hours_studied.png)
- **Violin Plots**: Reveal exam score distributions by gender, highlighting variability and trends.
  ![Violin Plot](https://github.com/LutherYTT/Decoding-Student-Performance-Regression-and-Visualization-Techniques/blob/main/reports/figures/violin_plot.png)
- **Bubble Plot**: Visualizes the relationship between hours studied, attendance (bubble size), and exam scores, with gender differences.
  ![Bubble Plot](https://github.com/LutherYTT/Decoding-Student-Performance-Regression-and-Visualization-Techniques/blob/main/reports/figures/bubble_plot.png)

## Conclusion and Future Work

This analysis highlights the significant roles of hours studied, attendance, and parental involvement in student performance, while noting limitations such as the dataset’s representativeness and potential unobserved confounders. Future enhancements could include expanding the dataset for diversity, adding variables like socio-economic status, and exploring advanced machine learning techniques.

## References

- Kaggle. (2023, January 10). Student performance factors dataset. Kaggle Datasets. https://www.kaggle.com/datasets/lainguyn123/student-performance-factors
