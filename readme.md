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
Required Libraries: Install through your command line : pip install numpy pandas scipy

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
  a. Voltage Window: The operational potential window.
  b. Specific Capacity: Separated into integrated cathodic and anodic sweep values.
  c. Specific Capacitance: Calculated directly from capacity metrics relative to the voltage window.
  d. Coulombic Efficiency: The ratio of anodic to cathodic capacity.
  e. Electron Transfer Data: The fractional number of electrons transferred during cathodic and anodic process (requires        Molecular Weight input).
  f. Rate Capability: Normalized performance retention relative to the maximum observed capacity.

2. [Folder]_E_I.txt: (Potential vs. Current Density)
  a. Organizes normalized current density (mA/g) and potential (V) from all analyzed sweep rates into the columns.
  b. Appends isolated peak anodic currents and their corresponding potential are also located at the end of the dataset.

3. [Folder]_E_C.txt: (Potential vs. Specific Capacitance)
  a. Calculates specific capacitance (F/g) as a function of potential for every sweep rate using the relation C= I/(m x v).

4. [Folder]_log_b.txt: (Kinetics and b-Value Analysis)
  a. Gives the linear regression data needed to find charge storage kinetics using the Power Law Relationship.
  b. Outputs calculated b-values as slopes and R^2 fit values to differentiate between diffusion-controlled (b = 0.5) and       surface-controlled (b = 1.0) processes.


   



