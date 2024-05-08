# Original Script in TCL by L. Martinez, Feb 26, 2008. (leandromartinez98@gmail.com)
# Converted to Python by Anna Bontempo, May 8, 2024.

print("-------------------------------------------------------")
print(" Gets maximum and minimum coordinates from a PDB file. ")
print(" The selection will be defined below: ")
print(" Use 'all' to consider all atoms in each field. ")
print("-------------------------------------------------------")

pdbfile = input(" PDB file: ").strip()
segment = input(" Segment: ").strip()
residue = input(" Residue type: ").strip()
atomtype = input(" Atom type: ").strip()
firstatom = input(" Atom index greater than: ").strip()
lastatom = input(" Atom index less than: ").strip()

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
        consider = True
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
        if consider:
            x = float(line[30:38].strip())
            y = float(line[38:46].strip())
            z = float(line[46:54].strip())
            xmin = min(xmin, x)
            ymin = min(ymin, y)
            zmin = min(zmin, z)
            xmax = max(xmax, x)
            ymax = max(ymax, y)
            zmax = max(zmax, z)

print("-------------------------------------------------------")
print(" Minimum and maximum coordinates of selected atoms: ")
print(f" X_min = {xmin:.3f}     X_max = {xmax:.3f}")
print(f" Y_min = {ymin:.3f}     Y_max = {ymax:.3f}")
print(f" Z_min = {zmin:.3f}     Z_max = {zmax:.3f}")
print("-------------------------------------------------------")
print(" Length in each direction: ")
print(f" x: {xmax - xmin:.3f}")
print(f" y: {ymax - ymin:.3f}")
print(f" z: {zmax - zmin:.3f}")
print("-------------------------------------------------------")
print(" Cell centre: ")
print(f" X= {(xmax + xmin) / 2:.3f}")
print(f" Y= {(ymax + ymin) / 2:.3f}")
print(f" Z= {(zmax + zmin) / 2:.3f}")
print("-------------------------------------------------------")
print(" Copy/paste for NAMD: ")
print(f"cellBasisVector1 {xmax - xmin:.3f} 0 0")
print(f"cellBasisVector2 0 {ymax - ymin:.3f} 0")
print(f"cellBasisVector3 0 0 {zmax - zmin:.3f}")
print(f"cellOrigin {(xmax + xmin) / 2:.3f} {(ymax + ymin) / 2:.3f} {(zmax + zmin) / 2:.3f}")
print("-------------------------------------------------------")

