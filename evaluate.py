import pandas as pd
from main import route_ticket

def evaluate_router(csv_path="tickets.csv"):
    df = pd.read_csv(csv_path)
    predictions = []

    for _, row in df.iterrows():
        msg = row["user_message"]
        true_cat = row["true_category"]

        result = route_ticket(msg)
        pred_cat = result.get("category", "Unknown")

        predictions.append({
            "user_message": msg,
            "true_category": true_cat,
            "predicted_category": pred_cat
        })

    results_df = pd.DataFrame(predictions)
    results_df["correct"] = results_df["true_category"] == results_df["predicted_category"]

    accuracy = results_df["correct"].mean()

    print("\n--- Evaluation Results ---")
    print(results_df.to_string(index=False))
    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    evaluate_router()
