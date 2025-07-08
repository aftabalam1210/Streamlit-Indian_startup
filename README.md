

# 🚀 Startup Funding Analysis - Streamlit App
[DEMO](https://app-indianstartup-omi2fj3gnhnsnxffb8wau9.streamlit.app/)

This Streamlit app provides a comprehensive interactive dashboard for analyzing startup funding data in India. It offers both an **overall** view of the funding ecosystem and **individual investor-level insights**, making it a powerful tool for enthusiasts, analysts, and investors alike.

## 📊 Features

### 🧮 Overall Analysis

* Total funding invested across startups.
* Highest single funding event.
* Average investment per startup.
* Count of unique funded startups.
* Month-on-Month (MoM) trend graph (total investment and count of deals).

### 💼 Investor-Level Analysis

* Most recent investments made by the selected investor.
* Top startups the investor has funded.
* Investment distribution by sector and city.
* Year-wise investment trend.

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/aftabalam1210/startup-funding-analysis.git
cd startup-funding-analysis
```

### 2. Install Dependencies

Make sure you have Python 3.7 or above. Then install the required packages:

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file doesn't exist, you can install manually:

```bash
pip install streamlit pandas matplotlib
```

### 3. Add Dataset

Place your dataset `startup_cleaned.csv` in the root directory of the project. Ensure it includes the following columns:

* `date` (format: `YYYY-MM-DD`)
* `startup`
* `amount` (numeric)
* `vertical` (industry/sector)
* `city`
* `round` (funding round)
* `investors` (comma-separated investor names)

### 4. Run the App

```bash
streamlit run app.py
```

This will open a browser window with the interactive dashboard.

## 📌 Notes

* Ensure the `amount` column is in crores (Cr) for accurate representation.
* The app parses investors by splitting the `investors` column by commas.
* Inconsistent or missing dates may be coerced to `NaT` and skipped in time-based aggregations.

## 📁 File Structure

```
.
├── app.py                 # Main Streamlit app script
├── startup_cleaned.csv    # Input dataset (user provided)
└── README.md              # This documentation
```
## 📂 Dataset Source

The dataset used in this project is publicly available on Kaggle:

**🔗 [Indian Startup Funding - by Sudalai Rajkumar](https://www.kaggle.com/datasets/sudalairajkumar/indian-startup-funding)**

It contains information about startup funding in India, including:

* Startup name
* Date of funding
* Amount invested
* Industry vertical
* Investor names
* City and funding round

The data was cleaned and pre-processed before building the dashboard.

---

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/ad38564a-2a90-4a69-a332-ac043c614611)


## 🙌 Contribution

Feel free to fork this project and submit pull requests. Suggestions and improvements are always welcome.

## 📃 License

MIT License

