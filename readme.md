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
   cd <path\to\your\code\folder>
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
   1. Folder Path: The location of your .mpt file. Don't include the quotation mark.
   2. Cycle number: The cycle number you want to analyze.
   3. Active mass: The mass of your electrochemically active material.
   4. Molecular Weight: Press Enter to skip, or provide it if wanted.

### Results Location
After analysis is complete, the software cerates a folder named :[Original_Folder_Name]_results

Example:
If your data are stored in a folder named "CV_Data"
Then, your analysis results will be placed in a new folder named "CV_Data_Results".

All generated analysis files are stored inside this new results folder.

## Results description
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
   
#### Example Visualizations
<br> <img width="556" height="308" alt="Screenshot 2026-07-10 111252" src="https://github.com/user-attachments/assets/81f7e7b8-4b5d-4ea9-9ef8-57fad38bae3b" />

### 2. [Folder]_E_I.txt: (Potential vs. Current Density)
   - Organize potential (V) and normalized current density (mA/g) from all analyzed sweep rates into columns, ordered from lowest to highest sweep rate (left to right).
   - Append isolated peak anodic currents and their corresponding potential are also located in the last two columns of the dataset.

#### Example Visualization
<br> <img width="517" height="425" alt="Screenshot 2026-09-03 180146" src="https://github.com/user-attachments/assets/07119698-eb3a-4fe1-9dec-9ef05fca7761" />

### 3. [Folder]_E_C.txt: (Potential vs. Specific Capacitance)
   - Calculates specific capacitance (F/g) as a function of potential for every sweep rate using C = I / (m × v), where I is current (A), m is the mass of the active material (g), and v is the scan rate (V/s).

#### Example Visualization
<br> <img width="518" height="446" alt="Screenshot 2026-09-03 172617" src="https://github.com/user-attachments/assets/5ff58656-1616-4b85-9d12-569c83a422d8" />

### 4. [Folder]_log_b.txt: (Kinetics and b-Value Analysis)
   - Gives the linear regression data needed to find charge storage kinetics using the Power Law Relationship.
   - Outputs calculated b-values as slopes and R^2 fit values to differentiate between diffusion-controlled (b = 0.5) and surface-controlled (b = 1.0) processes.
   1. log(v): The logarithm of the experimental scan rate.
   2. log(I): The logarithm of the experimental peak current.
   3. Fitted log(V): The scan rate values mapped across the linear regression model.
   4. Fitted log(I): The predicted peak current values generated along the calculated linear fit line.
   5. b value: The calculated slope extracted from the linear regression line used to define the dominant charge storage mechanism.
   6. R square: The coefficient of determination indicating the quality and accuracy of the linear regression fit.

#### Example Visualization
<br> <img width="557" height="313" alt="Screenshot 2026-07-10 111404" src="https://github.com/user-attachments/assets/903538e4-27d5-4e97-a3d4-df60a423c8d2" />
  
## Sample Data
A sample dataset is included in this repository for users who want to practice using the code.

### Included files

- **.mpr file:** The `.mpr` file is the original Bio-Logic data format and can only be opened using EC-Lab software. Users can use this file to practice exporting the data into an `.mpt` format.
- **.mpt file:** The `.mpt` file is the text-based format usable by `CV_analyzer.py` and can be analyzed directly using the code. Users who do not have access to EC-Lab software can use the `.mpt` file to practice using the code.

### Sample Experimental Parameters
The sample dataset comes from Ti₃C₂Tₓ, a thin film electrode (Tₓ = –O, –OH, –Cl, and –F) in 5 M H₂SO₄ electrolyte.

<br>Active mass = 0.041 mg
<br>Molecular Weight = 204.65 g/mol
<br>Reference Electrode = Hg/Hg₂SO₄ / K2SO4 (sat'd)
<br>Counter Electrode: Activated Carbon
<br>Environment: Room temperature
<br>Initial state: -378.7 mV vs Hg/Hg₂SO₄

<br>When using the sample dataset enter:
<br>Active Mass: 0.041
<br>Molecular Weight = 204.65
