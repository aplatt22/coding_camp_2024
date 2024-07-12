# read the file
with open('example.xyz') as file:
    lines = []
    for line in file:
        lines.append(line)

# makes sure we only get number
n_atoms = int(lines[0].strip()) 
# getting atoms in molecule
atoms = lines[2:2+n_atoms]

# getting indices of desired atoms
atom3 = atoms[2].strip().split() # make tuple of coordinates for atom 3
atom4 = atoms[3].strip().split() # make tuple of coodrinates for atom 4

# getting atom 3 coordinates separated
x3 = float(atom3[1])
y3 = float(atom3[2])
z3 = float(atom3[3])
# getting atom 4 coordinates separated
x4 = float(atom4[1])
y4 = float(atom4[2])
z4 = float(atom4[3])

# setting distance variable
distance = ((x3-x4)**2 + (y3-y4)**2 + (z3-z4)**2)**(1/2)

print(f'distance = {distance}')
