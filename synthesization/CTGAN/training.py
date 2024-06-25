import pandas as pd
import numpy as np
from sklearn import cluster

from ydata_synthetic.synthesizers import ModelParameters, TrainParameters
from ydata_synthetic.synthesizers.regular import RegularSynthesizer

# Read the original data and have it preprocessed
data = pd.read_parquet(f'E:\m2hycon\Thesis\SyntheticDataGeneration\data\preprocessed/v7-truncated-50ts-f1.parquet')
data.dropna(inplace=True, axis=0)

cat_cols = [
	'misalignment_cd_vs_ld',
]

num_cols = data.columns.tolist()
num_cols = [item for item in num_cols if item not in cat_cols]


# Defining the training parameters
batch_size = 500
epochs = 1000+1
learning_rate = 2e-4
beta_1 = 0.5
beta_2 = 0.9

ctgan_args = ModelParameters(batch_size=batch_size,
                             lr=learning_rate,
                             betas=(beta_1, beta_2))

train_args = TrainParameters(epochs=epochs)

# Fit the synthesizer and save the model to disk for later use in sampling
synth = RegularSynthesizer(modelname='ctgan', model_parameters=ctgan_args)
synth.fit(data=data, train_arguments=train_args, num_cols=num_cols, cat_cols=[])
synth.save("v7-f1-ctgan.pkl")
synth_data = synth.sample(1000)
synth_data.to_parquet('v8-f1.parquet')