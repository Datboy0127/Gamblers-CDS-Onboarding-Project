import pandas as pd
import os
from google.colab import files

def remove_nan(df):
    return df.dropna()

def replace_nan(df):
    output = df.copy()
    for col in output.columns:
        if output[col].dtype in ['float64', 'int64']:
            output[col].fillna(output[col].mean(), inplace=True)
        else:
            output[col].fillna(output[col].mode()[0], inplace=True)
    return output

def one_hot(column, labels):
    return pd.DataFrame({label: (column == label).astype(int) for label in labels})

def compile(path):
    df = pd.read_csv(path)
    df_cleaned = replace_nan(df)
    summary = {}

    summary["numerical"] = df_cleaned.describe().to_dict()

    categorical_summary = {}
    for col in df_cleaned.select_dtypes(include=['object']).columns:
        categorical_summary[col] = {
            "unique": df_cleaned[col].unique().tolist(),
            "counts": df_cleaned[col].value_counts().to_dict()
        }
    summary["categorical"] = categorical_summary

    return df_cleaned, summary

path = f"/content/spreadspoke_scores.csv"

df, summary_stats = compile(path)

cleaned_path = "/content/spreadspoke_scores_cleaned.csv"
df.to_csv(cleaned_path, index=False)

files.download(cleaned_path)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv(cleaned_path)
df = df.apply(pd.to_numeric, errors='ignore')

plot_dir = "plots"
os.makedirs(plot_dir, exist_ok=True)

numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
for col in numerical_columns:
    plt.figure()
    sns.histplot(df[col], bins=30, kde=True)
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.title(f"Histogram for {col}")
    plt.savefig(f"{plot_dir}/histogram_{col}.png")
    plt.close()

categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    plt.figure()
    df[col].value_counts().plot(kind='bar', color='skyblue')
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.title(f"Bar for {col}")
    plt.xticks(rotation=45)
    plt.savefig(f"{plot_dir}/barplot_{col}.png")
    plt.close()

violin_pairs = [("score_home", "team_home"), ("score_away", "team_away"), ("weather_temperature", "stadium")]
for num_col, cat_col in violin_pairs:
    plt.figure(figsize=(12, 6))
    sns.violinplot(x=df[cat_col], y=df[num_col])
    plt.xlabel(cat_col)
    plt.ylabel(num_col)
    plt.title(f"Violin for {num_col} by {cat_col}")
    plt.xticks(rotation=90)
    plt.savefig(f"{plot_dir}/violin_{num_col}_by_{cat_col}.png")
    plt.close()

scatter_pairs = [("score_home", "score_away"), ("weather_temperature", "weather_wind_mph"), ("spread_favorite", "over_under_line")]
for x_col, y_col in scatter_pairs:
    plt.figure()
    sns.scatterplot(x=df[x_col], y=df[y_col])
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"Scatter for {x_col} vs {y_col}")
    plt.savefig(f"{plot_dir}/scatter_{x_col}_vs_{y_col}.png")
    plt.close()

plt.figure(figsize=(10, 8))
corr = df.select_dtypes(include=['int64', 'float64']).corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.savefig(f"{plot_dir}/correlation_matrix.png")
plt.close()

plt.figure()
sns.boxplot(x=df["schedule_week"], y=df["score_home"])
plt.xlabel("Schedule Week")
plt.ylabel("Home Team Score")
plt.title("Box Plot of Home Score by Week")
plt.savefig(f"{plot_dir}/boxplot_schedule_week_score_home.png")
plt.close()

plt.figure()
sns.lineplot(x=df["schedule_season"], y=df["score_home"], ci=None)
plt.xlabel("Season")
plt.ylabel("Home Team Score")
plt.title("Home Scores Over Seasons")
plt.savefig(f"{plot_dir}/lineplot_season_score_home.png")
plt.close()
