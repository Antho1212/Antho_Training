"""This module implements basic gaming operations.  These
functions should be used to create higher level operations.
In particular, they should NOT be directly used by players."""


import os, pickle, random
    


# === database management (do not use outside of API) ===
def _load_game_db() -> dict:
    """Loads the game database.
    
    Returns
    -------
    game_db: contains all game information (dict)
    
    Notes
    -----
    If no database exists, an empty one is automatically created.
    
    """
    
    try:
        fd = open('game.db', 'rb')
        game_db = pickle.load(fd)
        fd.close()
    except:
        game_db =  {'creatures':{}, 'players':{}}

    return game_db


def _dump_game_db(game_db: dict) -> None:
    """Dumps the game database.
    
    Parameters
    -------
    game_db: contains all game information (dict)
    
    """
    
    fd = open('game.db', 'wb')
    pickle.dump(game_db, fd)
    fd.close()



# === player management functions ===
def player_exists(player: str) -> bool:
    """Tells whether a player already exists or not.
    
    Parameters
    ----------
    player: player name (str)
    
    Returns
    -------
    result: True if player already exists, False otherwise (bool)
    
    """
    
    game_db = _load_game_db()
    
    return player in game_db['players']
    
    
def add_new_player(player: str) -> None:
    """Adds a new player to the game.
        
    Parameters
    ----------
    player: player name (str)
    
    Raises
    ------
    ValueError: if there already is a player with the same name
    
    Notes
    -----
    A new player has zero money and no creature.
    
    """
    
    game_db = _load_game_db()
    
    if player_exists(player):
        raise ValueError('player %s already exists' % player)

    game_db['players'][player] = {'money':0, 'creature':None}
    
    _dump_game_db(game_db)


def set_player_money(player: str, money: int) -> None:
    """Sets the amount of money of a player.
        
    Parameters
    ----------
    player: player name (str)
    money: amount of money (int)
    
    Raises
    ------
    ValueError: if the player does not exist
    ValueError: if money is strictly negative
    
    """
    
    game_db = _load_game_db()
    
    if not player_exists(player):
        raise ValueError('player %s does not exists' % player)
    if money < 0:
        raise ValueError('money cannot be negative (money = %d)' % money)
    
    game_db['players'][player]['money'] = money
    
    _dump_game_db(game_db)


def get_player_money(player: str) -> int:
    """Returns the amount of money of a player.
        
    Parameters
    ----------
    player: player name (str)
    
    Returns
    -------
    money: amount of money (int)
    
    Raises
    ------
    ValueError: if the player does not exist
    
    """
    
    game_db = _load_game_db()
    
    if not player_exists(player):
        raise ValueError('player %s does not exists' % player)
    
    return game_db['players'][player]['money']


def has_creature(player: str) -> bool:
    """Tells whether the player has a creature or not.
    
    Parameters
    -------
    player: player name (str)
    
    Returns
    -------
    result: True if the player has creature, False otherwise (bool)
    
    Raises
    ------
    ValueError: if the player does not exist
    
    """
    
    game_db = _load_game_db()
    
    if not player_exists(player):
        raise ValueError('player %s does not exists' % player)
    
    return game_db['players'][player]['creature'] != None


# === creature management functions ===
def creature_exists(creature: str) -> bool:
    """Tells whether a creature already exists or not.
    
    Parameters
    ----------
    creature: creature name (str)
    
    Returns
    -------
    result: True if creature already exists, False otherwise (bool)
    
    """
    
    game_db = _load_game_db()
    
    return creature in game_db['creatures']


def get_player(creature: str) -> str:
    """Returns the name of player who owns the creature.
    
    Parameters
    ----------
    creature: creature name (str)
    
    Returns
    -------
    player: player name (str)
    
    Raises
    ------
    ValueError: if the creature does not exist
    
    """
    
    game_db = _load_game_db()
    
    if not creature_exists(creature):
        raise ValueError('creature %s does not exists' % creature)
    
    return game_db['creatures'][creature]['player']
    
    
    
def set_creature(player: str, creature: str, variety: str, strength: int, life: int) -> None:
    """Sets the creature of a player.
    
    Parameters
    -------
    player: player name (str)
    creature: creature name (str)
    variety: creature variety (str)
    strength: creature strength (int)
    life: creature life (int)
    
    Raises
    ------
    ValueError: if the player does not exist
    ValueError: if the player already has a creature
    ValueError: if the creature is already owned by another player
    ValueError: if variety is neither 'water', 'fire' nor 'plant'
    ValueError: if strength is strictly negative
    ValueError: if life is strictly negative

    """
    
    game_db = _load_game_db()
    
    if not player_exists(player):
        raise ValueError('player %s does not exists' % player)
    if has_creature(player):
        raise ValueError('player %s already has a creature' % player)
    if variety not in ('water', 'fire', 'plant'):
        raise ValueError('variety %s is not valid' % variety)
    if strength < 0:
        raise ValueError('strength cannot be negative (strength = %d)' % strength)
    if life < 0:
        raise ValueError('life cannot be negative (life = %d)' % life)
    
    game_db['players'][player]['creature'] = creature
    game_db['creatures'][creature] = {'variety':variety, 'strength':strength, 'life':life, 'player':player}
    
    _dump_game_db(game_db)


def remove_creature(creature: str) -> None:
    """Removes a creature from the game.
    
    Parameters
    -------
    creature: creature name (str)
    
    Raises
    ------
    ValueError: if the creature does not exist
    
    Notes
    -----
    After its removal, the creature cannot be used anymore and is "lost".

    """
    
    game_db = _load_game_db()
    
    if not creature_exists(creature):
        raise ValueError('creature %s does not exists' % creature)
    
    player = game_db['creatures'][creature]['player']
    game_db['players'][player]['creature'] = None
    del game_db['creatures'][creature]
    
    _dump_game_db(game_db)


def get_random_creature_name() -> str:
    """Returns a random, unique creature name.
    
    Returns
    -------
    creature: random, unique creature name (str)
    
    """

    game_db = _load_game_db()
    
    is_unique = False
    while not is_unique:
        prefix = ('Lieju', 'Raiden', 'Rinnees')[random.randint(0, 2)]
        suffix = str(random.randint(100, 999))
        creature = prefix + '#' + suffix
        
        is_unique = not creature_exists(creature)
    
    return creature


def get_random_creature_variety() -> str:
    """Returns a random creature variety.
    
    Returns
    -------
    variety: random, unique creature variety (str)

    Notes
    -----
    variety can be either 'water', 'fire' or 'plant'.
    
    """

    return ('water', 'fire', 'plant')[random.randint(0, 2)]
    

def get_creature_variety(creature: str) -> str:
    """Returns the variety of a creature.
        
    Parameters
    ----------
    creature: creature name (str)
    
    Returns
    -------
    variety: creature variety (str)
    
    Raises
    ------
    ValueError: if the creature does not exist
    
    """
    
    game_db = _load_game_db()
    
    if not creature_exists(creature):
        raise ValueError('creature %s does not exist' % creature)
    
    return game_db['creatures'][creature]['variety'] 


def set_creature_strength(creature: str, strength: int) -> None:
    """Modifies the strengthof a creature.
        
    Parameters
    ----------
    creature: creature name (str)
    strength: creature strength (int)
    
    Raises
    ------
    ValueError: if the creature does not exist
    ValueError: if strength is strictly negative
     
    """
    
    game_db = _load_game_db()
    
    if not creature_exists(creature):
        raise ValueError('creature %s does not exist' % creature)
    if strength < 0:
        raise ValueError('strength cannot be negative (strength = %d)' % strength)
    
    game_db['creatures'][creature]['strength']  = strength
    
    _dump_game_db(game_db)
    
    
def get_creature_strength(creature: str) -> int:
    """Returns the strengthof a creature.
        
    Parameters
    ----------
    creature: creature name (str)
    
    Returns
    -------
    strength: creature strength (int)
    
    Raises
    ------
    ValueError: if the creature does not exist
    
    """
    
    game_db = _load_game_db()
    
    if not creature_exists(creature):
        raise ValueError('creature %s does not exist' % creature)
    
    return game_db['creatures'][creature]['strength'] 
    
    
def set_creature_life(creature: str, life: int) -> None:
    """Modifies the lifeof a creature.
        
    Parameters
    ----------
    creature: creature name (str)
    life: creature life (int)
        
    Raises
    ------
    ValueError: if the creature does not exist
    ValueError: if life is strictly negative
     
    """
    
    game_db = _load_game_db()
    
    if not creature_exists(creature):
        raise ValueError('creature %s does not exist' % creature)
    if life < 0:
        raise ValueError('life cannot be negative (life = %d)' % life)
    
    game_db['creatures'][creature]['life']  = life
    
    _dump_game_db(game_db)

        
def get_creature_life(creature: str) -> int:
    """Returns the lifeof a creature.
        
    Parameters
    ----------
    creature: creature name (str)
    
    Returns
    -------
    life: creature life (int)
    
    Raises
    ------
    ValueError: if the creature does not exist
    
    """
    
    game_db = _load_game_db()
    
    if not creature_exists(creature):
        raise ValueError('creature %s does not exist' % creature)
    
    return game_db['creatures'][creature]['life'] 
    

def reset_game() -> None:
    """Remove all players and creatures."""
    
    if os.path.exists('game.db'):
        os.remove('game.db')
