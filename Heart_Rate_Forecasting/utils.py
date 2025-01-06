
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np

def detect_anomalies(df, columns):
    anomaly_data = {
        'column_name': [],
        'negative_values': [],
        'spikes': [],
        'zeros': [],
        'nan_values': []
    }
    
    for col in columns:
        if col in df.columns:
            col_data = df[col]
            negative_values_count = (col_data < 0).sum()
            mean = col_data.mean()
            std = col_data.std()
            spike_threshold = 4 * std
            spikes_count = (np.abs(col_data - mean) > spike_threshold).sum()
            zeros_count = (col_data == 0).sum()
            nan_values_count = col_data.isna().sum()
            anomaly_data['column_name'].append(col)
            anomaly_data['negative_values'].append(negative_values_count)
            anomaly_data['spikes'].append(spikes_count)
            anomaly_data['zeros'].append(zeros_count)
            anomaly_data['nan_values'].append(nan_values_count)
    anomaly_df = pd.DataFrame(anomaly_data)
    
    return anomaly_df
