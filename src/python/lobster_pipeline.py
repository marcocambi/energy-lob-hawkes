import numpy as np
def process_lobster_timestamps(
    file_path: str,
    session_start: float = 34200.0,
    session_end: float = 57600.0,
    jitter: float = 1e-7,
) -> np.ndarray:
    df = pd.read_csv(
        file_path, header=None, usecols=[0, 1], names=["time", "event_type"]
    )

    df = df[(df["time"] >= session_start) & (df["time"] <= session_end)]
    df = df[df["event_type"].isin([4, 5])]

    timestamps = np.sort(df["time"].to_numpy() - session_start)

    # Fix tie-collapsing: np.unique() cancellava eventi simultanei,
    # sottostimando l'intensità proprio nei burst. Qui si aggiunge un
    # jitter deterministico crescente ai duplicati: nessun evento viene
    # perso, l'ordine resta stretto, il jitter (1e-7s) è trascurabile per la MLE.
    change = np.concatenate(([True], timestamps[1:] != timestamps[:-1]))
    group_start = np.where(change)[0]
    group_id = np.cumsum(change) - 1
    idx_in_group = np.arange(len(timestamps)) - group_start[group_id]

    return timestamps + idx_in_group * jitter


if __name__ == "__main__":
    print("Funzione caricata con successo! Pronto per l'analisi.")
