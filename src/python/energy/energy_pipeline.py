import numpy as np
import pandas as pd


def process_energy_timestamps(
    file_path: str,
    contract_type: str = "CO",
) -> np.ndarray:
    """
    Parser per dati EPEX Spot / ICE intraday continuous trading.

    Schema colonne da confermare quando arrivano i dati reali (in attesa
    di risposta EPEX). Ipotesi basata sulla letteratura (Deschatre & Gruet
    2022, Graf von Luckner & Kiesel 2021): execution timestamp, buy/sell
    indicator, delivery period, price, volume.

    TODO: sostituire nomi colonna placeholder con quelli reali del dataset
    TODO: confermare risoluzione temporale (secondi vs millisecondi)
    TODO: confermare se serve lo stesso fix di tie-collapsing di equity/
          (probabile: mercati continui hanno gli stessi problemi di tick
          simultanei)
    """
df = pd.read_csv(file_path)
df = df[df["contract_type"] == contract_type]

    timestamps = df["execution_timestamp"].to_numpy()
    timestamps = np.sort(timestamps)

    return timestamps

if __name__ == "__main__":
    print("Scheletro energy pipeline caricato — schema dati da confermare.")
