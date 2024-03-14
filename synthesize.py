import pandas as pd
import ydata_synthetic.synthesizers
import ydata_synthetic.synthesizers.timeseries

def synthesize_group(group: pd.DataFrame):
	with pd.option_context('display.max_columns', None):
		print(group)
	
	timeseries_synthesizer = ydata_synthetic.synthesizers.timeseries.TimeSeriesSynthesizer(
		modelname = 'timegan',
		model_parameters = ydata_synthetic.synthesizers.ModelParameters(
			batch_size = 128,
			lr         = 5e-4,
			noise_dim  = 32,
			layers_dim = 128,
			latent_dim = 24,
			gamma      = 1,
		),
	)

	timeseries_synthesizer.fit(
		group,
		ydata_synthetic.synthesizers.TrainParameters(
			epochs           = 5,#0,#000,
			sequence_length  = 24,
			number_sequences = len(group.columns),
		),
		num_cols = list(group.columns),
	)

	synthesized_data = timeseries_synthesizer.sample(n_samples = 5)
	return synthesized_data


def main():
	failure_groups_meta = pd.read_parquet('preprocessed_data/group_meta.parquet')
	failure_groups = [
		pd.read_parquet(f'preprocessed_data/group_{group_index}.parquet')
		for group_index in range(failure_groups_meta.shape[0])
	]

	with pd.option_context('display.max_rows', None):
		print(failure_groups_meta)
	
	for (group_index, group_meta), group in zip(failure_groups_meta.iterrows(), failure_groups):
		print(group_index)
		print(group_meta)

		synthesized_data = synthesize_group(group)

		for (j, synthesized_group_block) in enumerate(synthesized_data):
			print(group_index, j)
			synthesized_group_block.to_parquet(f'synthesized_data/versuch1/group_{group_index}_{j}.parquet')

if __name__ == "__main__":
	main()

