"""
Mini Pipeline Validator:
Reads logged CSV and performs simple data quality checks.
Simulates post-processing validation in an MLOps pipeline.
"""
import pandas as pd
from loguru import logger

def validate_results(path="data/results.csv"):
    df = pd.read_csv(path, names=["timestamp","operation","x","y","result"])
    logger.info(f"Loaded {len(df)} records from {path}")

    if df["result"].isna().any():
        logger.error("❌ Found missing result values.")
    else:
        logger.info("✅ No missing result values.")

    mean_val = df["result"].mean()
    logger.info(f"📊 Mean of results = {mean_val:.2f}")

    op_counts = df["operation"].value_counts().to_dict()
    logger.info(f"🧮 Operation distribution: {op_counts}")

    return {"count": len(df), "mean": mean_val, "ops": op_counts}

if __name__ == "__main__":
    summary = validate_results()
    print(summary)
