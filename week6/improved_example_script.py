# function for reading xyz file
def read_xyz_file(filepath):
    """
    A function that reads a filepath and returns a 
    suitable representation of a molecule.

    Parameteres
    -----------
        filepath : str
            A valid filepath in the system
    """
    molecule = None
    with open('example.xyz') as file:
        lines = []
    for line in file:
        lines.append(line)
    # makes sure we only get number
    n_atoms = int(lines[0].strip()) 
    # getting atoms in molecule
    atoms = lines[2:2+n_atoms]

    return molecule

# example of atom representation
# atom1 = ('C', (0.0,0.0,0.0))

def subtraction(point0,point1):
    """
    It takes in two points and returns the element 
    wise subtraction of its coordiantes.

    Args:
        point0 (tuple): a tuple of length 3 where the positions
                        correspond respectively to x,y,z
        point1 (tuple): a tuple of length 3 where the positions
                        correspond respectively to x,y,z

    Returns:
        output (tuple): the addition of the who points 
                        element wise
    """
    pass

def element_wise_power(value,point):
    return point**value

def get_distance(point0,point1):
    
    x0 = float(point0[1])
    y0 = float(point0[2])
    z0 = float(point0[3])
    x1 = float(point1[1])
    y1 = float(point1[2])
    z1 = float(point1[3])

    difference_vector = subtraction(point0,point1)
    difference_vector = element_wise_power(2.0,difference_vector)
    distance = element_wise_power(0.5,difference_vector)

    return distance

# this is the section that defines the main part of the code
# can look at functions if confused
if __name__ == '__main__':

    ifile = 'example.xyz'
    atom0_idx = 3
    atom1_idx = 4
    # atom1 = ('C',(0.0,0.0,0.0))
    # molecule = a list of atoms

    molecule = read_xyz_file(ifile)

    # getting indices of desired atoms
    atom0 = molecule[atom0_idx - 1].strip().split()
    atom1 = molecule[atom1_idx - 1].strip().split()

    distance = get_distance(atom0[1],atom1[1])

    print(f'distance = {distance}')
