import pandas as pd


df = pd.read_csv(
    "data/detection_results.csv"
)


def calculate_risk(row):

    score = 0

    # Unusual login time

    if (
        row["login_hour"] < 6
        or
        row["login_hour"] > 22
    ):
        score += 20


    # Failed login attempts

    if row["failed_logins"] >= 5:
        score += 25


    # Excessive file access

    if row["files_accessed"] >= 100:
        score += 25


    # Large download

    if row["download_mb"] >= 1000:
        score += 20


    # New IP address

    if row["new_ip"] == 1:
        score += 10


    return score


df["risk_score"] = df.apply(
    calculate_risk,
    axis=1
)


def severity(score):

    if score >= 70:
        return "Critical"

    elif score >= 50:
        return "High"

    elif score >= 25:
        return "Medium"

    return "Low"


df["severity"] = df[
    "risk_score"
].apply(severity)


df.to_csv(
    "data/alerts.csv",
    index=False
)


print(
    "Risk scoring completed."
)