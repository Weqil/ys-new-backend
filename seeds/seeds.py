
def setAllSeeds():
    from .adminSeed import setStartAdmins
    print('seeds start')
    setStartAdmins()
    print('seeds complete')
    return True
