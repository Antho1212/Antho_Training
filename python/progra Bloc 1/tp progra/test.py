def get_random_creature_variety(creature :str) -> str: 
    """Returns a random creature variety.
    Returns 
    --------
    
    variety : random, unique creature variety (str)
    
    Notes 
    ------
    
    variety can be either "water", "fire" or "plant". """
    creature = ("water", "fire", "plant")
    return get_random_creature_variety(creature)


print(get_random_creature_variety(alof))
