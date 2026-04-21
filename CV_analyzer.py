import argparse
import numpy as np
import pandas as pd
from pathlib import Path
import os
from decimal import Decimal
from scipy import stats, integrate

def list_files(folder_path):
    file_list = []
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):
            file_list.append(full_path)
    return file_list

def get_header_num(file):
    # find header line
    with open(file, "r", encoding='windows-1252') as f:
        f.readline()
        line = f.readline()
        header_num = int(line.split()[-1])
        return header_num
    
def read_file(file, cycle):
    # read from header line
    header = get_header_num(file) - 1
    df = pd.read_csv(
        file,
        encoding = 'windows-1252',
        sep = "\t",
        skiprows = header,
        usecols = ["time/s", "Ewe/V", "<I>/mA", "cycle number"]
    )
    return df

def read_all_files(folder_path, cycle, mass):
    files = list_files(folder_path)
    dfs = []

    for i, file in enumerate(files):
        df = read_file(file, cycle)
        df = df[df["cycle number"] == cycle]
        df["file_number"] = i
        df["I/mass"] = df["<I>/mA"] / mass * 1000 # from mg to g
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)

def get_sweep_rate(df):
    file_numbers = sorted(df["file_number"].unique())
    sweep_rates = {}
    for fn in file_numbers:
        sub = df[df["file_number"] == fn]
        t = sub["time/s"].values
        E = sub["Ewe/V"].values

        ini_dat_pt = np.argmax(E)
        end_dat_pt = np.argmin(E)

        raw = abs((E[end_dat_pt] - E[ini_dat_pt]) / (t[end_dat_pt] - t[ini_dat_pt])) * 1000
        rounded = float(f'{raw:.2g}')
        sweep_rates[fn] = rounded if rounded < 1 else int(rounded)

    # Sort by sweep rate value
    sweep_rates = dict(sorted(sweep_rates.items(), key=lambda x: x[1]))
    return sweep_rates  # {file_number: sweep_rate} sorted by sweep rate

def build_header(sweep_rates, col2_label, col2_unit):
        labels = []
        units = []
        rates = []
        for sr in sweep_rates.values():
            labels += ["Potential", col2_label]
            units += ["V", col2_unit]
            rates += [f"{sr} mV/s", f"{sr} mV/s"]
        return pd.MultiIndex.from_arrays([labels, units, rates])

def build_log_table(sweep_rates, peak_currents):
    log_sr = np.array([np.log(sr) for sr in sweep_rates.values()])
    log_ip = np.array([np.log(abs(pc)) for pc in peak_currents])

    slope, intercept, r_value, _, _ = stats.linregress(log_sr, log_ip)

    # Fitted values at min and max of log_sr only
    x_min, x_max = log_sr.min(), log_sr.max()
    y_min = slope * x_min + intercept
    y_max = slope * x_max + intercept

    # Pad to match number of rows
    n = len(log_sr)
    def pad(lst): return lst + [np.nan] * (n - len(lst))

    log_df = pd.DataFrame({
        ("log(V)"): log_sr,
        ("log(I)"): log_ip,
        ("fitted log(V)"): pad([x_min, x_max]),
        ("fitted log(I)"): pad([y_min, y_max]),
        ("b value"): pad([slope]),
        ("R square"): pad([r_value**2]),
    })

    return log_df

def create_output(df, sweep_rates):
    EI_parts = []
    EC_parts = []
    peak_currents = []
    peak_potentials = []
    
    for fn, sr in sweep_rates.items():
        sub = df[df["file_number"] == fn][["Ewe/V", "I/mass"]].reset_index(drop=True)

        # EI table
        ei = sub.copy()
        ei.columns = [f"E_{sr}", f"I_{sr}"]
        EI_parts.append(ei)

        # EC table
        ec = sub.copy()
        ec["I/mass"] = ec["I/mass"] / sr  # F/g
        ec.columns = [f"E_{sr}", f"C_{sr}"]
        EC_parts.append(ec)

        # Peak: max current and its corresponding potential
        I = df[df["file_number"] == fn]["I/mass"].values
        E = df[df["file_number"] == fn]["Ewe/V"].values
        peak_idx = np.argmax(I)
        peak_currents.append(I[peak_idx])
        peak_potentials.append(E[peak_idx])

    # Build peak table (2 cols)
    peak_df = pd.DataFrame({
        ("Peak Potential", "V", "Peak Potential"): peak_potentials,
        ("Peak Current", "mA/g", "Peak Current"): peak_currents,
    })

    # build EI table
    EI = pd.concat(EI_parts, axis=1)
    EI.columns = build_header(sweep_rates, "Current", "mA/g")
    EI = pd.concat([EI, peak_df], axis=1)

    # build EC table
    EC = pd.concat(EC_parts, axis=1)
    EC.columns = build_header(sweep_rates, "Capacitance", "F/g")

    # build log table
    log_df = build_log_table(sweep_rates, peak_currents)
    
    return EI, EC, log_df

def build_summary_table(df, sweep_rates, NW):
    rows = []
    for fn, sr in sweep_rates.items():
        sub = df[df["file_number"] == fn].copy()
        E = sub["Ewe/V"].values
        I = sub["I/mass"].values  # mA/g
        t = sub["time/s"].values

        voltage_window = round(E.max() - E.min(), 2)

        # split into cathodic (I < 0) and anodic (I >= 0)
        cath = I < 0
        anod = I >= 0

        # integrate over time (mA/g * s = mAs/g) and convert to mAh/g
        cath_cap = abs(integrate.trapezoid(I[cath], t[cath])) / 3600
        anod_cap = abs(integrate.trapezoid(I[anod], t[anod])) / 3600

        rows.append({
            "sr": sr,
            "voltage_window": voltage_window,
            "cath_cap": cath_cap,
            "anod_cap": anod_cap,
        })
    summary = pd.DataFrame(rows)

    max_cath = summary["cath_cap"].max()
    max_anod = summary["anod_cap"].max()
    
    summary_df = pd.DataFrame({
        ("Sweep Rate", "mV/s", ""): summary["sr"],
        ("Voltage Window", "V", ""): summary["voltage_window"],
        ("Cathodic Specific Capacity", "mAh/g", ""): summary["cath_cap"],
        ("Anodic Specific Capacity", "mAh/g", ""): summary["anod_cap"],
        ("Cathodic Specific Capacitance", "F/g", ""): summary["cath_cap"] * 3.6 / summary["voltage_window"],
        ("Anodic Specific Capacitance", "F/g", ""): summary["anod_cap"] * 3.6 / summary["voltage_window"],
        ("Coulombic Efficiency", "", ""): summary["anod_cap"] / summary["cath_cap"] * 100,
        ("#e Cathodic", "", ""): summary["cath_cap"] * NW / 96485.3329 * 3.6,
        ("#e Anodic", "", ""): summary["anod_cap"] * NW / 96485.3329 * 3.6,
        ("Rate Capability Cathodic", "", ""): summary["cath_cap"] / max_cath,
        ("Rate Capability Anodic", "", ""): summary["anod_cap"] / max_anod,
    })

    return summary_df

def main(folder_path, cycle, mass, MW=0):
    # create folder for output
    folder = Path(folder_path).resolve()
    new_folder = folder.parent / f"{folder.stem}_results"
    new_folder.mkdir(exist_ok=True)
    print(f"Result folder {new_folder} created...")

    # data read in
    print(f"Reading data...")
    df = read_all_files(folder, cycle, mass)
    print("Data reading and prep complete...")

    # get sweep rates
    sweep_rates = get_sweep_rate(df)

    # create EI, EC and log_df
    EI, EC, log_df = create_output(df, sweep_rates)

    # create summary table
    summary_df = build_summary_table(df, sweep_rates, MW)
    print("Output tables created...")

    # write output to txt files
    EI_path = new_folder / f"{folder.stem}_E_I.txt"
    EI.to_csv(EI_path, sep="\t", float_format="%.4f", index=False)

    EC_path = new_folder / f"{folder.stem}_E_C.txt"
    EC.to_csv(EC_path, sep="\t", float_format="%.4f", index=False)

    log_path = new_folder / f"{folder.stem}_log_b.txt"
    log_df.to_csv(log_path, sep="\t", float_format="%.6f", index=False)

    summary_path = new_folder / f"{folder.stem}_analysis.txt"
    summary_df.to_csv(summary_path, sep="\t", float_format="%.6f", index=False)
    print("Output tables written to disk...")

def get_inputs():
    folder_path = input("Enter folder path: ").strip()
    cycle = int(input("Enter cycle number: ").strip())
    mass =float(input("Enter mass (mg): ").strip())
    mw_input = input("Enter molecular weight (g/mol) [optional, press Enter to skip]: ").strip()
    MW = float(mw_input) if mw_input else 0
    return folder_path, cycle, mass, MW


if __name__ == "__main__":
    folder_path, cycle, mass, MW = get_inputs()
    main(folder_path=folder_path, cycle=cycle, mass=mass, MW=MW)
