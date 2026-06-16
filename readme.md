CV_analyzer.py

## Description
This is a data processing tool designed to automate the analysis of CV rate data collected. This is done for the characterization of electrochemical energy storage materials by extracting kinetics,capacity, and capacitance metrics from Bio-logic potentiostat raw exports.

## How to use
### Before running the code
#### Data Collection
1. Collect CV or CVA data using a Bio-logic potentiostat, using a single file for each sweep rate.
2.Export the raw data curves directly into standard text-based .mpt files.
3. Place the _.mpt_ files to be analyzed in a separate folder (I would exclude the conditioning cycles).

#### Software pre-requisites
Operating System : Windows, macOS, or Linux
Command Line: PowerShell (Windows) or Terminal (macOS/Linux)
Environment: Python 3.x
Required Libraries: Install by copy and pasting the following code into your command line: python -m pip install numpy pandas scipy


### Using the code
1. Download CV_analyzer.py and place it in your working directory
2. Open your command-line interface (ie. PowerShell on Windows).
3. Find the directory containing the script using the change directory (cd) command: cd “path\to\your\code\folder”
4. In PowerShell, run the analysis code using "Python CV_analyzer.py"
5. Follow the prompts:
  a. Folder Path: The location of you .mpt file
  b. Cycle number: The cycle number you want to analyze.
  c. Active mass: The mass of your electrochemically active material.
  d. Molecular Weight: Press Enter to skip, or provide it if wanted.


## What it does
The script creates a new directory called [Your_Folder_Name]_results in the same directory as your source data. It has .txt files inside it that are made for easy plotting in software like OriginLab, Prism, or Excel.

1. [Folder]_Analysis.txt: (Data Summary)
  a. Sweep Rates (mV/s): The rate at which voltage is scanned during cyclic     voltammetry.
  b. Voltage Window: The operational potential window.
  c.Cathodic Specific Capacity: integrated current with respect to time in the cathodic cycle in the unit of mAh/g.
  d. Anodic Specific Capacity: Integrated current with respect to time in the anodic cycle in units of mAh/g.
  e. Specific Capacitance: Calculated directly from capacity metrics relative to the voltage window.
  f. Coulombic Efficiency: The ratio of anodic to cathodic capacity.
  g. Cathodic Electron Transfer Data: The fractional number of electrons transferred during the cathodic process (requires Molecular Weight input).
  h. Anodic Electron Transfer Data: The fractional number of electrons transferred during the anodic process (requires Molecular Weight input).
  i. Cathodic Rate Capability: Normalized performance retention relative to the maximum observed cathodic capacity.
  j. Anodic Rate Capability: Normalized performance retention relative to the maximum observed anodic capacity.

3. [Folder]_E_I.txt: (Potential vs. Current Density)
  a.Organizes potential (V) and normalized current density (mA/g) from all analyzed sweep rates into columns, ordered from lowest to highest sweep rate (left to right).
  b. Appends isolated peak anodic currents and their corresponding potential are also located in the last two columns of the dataset.

4. [Folder]_E_C.txt: (Potential vs. Specific Capacitance)
  a. Calculates specific capacitance (F/g) as a function of potential for every sweep rate using C = I / (m × v), where I is current (A), m is the mass of the active material (g), and v is the scan rate (V/s).

5. [Folder]_log_b.txt: (Kinetics and b-Value Analysis)
  a. Gives the linear regression data needed to find charge storage kinetics using the Power Law Relationship.
  b. Outputs calculated b-values as slopes and R^2 fit values to differentiate between diffusion-controlled (b = 0.5) and surface-controlled (b = 1.0) processes.
  c. log(v): The logarithm of the experimental scan rate.
  d. log(I): The logarithm of the experimental peak current.
  e. Fitted log(V): The scan rate values mapped across the linear regression model.
  f. Fitted log(I): The predicted peak current values generated along the calculated linear fit line.
  g. b value: The calculated slope extracted from the linear regression line used to define the dominant charge storage mechanism.
 h. R square: The coefficient of determination indicating the quality and accuracy of the linear regression fit.
