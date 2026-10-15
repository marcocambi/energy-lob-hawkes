import pandas as pd
import numpy as np

def load_and_filter_trades(file_path: str) -> np.ndarray:
    columns = ["time", "event_type", "order_id", "size", "price", "direction"]

    df = pd.read_csv(file_path, header = None, names=columns)

    trades = df[df["event_type"] == 4]

    timestamps = trades["time"].values,astype(np.float64)

    timestamps = np.unique(timestamps)

    return timestamps

if __name__ == "__main__":
    import os
    data_filename = "AAPL_2012-06-21_34200000_57600000_message_5.csv"

    file_path = os.path.join()

    print(f"Caricamento e filtraggio dei dati da: {file_path}")

    try:
        timestamps = load_and_filter_trades(file_path)

        print("\n--- Pipeline Execution Report ---")
        print(f"Status: SUCCESS")
        print(f"Total unique trade timestamps: {len(timestamps)}")
        print(f"First 5 timestamps (seconds from midnight): {timestamps[:5]}")
        print(f"Last 5 timestamps (seconds from midnight): {timestamps[-5:]}")

    except FileNotFoundError:
        print(f"Errore: Il file {file_path} non è stato trovato. Verifica il nome esatto nella cartella data/.")
    except Exception as e:
        print(f"Errore imprevisto durante l'esecuzione: {e}")