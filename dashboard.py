import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from main import route_ticket

# ---------- 1. Load data ----------
df = pd.read_csv("tickets.csv")

true = df["true_category"].tolist()
pred = []

print("\nRunning model on tickets.csv for dashboard...\n")

for msg in df["user_message"]:
    result = route_ticket(msg)
    pred.append(result.get("category", "Unknown"))

df["predicted_category"] = pred

# ---------- 2. Confusion matrix ----------
labels = sorted(df["true_category"].unique())

cm = confusion_matrix(df["true_category"], df["predicted_category"], labels=labels)

plt.figure(figsize=(6, 5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=labels,
    yticklabels=labels,
)
plt.title("Confusion Matrix - Ticket Categories")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.tight_layout()
plt.show()

# ---------- 3. Accuracy + cost estimate ----------
df["correct"] = df["true_category"] == df["predicted_category"]
accuracy = df["correct"].mean()

# simple cost model (example)
COST_PER_CALL_USD = 0.0015  # $0.0015 per ticket
total_requests = len(df)
total_cost = total_requests * COST_PER_CALL_USD

print("\n--- Dashboard Summary ---")
print(df[["user_message", "true_category", "predicted_category", "correct"]])
print(f"\nAccuracy: {accuracy * 100:.2f}%")
print(f"Total requests: {total_requests}")
print(f"Estimated API cost: ${total_cost:.4f} USD")
print("-------------------------")
