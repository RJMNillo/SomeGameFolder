# Action List
class Action():
    def __init__(self, AName, NumTargets, multiplier, Cooldown = 0):  
        self.name = AName
        self.Maxcooldown = Cooldown
        self.cooldown = Cooldown
        self.targets = NumTargets
        self.ATKMultiplier = multiplier

# Action List
# A Basic Attack that everyone inherits
Basic_Attack = Action("Basic Attack", 1, 1)

# Strong Recovery of one person
Strong_Recover = Action("Strong Recovery", 1, 2, 5)

# Team-Wide attacks
# They have NumTarget values of 0.
Burn_Wave = Action("Burn Wave", 0, 3, 7)
