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


## Results description
The script creates a new directory called [Your_Folder_Name]_results in the same directory as your source data. It has .txt files inside it that are made for easy plotting in software like OriginLab, Prism, or Excel.

### Example Visualizations of Graphs 
<img width="1050" height="900" alt="Graph12" src="https://github.com/user-attachments/assets/bf766bc8-a7fb-4af1-920b-6d21dd98fccc" />

<img width="1050" height="900" alt="Graph12" src="https://github.com/user-attachments/assets/08a46604-8c9c-4f97-bae3-a1d78d966895" />

<img width="1050" height="900" alt="Graph6" src="https://github.com/user-attachments/assets/8c49c4f9-fd3c-4057-bf1c-554ff8a3a442" />

<img width="1050" height="900" alt="Graph5" src="https://github.com/user-attachments/assets/50751e4a-333b-42c2-bbe8-747fc43030ae" />

<img width="1050" height="900" alt="Graph4" src="https://github.com/user-attachments/assets/d7ecaeee-eaa3-41d6-84db-aa1cea7f8d2a" />

<img width="1050" height="900" alt="Graph3" src="https://github.com/user-attachments/assets/c55903b8-8670-4cc1-98ea-666445e5c010" />

<img width="1050" height="900" alt="Graph2" src="https://github.com/user-attachments/assets/09cd8283-b573-4392-8e6a-70b90787a2c2" />

<img width="1050" height="900" alt="Graph9" src="https://github.com/user-attachments/assets/f49952ca-c55a-4961-abca-d5d71680cdf3" />

<img width="1050" height="900" alt="Graph8" src="https://github.com/user-attachments/assets/eda9595e-a972-4b98-8bbe-2d3641041862" />

<img width="1050" height="900" alt="Graph7" src="https://github.com/user-attachments/assets/b44c2ca0-b85a-4742-82ab-672a88f7b08a" />

<img width="1050" height="900" alt="Graph1" src="https://github.com/user-attachments/assets/662ce756-7cd2-46f5-91c8-55298d880951" />

<img width="1050" height="900" alt="Graph14" src="https://github.com/user-attachments/assets/12212f20-d06d-4d82-99a0-e999fd2bdc91" />


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

### 3a. [Folder]_E_C.txt: (Potential vs. Specific Capacitance)
   - Calculates specific capacitance (F/g) as a function of potential for every sweep rate using C = I / (m × v), where I is current (A), m is the mass of the active material (g), and v is the scan rate (V/s).
  
### 3b. [Folder]_E_C.txt: Additional Capacity Analysis
  - Calculates the material's specific capacity measured in mAh/g.

### 3c. [Folder]_E_C.txt: Coulombic Efficiency
  - Tracks the efficiency percentage of the charge-discharge cycles across different scan rates.

### 3d. [Folder]_E_C.txt: Capacitance Retention
  - Outlines the rate capability performance by evaulating capacitance retenations as scan rates increase.

### 3e. [Folder]_E_C.txt: Coulombic Efficiency
  - Monitors the cacluated number of electrones transffered during the anodic and cathodic sweeps across diffrent scan rates.

### 4. [Folder]_log_b.txt: (Kinetics and b-Value Analysis)
   - Gives the linear regression data needed to find charge storage kinetics using the Power Law Relationship.
   - Outputs calculated b-values as slopes and R^2 fit values to differentiate between diffusion-controlled (b = 0.5) and surface-controlled (b = 1.0) processes.
   1. log(v): The logarithm of the experimental scan rate.
   2. log(I): The logarithm of the experimental peak current.
   3. Fitted log(V): The scan rate values mapped across the linear regression model.
   4. Fitted log(I): The predicted peak current values generated along the calculated linear fit line.
   5. b value: The calculated slope extracted from the linear regression line used to define the dominant charge storage mechanism.
   6. R square: The coefficient of determination indicating the quality and accuracy of the linear regression fit.
  
