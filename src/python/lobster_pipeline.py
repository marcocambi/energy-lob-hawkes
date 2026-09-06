import numpy as np
import pandas as pd


def process_lobster_timestamps(
    file_path: str, session_start: float = 34200.0, session_end: float = 57600.0
) -> np.ndarray:
    df = pd.read_csv(
        file_path, header=None, usecols=[0, 1], names=["time", "event_type"]
    )

    df = df[(df["time"] >= session_start) & (df["time"] <= session_end)]

    df = df[df["event_type"].isin([4, 5])]

    timestamps = df["time"].to_numpy() - session_start

    timestamps = np.unique(timestamps)

    return timestamps

if __name__ == "__main__":
    print("Funzione caricata con successo! Pronto per l'analisi.")