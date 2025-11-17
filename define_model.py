from sklearn.ensemble import IsolationForest

model = IsolationForest(n_estimators=100, max_samples='auto', contamination='auto', random_state=42)
