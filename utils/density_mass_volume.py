def calculate_density(mass, volume):
    """
    Calculate density given mass and volume.
    
    Args:
        mass (float): The mass of the object.
        volume (float): The volume of the object.
    
    Returns:
        float: The density of the object.
    """
    if volume == 0:
        raise ValueError("Volume cannot be zero")
    return mass / volume


def calculate_mass(density, volume):
    """
    Calculate mass given density and volume.
    
    Args:
        density (float): The density of the object.
        volume (float): The volume of the object.
    
    Returns:
        float: The mass of the object.
    """
    if density == 0 and volume == 0:
        raise ValueError("Both density and volume cannot be zero")
    return density * volume


def calculate_volume(mass, density):
    """
    Calculate volume given mass and density.
    
    Args:
        mass (float): The mass of the object.
        density (float): The density of the object.
    
    Returns:
        float: The volume of the object.
    """
    if density == 0:
        raise ValueError("Density cannot be zero")
    return mass / density