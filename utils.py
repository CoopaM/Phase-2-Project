import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


def evaluate_model(X_train, X_test, y_train, y_test, log = False):
    '''
    Expected Good Doc String
    '''
    # Create and fit model
    model = sm.OLS(y_train, sm.add_constant(X_train)).fit()
    
    # Print summary (if OLS)
    print(model.summary())
    
    # Grab predictions
    train_preds = model.predict(sm.add_constant(X_train))
    test_preds = model.predict(sm.add_constant(X_test))
    
    # Evaluate on train and test
    print(f"Train R2 Score: {r2_score(y_train, train_preds):.4f}")
    if log == True:
        y_train_unlog = np.exmp1(y_train)
        train_preds_unlog = np.expm1(train_preds)
        print(f"Train MAE Score: ${mean_absolute_error(y_train_unlog, train_preds_unlog):.4f}")
        print(f"Train RMSE Score: ${mean_squared_error(y_train_unlog, train_preds_unlog, squared=False):.4f}")
    else:
        print(f"Train MAE Score: ${mean_absolute_error(y_train, train_preds):.4f}")
        print(f"Train RMSE Score: ${mean_squared_error(y_train, train_preds, squared=False):.4f}")
    print("*"*20)
    print(f"Test R2 Score: {r2_score(y_test, test_preds):.4f}")
    if log == True:
        y_test_unlog = np.expm1(y_test)
        test_preds_unlog = np.expm1(test_preds)
        print(f"Test MAE Score: ${mean_absolute_error(y_test_unlog, test_preds_unlog):.4f}")
        print(f"Test RMSE Score: ${mean_squared_error(y_test_unlog, test_preds_unlog, squared=False):.4f}")
    else:
        print(f"Test MAE Score: ${mean_absolute_error(y_test, test_preds):.4f}")
        print(f"Test RMSE Score: ${mean_squared_error(y_test, test_preds, squared=False):.4f}")
    print("*"*20)
    
    # Visualize residuals
    plt.scatter(train_preds, y_train-train_preds, label='Train')
    plt.scatter(test_preds, y_test-test_preds, label='Test')

    plt.axhline(y=0, color = 'red', label = '0')
    plt.xlabel('predictions')
    plt.ylabel('residuals')
    plt.legend()
    plt.show()
    
    return train_preds, test_preds