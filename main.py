import tkinter as tk

window = tk.Tk()
window.title('NAMD Config Generator')

frame = tk.Frame(window)
frame.pack()

END = -1


# ----- Methods ----- #
def maxMin(pdbfile: str, segment="all", residue="all", atomtype="all", firstatom="all", lastatom="all"):
    with open(pdbfile, 'r') as f:
        file_contents = f.read().splitlines()

    natoms = 0
    xmin, ymin, zmin = float('inf'), float('inf'), float('inf')
    xmax, ymax, zmax = float('-inf'), float('-inf'), float('-inf')

    for line in file_contents:
        if line.startswith("ATOM") or line.startswith("HETATM"):
            natoms += 1
            ss = line[72:76].strip()
            rt = line[17:21].strip()
            at = line[12:16].strip()
            considerforbounds = True
            if firstatom != "all" and natoms < int(firstatom):
                consider = False
            if lastatom != "all" and natoms > int(lastatom):
                consider = False
            if segment != "all" and ss != segment:
                consider = False
            if residue != "all" and rt != residue:
                consider = False
            if atomtype != "all" and at != atomtype:
                consider = False
            if considerforbounds:
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                xmin = min(xmin, x)
                ymin = min(ymin, y)
                zmin = min(zmin, z)
                xmax = max(xmax, x)
                ymax = max(ymax, y)
                zmax = max(zmax, z)
    print(f"cellOrigin {(xmax + xmin) / 2:.3f} {(ymax + ymin) / 2:.3f} {(zmax + zmin) / 2:.3f}")

    # returns cellBasisVectors 1-3 as well as the cell origin
    return f'{xmax - xmin:.3f} 0 0', \
           f'0 {ymax - ymin:.3f} 0', \
           f'0 0 {zmax - zmin:.3f}', \
           f'{(xmax + xmin) / 2:.3f} {(ymax + ymin) / 2:.3f} {(zmax + zmin) / 2:.3f}'


def generateConfig():
    print('button pressed')

    with open('runconfig.namd', 'w') as file:
        # input
        file.write('# ----- input ----- #\n')
        file.write(f'coordinates\t\t{coordinateFileInput.get()}\n')
        file.write(f'structure\t\t{structureFileInput.get()}\n')
        file.write(f'parameters\t\t{parametersFileInput.get()}\n')
        file.write(f'paratypecharmm\t\t{paraTypeCharmmInput.get()}\n')
        file.write(f'#bincoordinates\t\t{binCoordinatesInput.get()}\n')
        file.write(f'#binvelocities\t\t{binVelocitiesInput.get()}\n')

        # output
        file.write('\n# ----- output ----- #\n')
        file.write(f'set output\t\t{outputNameInput.get()}\n\n')
        file.write('outputname\t\t${output}\n')
        file.write(f'dcdfile\t\t{dcdFileNameInput.get()}\n')
        file.write(f'xstFile\t\t{xstFileNameInput.get()}\n')
        file.write(f'dcdfreq\t\t{dcdFrequencyInput.get()}\n')
        file.write(f'xstFreq\t\t{xstFrequencyInput.get()}\n')
        file.write(f'binaryoutput\t\t{binaryOutputInput.get()}\n')
        file.write(f'binaryrestart\t\t{binaryRestartInput.get()}\n')
        file.write(f'outputEnergies\t\t{outputEnergyInput.get()}\n')
        file.write(f'restartFreq\t\t{restartFrequencyInput.get()}\n')

        # Basic dynamics
        file.write('\n# ----- Basic dynamics ----- #\n')
        file.write(f'exclude\t\t{excludeInput.get()}\n')
        file.write(f'1-4scaling\t\t{oneFourScalingInput.get()}\n')
        file.write(f'COMmotion\t\t{comMotionInput.get()}\n')
        file.write(f'dielectric\t\t{dielectricInput.get()}\n')

        # Simulation space partitioning
        file.write('\n# ----- Simulation space partitioning ----- #\n')
        file.write(f'switching\t\t{switchingInput.get()}\n')
        file.write(f'switchdist\t\t{switchingDistanceInput.get()}\n')
        file.write(f'cutoff\t\t{cutoffInput.get()}\n')
        file.write(f'pairlistdist\t\t{pairlistDistanceInput.get()}\n')

        # Multiple timestepping
        file.write('\n# ----- Multiple timestepping ----- #\n')
        file.write(f'firsttimestep\t\t{firstTimestepInput.get()}\n')
        file.write(f'timestep\t\t{timestepInput.get()}\n')
        file.write(f'stepspercycle\t\t{stepsPerCycleInput.get()}\n')

        # Temperature control
        file.write('\n# ----- Temperature control ----- #\n')
        file.write(f'set temperature\t\t{temperatureInput.get()}\n')
        file.write('temperature\t\t$temperature\n')

        # Langevin dynamics
        file.write('\n# ----- Langevin dynamics ----- #\n')
        file.write(f'langevin\t\t{langevinInput.get()}\n')
        file.write(f'langevinDamping\t\t{langevinDampingInput.get()}\n')
        file.write('langevinTemp\t\t$temperature\n')

        # run maxmin algorithm to get cell basis vectors
        basisvec1, basisvec2, basisvec3, origin = maxMin(coordinateFileInput.get())

        # Periodic simulation
        file.write('\n# ----- Periodic simulation ----- #\n')
        file.write(f'PME\t\t{pmeInput.get()}\n')
        file.write(f'PMEGridSizeX\t\t{round(float(basisvec1.split()[0]))}\n')
        file.write(f'PMEGridSizeY\t\t{round(float(basisvec2.split()[1]))}\n')
        file.write(f'PMEGridSizeZ\t\t{round(float(basisvec3.split()[2]))}\n\n')
        file.write(f'useGroupPressure\t\t{groupPressureInput.get()}\n\n')
        file.write(f'LangevinPiston\t\t{langevinPistonInput.get()}\n')
        file.write(f'LangevinPistonTarget\t\t{targetPressureInput.get()}\n')
        file.write(f'LangevinPistonPeriod\t\t{pistonPeriodInput.get()}\n')
        file.write(f'LangevinPistonDecay\t\t{pistonDecayInput.get()}\n')
        file.write(f'LangevinPistonTemp\t\t{pistonTempInput.get()}\n')

        # Periodic boundary conditions
        file.write('\n# ----- Periodic boundary conditions ----- #\n')
        file.write(f'cellBasisVector1\t\t{basisvec1}\n')
        file.write(f'cellBasisVector2\t\t{basisvec2}\n')
        file.write(f'cellBasisVector3\t\t{basisvec3}\n')
        file.write(f'cellOrigin\t\t{origin}\n\n')
        file.write(f'wrapWater\t\t{wrapWaterInput.get()}\n')
        file.write(f'wrapNearest\t\t{wrapNearestInput.get()}\n')
        file.write(f'wrapAll\t\t{wrapAllInput.get()}\n')

        # Scripting
        file.write('\n# ----- Scripting ----- #\n')
        file.write(f'minimize\t\t{minimizeInput.get()}\n')
        file.write(f'reinitvels\t\t{reinitVelsInput.get()}\n')
        file.write(f'run {runStepsInput.get()}\n')

        # END
        file.write('END')


# ----- input ----- #
inputFrame = tk.LabelFrame(frame, text="Input")
inputFrame.grid(row=0, column=0)

# coordinates
coordinateFileLabel = tk.Label(inputFrame, text="Coordinates file (.pdb)")
coordinateFileLabel.grid(row=0, column=0)
coordinateFileInput = tk.Entry(inputFrame)
coordinateFileInput.grid(row=0, column=1)

# structure
structureFileLabel = tk.Label(inputFrame, text="Structure file (.psf)")
structureFileLabel.grid(row=1, column=0)
structureFileInput = tk.Entry(inputFrame)
structureFileInput.grid(row=1, column=1)

# parameters
parametersFileLabel = tk.Label(inputFrame, text="Parameters file (.prm)")
parametersFileLabel.grid(row=2, column=0)
parametersFileInput = tk.Entry(inputFrame)
parametersFileInput.grid(row=2, column=1)

# paraTypeCharmm
paraTypeCharmmLabel = tk.Label(inputFrame, text="Using Charmm?")
paraTypeCharmmLabel.grid(row=3, column=0)
paraTypeCharmmInput = tk.StringVar(inputFrame)
paraTypeCharmmInput.set("yes")
paraTypeCharmmInputMenu = tk.OptionMenu(inputFrame, paraTypeCharmmInput, *["yes", "no"])
paraTypeCharmmInputMenu.grid(row=3, column=1)

# #bincoordinates
binCoordinatesLabel = tk.Label(inputFrame, text="Bin Coordinates")
binCoordinatesLabel.grid(row=4, column=0)
binCoordinatesInput = tk.Entry(inputFrame)
binCoordinatesInput.insert(END, "minimized.restart.coor")
binCoordinatesInput.grid(row=4, column=1)

# #binvelocities
binVelocitiesLabel = tk.Label(inputFrame, text="Bin Velocities")
binVelocitiesLabel.grid(row=5, column=0)
binVelocitiesInput = tk.Entry(inputFrame)
binVelocitiesInput.insert(END, "minimized.restart.vel")
binVelocitiesInput.grid(row=5, column=1)

# set temperature
temperatureLabel = tk.Label(inputFrame, text="Initial Temperature (K)")
temperatureLabel.grid(row=6, column=0)
temperatureInput = tk.Entry(inputFrame)
temperatureInput.insert(END, "310")
temperatureInput.grid(row=6, column=1)

# ----- output ----- #
outputFrame = tk.LabelFrame(frame, text="Output")
outputFrame.grid(row=0, column=1, padx=10, pady=10)

# set output & outputname
outputNameLabel = tk.Label(outputFrame, text="Output Name")
outputNameLabel.grid(row=0, column=0)
outputNameInput = tk.Entry(outputFrame)
outputNameInput.insert(END, "output")
outputNameInput.grid(row=0, column=1)

# dcdfile
dcdFileNameLabel = tk.Label(outputFrame, text="DCD File Name")
dcdFileNameLabel.grid(row=1, column=0)
dcdFileNameInput = tk.Entry(outputFrame)
dcdFileNameInput.insert(END, "${output}.dcd")
dcdFileNameInput.grid(row=1, column=1)

# xstFile
xstFileNameLabel = tk.Label(outputFrame, text="XST File Name")
xstFileNameLabel.grid(row=2, column=0)
xstFileNameInput = tk.Entry(outputFrame)
xstFileNameInput.insert(END, "${output}.xst")
xstFileNameInput.grid(row=2, column=1)

# dcdfreq
dcdFrequencyLabel = tk.Label(outputFrame, text="DCD Frequency (500=once per picosecond)")
dcdFrequencyLabel.grid(row=3, column=0)
dcdFrequencyInput = tk.Entry(outputFrame)
dcdFrequencyInput.insert(END, "50")
dcdFrequencyInput.grid(row=3, column=1)

# xstFreq
xstFrequencyLabel = tk.Label(outputFrame, text="XST Frequency (500=1/ps)")
xstFrequencyLabel.grid(row=4, column=0)
xstFrequencyInput = tk.Entry(outputFrame)
xstFrequencyInput.insert(END, "50")
xstFrequencyInput.grid(row=4, column=1)

# binaryoutput
binaryOutputLabel = tk.Label(outputFrame, text="Binary Output?")
binaryOutputLabel.grid(row=5, column=0)
binaryOutputInput = tk.StringVar(outputFrame)
binaryOutputInput.set("yes")
binaryOutputInputMenu = tk.OptionMenu(outputFrame, binaryOutputInput, *["yes", "no"])
binaryOutputInputMenu.grid(row=5, column=1)

# binaryrestart
binaryRestartLabel = tk.Label(outputFrame, text="Binary Restart?")
binaryRestartLabel.grid(row=6, column=0)
binaryRestartInput = tk.StringVar(outputFrame)
binaryRestartInput.set("yes")
binaryRestartInputMenu = tk.OptionMenu(outputFrame, binaryRestartInput, *["yes", "no"])
binaryRestartInputMenu.grid(row=6, column=1)

# outputEnergies
outputEnergyLabel = tk.Label(outputFrame, text="Output Energy Print Frequency (500=1/ps)")
outputEnergyLabel.grid(row=7, column=0)
outputEnergyInput = tk.Entry(outputFrame)
outputEnergyInput.insert(END, "50")
outputEnergyInput.grid(row=7, column=1)

# restartfreq
restartFrequencyLabel = tk.Label(outputFrame, text="Restart Frequency (500=1/ps)")
restartFrequencyLabel.grid(row=8, column=0)
restartFrequencyInput = tk.Entry(outputFrame)
restartFrequencyInput.insert(END, "50")
restartFrequencyInput.grid(row=8, column=1)

# ----- Basic dynamics ----- #
dynamicsFrame = tk.LabelFrame(frame, text="Basic Dynamics")
dynamicsFrame.grid(row=1, column=0)

# exclude
excludeLabel = tk.Label(dynamicsFrame, text="Charmm: Exclude")
excludeLabel.grid(row=0, column=0)
excludeInput = tk.Entry(dynamicsFrame)
excludeInput.insert(END, "scaled1-4")
excludeInput.grid(row=0, column=1)

# 1-4scaling
oneFourScalingLabel = tk.Label(dynamicsFrame, text="Charmm: 1-4 Scaling")
oneFourScalingLabel.grid(row=1, column=0)
oneFourScalingInput = tk.Entry(dynamicsFrame)
oneFourScalingInput.insert(END, "1")
oneFourScalingInput.grid(row=1, column=1)

# COMmotion
comMotionLabel = tk.Label(dynamicsFrame, text="COMmotion")
comMotionLabel.grid(row=2, column=0)
comMotionInput = tk.StringVar(dynamicsFrame)
comMotionInput.set("no")
comMotionInputMenu = tk.OptionMenu(dynamicsFrame, comMotionInput, *["yes", "no"])
comMotionInputMenu.grid(row=2, column=1)

# dielectric
dielectricLabel = tk.Label(dynamicsFrame, text="Dielectric")
dielectricLabel.grid(row=3, column=0)
dielectricInput = tk.Entry(dynamicsFrame)
dielectricInput.insert(END, "1.0")
dielectricInput.grid(row=3, column=1)

# ----- Simulation Space Partitioning ----- #
simSpaceFrame = tk.LabelFrame(frame, text="Simulation Space Partitioning")
simSpaceFrame.grid(row=1, column=1)

# switching
switchingLabel = tk.Label(simSpaceFrame, text="Switching")
switchingLabel.grid(row=0, column=0)
switchingInput = tk.StringVar(simSpaceFrame)
switchingInput.set("on")
switchingInputMenu = tk.OptionMenu(simSpaceFrame, switchingInput, *["on", "off"])
switchingInputMenu.grid(row=0, column=1)

# switchdist
switchingDistanceLabel = tk.Label(simSpaceFrame, text="Switching Distance")
switchingDistanceLabel.grid(row=1, column=0)
switchingDistanceInput = tk.Entry(simSpaceFrame)
switchingDistanceInput.insert(END, "9")
switchingDistanceInput.grid(row=1, column=1)

# cutoff
cutoffLabel = tk.Label(simSpaceFrame, text="Cutoff (10 w/PME else 12)")
cutoffLabel.grid(row=2, column=0)
cutoffInput = tk.Entry(simSpaceFrame)
cutoffInput.insert(END, "10")
cutoffInput.grid(row=2, column=1)

# pairlistdist
pairlistDistanceLabel = tk.Label(simSpaceFrame, text="Pairlist Distance")
pairlistDistanceLabel.grid(row=3, column=0)
pairlistDistanceInput = tk.Entry(simSpaceFrame)
pairlistDistanceInput.insert(END, "11")
pairlistDistanceInput.grid(row=3, column=1)

# ----- Multiple Timestepping ----- #
timestepFrame = tk.LabelFrame(frame, text="Multiple Timestepping")
timestepFrame.grid(row=2, column=0)

# firsttimestep
firstTimestepLabel = tk.Label(timestepFrame, text="First Timestep")
firstTimestepLabel.grid(row=0, column=0)
firstTimestepInput = tk.Entry(timestepFrame)
firstTimestepInput.insert(END, "0")
firstTimestepInput.grid(row=0, column=1)

# timestep
timestepLabel = tk.Label(timestepFrame, text="Timestep (0 < timestep < 4)")
timestepLabel.grid(row=1, column=0)
timestepInput = tk.Entry(timestepFrame)
timestepInput.insert(END, "2.0")
timestepInput.grid(row=1, column=1)

# stepspercycle
stepsPerCycleLabel = tk.Label(timestepFrame, text="Steps Per Cycle")
stepsPerCycleLabel.grid(row=2, column=0)
stepsPerCycleInput = tk.Entry(timestepFrame)
stepsPerCycleInput.insert(END, "1")
stepsPerCycleInput.grid(row=2, column=1)

# ----- Langevin Dynamics ----- #
langevinFrame = tk.LabelFrame(frame, text="Langevin Dynamics")
langevinFrame.grid(row=3, column=0)

# langevin
langevinLabel = tk.Label(langevinFrame, text="Enabled")
langevinLabel.grid(row=0, column=0)
langevinInput = tk.StringVar(langevinFrame)
langevinInput.set("on")
langevinInputMenu = tk.OptionMenu(langevinFrame, langevinInput, *["on", "off"])
langevinInputMenu.grid(row=0, column=1)

# langevinDamping
langevinDampingLabel = tk.Label(langevinFrame, text="Damping Coefficient (x/ps)")
langevinDampingLabel.grid(row=1, column=0)
langevinDampingInput = tk.Entry(langevinFrame)
langevinDampingInput.insert(END, "1")
langevinDampingInput.grid(row=1, column=1)

# langevinTemp
langevinTempLabel = tk.Label(langevinFrame, text="Bath Temperature (leave as is)")
langevinTempLabel.grid(row=2, column=0)
langevinTempInput = tk.Entry(langevinFrame)
langevinTempInput.insert(END, "$temperature")
langevinTempInput.grid(row=2, column=1)

# ----- Periodic Simulation ----- #
periodicSimFrame = tk.LabelFrame(frame, text="Periodic Simulation")
periodicSimFrame.grid(row=2, column=1)

# PME
pmeLabel = tk.Label(periodicSimFrame, text="PME")
pmeLabel.grid(row=0, column=0)
pmeInput = tk.StringVar(periodicSimFrame)
pmeInput.set("on")
pmeInputMenu = tk.OptionMenu(periodicSimFrame, pmeInput, *["on", "off"])
pmeInputMenu.grid(row=0, column=1)

# useGroupPressure
groupPressureLabel = tk.Label(periodicSimFrame, text="Use Group Pressure?")
groupPressureLabel.grid(row=1, column=0)
groupPressureInput = tk.StringVar(periodicSimFrame)
groupPressureInput.set("yes")
groupPressureInputMenu = tk.OptionMenu(periodicSimFrame, groupPressureInput, *["yes", "no"])
groupPressureInputMenu.grid(row=1, column=1)

# LangevinPiston
langevinPistonLabel = tk.Label(periodicSimFrame, text="Langevin Piston")
langevinPistonLabel.grid(row=2, column=0)
langevinPistonInput = tk.StringVar(periodicSimFrame)
langevinPistonInput.set("on")
langevinPistonInputMenu = tk.OptionMenu(periodicSimFrame, langevinPistonInput, *["on", "off"])
langevinPistonInputMenu.grid(row=2, column=1)

# LangevinPistonTarget
targetPressureLabel = tk.Label(periodicSimFrame, text="Piston Target Pressure (bars)")
targetPressureLabel.grid(row=3, column=0)
targetPressureInput = tk.Entry(periodicSimFrame)
targetPressureInput.insert(END, "1.02")
targetPressureInput.grid(row=3, column=1)

# LangevinPistonPeriod
pistonPeriodLabel = tk.Label(periodicSimFrame, text="Piston Oscillation Period (fs)")
pistonPeriodLabel.grid(row=4, column=0)
pistonPeriodInput = tk.Entry(periodicSimFrame)
pistonPeriodInput.insert(END, "150")
pistonPeriodInput.grid(row=4, column=1)

# LangevinPistonDecay
pistonDecayLabel = tk.Label(periodicSimFrame, text="Piston Decay Time (fs)")
pistonDecayLabel.grid(row=5, column=0)
pistonDecayInput = tk.Entry(periodicSimFrame)
pistonDecayInput.insert(END, "90")
pistonDecayInput.grid(row=5, column=1)

# LangevinPistonTemp
pistonTempLabel = tk.Label(periodicSimFrame, text="Piston Temperature (usually leave as is)")
pistonTempLabel.grid(row=6, column=0)
pistonTempInput = tk.Entry(periodicSimFrame)
pistonTempInput.insert(END, "$temperature")
pistonTempInput.grid(row=6, column=1)

# ----- Periodic Boundary Conditions ----- #
boundaryFrame = tk.LabelFrame(frame, text="Periodic Boundary Conditions")
boundaryFrame.grid(row=3, column=1)

# wrapWater
wrapWaterLabel = tk.Label(boundaryFrame, text="Wrap Water to Central Cell")
wrapWaterLabel.grid(row=0, column=0)
wrapWaterInput = tk.StringVar(boundaryFrame)
wrapWaterInput.set("on")
wrapWaterInputMenu = tk.OptionMenu(boundaryFrame, wrapWaterInput, *["on", "off"])
wrapWaterInputMenu.grid(row=0, column=1)

# wrapAll
wrapAllLabel = tk.Label(boundaryFrame, text="Wrap Other Molecules")
wrapAllLabel.grid(row=1, column=0)
wrapAllInput = tk.StringVar(boundaryFrame)
wrapAllInput.set("on")
wrapAllInputMenu = tk.OptionMenu(boundaryFrame, wrapAllInput, *["on", "off"])
wrapAllInputMenu.grid(row=1, column=1)

# wrapAll
wrapNearestLabel = tk.Label(boundaryFrame, text="Wrap Nearest (use for non-rectangular cells)")
wrapNearestLabel.grid(row=2, column=0)
wrapNearestInput = tk.StringVar(boundaryFrame)
wrapNearestInput.set("off")
wrapNearestInputMenu = tk.OptionMenu(boundaryFrame, wrapNearestInput, *["on", "off"])
wrapNearestInputMenu.grid(row=2, column=1)

# ----- Scripting ----- #
scriptingFrame = tk.LabelFrame(frame, text="Scripting")
scriptingFrame.grid(row=4, column=0)

# minimize
minimizeLabel = tk.Label(scriptingFrame, text="Lower Potential Energy for x Steps")
minimizeLabel.grid(row=0, column=0)
minimizeInput = tk.Entry(scriptingFrame)
minimizeInput.insert(END, "1000")
minimizeInput.grid(row=0, column=1)

# reinitvels
reinitVelsLabel = tk.Label(scriptingFrame, text="Reinit Velocities (leave as is)")
reinitVelsLabel.grid(row=1, column=0)
reinitVelsInput = tk.Entry(scriptingFrame)
reinitVelsInput.insert(END, "$temperature")
reinitVelsInput.grid(row=1, column=1)

# run
runStepsLabel = tk.Label(scriptingFrame, text="Number of Steps to Run")
runStepsLabel.grid(row=2, column=0)
runStepsInput = tk.Entry(scriptingFrame)
runStepsInput.insert(END, "50000")
runStepsInput.grid(row=2, column=1)

# ----- Generate Button ----- #
generateConfigButton = tk.Button(frame, text="Generate", command=generateConfig)
generateConfigButton.grid(row=4, column=1)

window.mainloop()
