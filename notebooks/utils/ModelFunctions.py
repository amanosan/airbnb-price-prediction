from sklearn.model_selection import cross_val_score, KFold


def rmse_cv(model, X_train, y_train, n_splits=5):
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    score = cross_val_score(model, X_train, y_train,
                            scoring='neg_mean_squared_error', cv=kf)
    return score
