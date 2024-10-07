import pandas as pd
from envtest import calculate_average

data = pd.read_csv('scripts/data.csv')

scores = data['score'].tolist()

average_score = calculate_average(scores)

print(f"Average score is：{average_score}")
