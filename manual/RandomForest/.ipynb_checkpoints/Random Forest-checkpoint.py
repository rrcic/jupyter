from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier


##Create 100 classes with 10000 samples and 10 features per sample
X, y = make_blobs(n_samples=10000, n_features=10, centers=100, random_state=0)

## Random forest
clf2 = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
scores2 = cross_val_score(clf2, X, y)
print(scores2.mean())