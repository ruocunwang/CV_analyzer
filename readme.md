CV_analyzer.py

## Description
This code performs analysis on _CV Rate Data_ for the characterization of electrochemical energy storage of materials.

## How to use
### Before running the code
#### Data Collection
1. Collect data with a Bio-Logic potentiostat with one CV or CVA technique for each sweep rate.
2. Export the data into _.mpt_ files.
3. Place the _.mpt_ files to be analyzed in a separate folder (I would exclude the conditioning cycles).

#### Software pre-requisites
1. PowerShell
2. Python 3

### Using the code
1. Download the analysis code and place it in a folder that you can find in the future
2. Open PowerShell (if you use Windows)
3. In PowerShell, navigate to the folder that you placed the analysis code (need to add details on how-to)
4. In PowerShell, run the analysis code using "Python CV_analyzer.py"
5. Follow the prompts.

## What it does
Output four text files in a separate folder named "XXX_results": 
1. data_analysis.txt
- Sweep rates, unit: mV/s. They are the independent variables used in cyclic voltammetry to control charge/discharge speed (better definition available).
2. data_E_C.txt
3. data_E_I.txt
4. data_log_b.txt
