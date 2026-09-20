import numpy as np
import pandas as pd

def process_energy_timestamps(
    file_path: str,
    contract_type: str = "CO",
) -> np.ndarray:
   df = pd.read_csv(file_path)
   df = df[df["contract_type"] == contract_type]
   timestamps = df["execution_timestamp"].to_numpy()
   timestamps = np.sort(timestamps)
   return timestamps

if __name__ == "__main__":
    print("Scheletro energy pipeline caricato — schema dati da confermare.")