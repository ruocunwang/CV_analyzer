CV_analyzer.py

## Description
This is a data processing tool designed to automate the analysis of CV rate data collected. This is done for the characterization of electrochemical energy storage materials by extracting kinetics,capacity, and capacitance metrics from Bio-logic potentiostat raw exports.

## How to use
### Getting started
#### Data Collection
1. Collect CV or CVA data using a Bio-Logic potentiostat, using a single file for each sweep rate.
2. Export the raw data curves directly into standard text-based .mpt files.
3. Place the _.mpt_ files to be analyzed in a separate folder (I would exclude the conditioning cycles).

#### Setup
- Operating System: Windows, macOS, or Linux
- Command-line interface: PowerShell/GitBash (Windows) or Terminal (macOS/Linux)
- Environment: Python 3.x [How to install Python in Command-line interface](https://learn.microsoft.com/en-us/windows/dev-environment/python?tabs=winget)
- Required Libraries: Install by copy and pasting the following code into your command line:
  ```
  python -m pip install numpy pandas scipy
  ```


### Running the code
1. Open your command-line interface (ie. PowerShell/GitBash on Windows or Terminal on Mac).
2. Find the directory where you want to put the repo (cd) command:
   ```sh
   cd “path\to\your\code\folder”
   ```
3. Clone the repo to the directory
   ```sh
   git clone https://github.com/ruocunwang/CV_analyzer.git
   ```
4. Navigate to the repo directory
   ```sh
   cd CV_analyzer
   ```
6. In the command-line interface, run the analysis code using
   ```sh
   Python CV_analyzer.py
   ```
7. Follow the prompts:
   1. Folder Path: The location of your .mpt file
   2. Cycle number: The cycle number you want to analyze.
   3. Active mass: The mass of your electrochemically active material.
   4. Molecular Weight: Press Enter to skip, or provide it if wanted.


## What it does
The script creates a new directory called [Your_Folder_Name]_results in the same directory as your source data. It has .txt files inside it that are made for easy plotting in software like OriginLab, Prism, or Excel.

### 1. [Folder]_Analysis.txt: (Data Summary)
   1. **Sweep Rates (mV/s):** The rate at which voltage is scanned during cyclic voltammetry.
   2. **Voltage Window (V):** The operational potential window.
   3. **Cathodic Specific Capacity (mAh/g):** Integrated cathodic current with respect to time normalized by the active mass.
   4. **Anodic Specific Capacity (mAh/g):** Integrated anodic current with respect to time normalized by the active mass.
   5. **Cathodic Specific Capacitance (F/g):** Cathodic specific capacity divided by the voltage window.
   6. **Anodic Specific Capacitance (F/g):** Anodic specific capacity divided by the voltage window.
   7. **Coulombic Efficiency (%):** The ratio of anodic to cathodic capacity.
   8. **Cathodic Electron Transfer:** The fractional number of electrons transferred during the cathodic process calculated using Faraday's law of electrolysis (requires Molecular Weight input).
   9. **Anodic Electron Transfer:** The fractional number of electrons transferred during the anodic process calculated using Faraday's law of electrolysis (requires Molecular Weight input).
   10. **Cathodic Rate Capability:** Normalized performance retention relative to the maximum cathodic capacity.
   11. **Anodic Rate Capability:** Normalized performance retention relative to the maximum anodic capacity.

### 2. [Folder]_E_I.txt: (Potential vs. Current Density)
   - Organize potential (V) and normalized current density (mA/g) from all analyzed sweep rates into columns, ordered from lowest to highest sweep rate (left to right).
   - Append isolated peak anodic currents and their corresponding potential are also located in the last two columns of the dataset.

### 3. [Folder]_E_C.txt: (Potential vs. Specific Capacitance)
   - Calculates specific capacitance (F/g) as a function of potential for every sweep rate using C = I / (m × v), where I is current (A), m is the mass of the active material (g), and v is the scan rate (V/s).

### 4. [Folder]_log_b.txt: (Kinetics and b-Value Analysis)
   1. Gives the linear regression data needed to find charge storage kinetics using the Power Law Relationship.
   2. Outputs calculated b-values as slopes and R^2 fit values to differentiate between diffusion-controlled (b = 0.5) and surface-controlled (b = 1.0) processes.
   3. log(v): The logarithm of the experimental scan rate.
   4. log(I): The logarithm of the experimental peak current.
   5. Fitted log(V): The scan rate values mapped across the linear regression model.
   6. Fitted log(I): The predicted peak current values generated along the calculated linear fit line.
   7. b value: The calculated slope extracted from the linear regression line used to define the dominant charge storage mechanism.
   8. R square: The coefficient of determination indicating the quality and accuracy of the linear regression fit.
