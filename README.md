# NAMD-Config-Generator
#### Config file generator for easier simulations with the Nanoscale Molecular Dynamics (NAMD) software. 
## Why use a config generator?
- It's easy to make typos when manually writing each parameter in the config file.
- It's difficult to find the names of every required field when making a config file.
- UI that can auto-format your values into a valid config file.
- Changing file extensions manually can be annoying.
## Installation
1. Clone this repository using `git clone https://github.com/shmoe6/NAMD-Config-Generator.git`.
2. Locate the folder of `main.py`.
3. Put the following required files for simulation in the same folder as `main.py`:
   1. Coordinates file (`.pdb`)
   2. Structure file (`.psf`)
   3. Paremeters file (`.prm`)
## Usage
1. Open up the folder containing this repository and your simulation files.
2. Run `main.py` and input the names of each file.
3. Using the UI, tweak config values as needed.
   1. Fields labeled "leave as is" should be left alone except in very specific cases.
4. When finished, click the **generate** button. 
5. The output file will be stored in the same folder. It will be titled `runconfig.namd`. 