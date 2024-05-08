import tkinter as tk

window = tk.Tk()
window.title('NAMD Config Generator')

frame = tk.Frame(window)
frame.pack()

END = -1

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

# ----- output ----- #
outputFrame = tk.LabelFrame(frame, text="Output")
outputFrame.grid(row=0, column=1)

# set output & outputname
outputNameLabel = tk.Label(outputFrame, text="Output Name")
outputNameLabel.grid(row=0, column=0)
outputNameLabelInput = tk.Entry(outputFrame)
outputNameLabelInput.insert(END, "output")
outputNameLabelInput.grid(row=0, column=1)

# dcdfile
dcdFileNameLabel = tk.Label(outputFrame, text="DCD File Name")
dcdFileNameLabel.grid(row=1, column=0)
dcdFileNameInput = tk.Entry(outputFrame)
dcdFileNameInput.insert(END, "${output}.dcd")
dcdFileNameInput.grid(row=1, column=1)

# xstFile
dcdFileNameLabel = tk.Label(outputFrame, text="XST File Name")
dcdFileNameLabel.grid(row=2, column=0)
dcdFileNameInput = tk.Entry(outputFrame)
dcdFileNameInput.insert(END, "${output}.xst")
dcdFileNameInput.grid(row=2, column=1)

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

# ----- Temperature Control ----- #
temperatureFrame = tk.LabelFrame(frame, text="Temperature Control")
temperatureFrame.grid(row=2, column=1)

# set temperature
temperatureLabel = tk.Label(temperatureFrame, text="Initial Temperature (K)")
temperatureLabel.grid(row=0, column=0)
temperatureInput = tk.Entry(temperatureFrame)
temperatureInput.insert(END, "310")
temperatureInput.grid(row=0, column=0)

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
langevinDampingInput = tk.Entry(timestepFrame)
langevinDampingInput.insert(END, "1")
langevinDampingInput.grid(row=1, column=1)

# langevinTemp
langevinTempLabel = tk.Label(langevinFrame, text="Bath Temperature (leave as is)")
langevinTempLabel.grid(row=2, column=0)
langevinTempInput = tk.Entry(timestepFrame)
langevinTempInput.insert(END, "$temperature")
langevinTempInput.grid(row=2, column=1)

window.mainloop()