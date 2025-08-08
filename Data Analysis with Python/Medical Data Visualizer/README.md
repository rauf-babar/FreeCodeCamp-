🩺 Medical Data Visualizer

This project is a solution to the Medical Data Visualizer project from freeCodeCamp's Data Analysis with Python Certification.

It uses pandas, seaborn, and matplotlib to clean, analyze, and visualize patient data from a medical examination dataset.

---

📁 Project Files

- medical_data_visualizer.py: Main script for data preprocessing and visualization.
- catplot.png: Bar chart showing counts of good and bad health indicators, split by presence or absence of cardiovascular disease.
- heatmap.png: Correlation heatmap between various medical measurements after cleaning outliers.

---

✅ Tasks Completed

1. Add an Overweight Column
BMI is calculated using:
    - BMI = weight / (height in meters)^2
Patients with BMI > 25 are marked as overweight (1), otherwise not (0).

2. Normalize Data
Normalized cholesterol and gluc values so that:
    - 0 = good
    - 1 = bad

3. Categorical Plot (catplot.png)
    - Created using Seaborn’s catplot().
    - Visualizes the distribution of:
    - cholesterol, gluc, smoke, alco, active, and overweight
    - Split by cardio status (0 = no heart disease, 1 = has heart disease).
    - Shows how these health indicators vary among patients.

4. Clean Data
Removed invalid or extreme values by filtering:
    - Diastolic pressure > Systolic pressure
    - Height and weight outside 2.5th–97.5th percentile range

5. Correlation Heatmap (heatmap.png)
    - Displays Pearson correlation coefficients between health variables.
    - Masked the upper triangle for clarity.
    - Annotated with values (rounded to 1 decimal place).
    - Helps identify relationships (e.g. weight vs BMI, systolic vs diastolic).
