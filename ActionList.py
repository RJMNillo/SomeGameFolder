# Action List

class Action():
    def __init__(self, AName, ACooldown = 0):  
        self.name = AName
        self.cooldown = ACooldown

    def DoAction(self):
        pass

# Actions List
class BasicAttack(Action):
    def __init__(self, AName, BAUser, BATarget):
        Action.__init__(self, AName)
        self.User = BAUser
        self.Target = BATarget
    
    def DoAction(self):
        DamageDealt = self.User.ATK - self.Target.DEF
        self.Target.HP = self.Target.HP - DamageDealt
        # All Actions will reset the Interval to 0
        self.User.Interval = 0
