# Reggie Jan Marc Nillo
# Game Idea No. 1

# RPG
# Might follow the classic Megami Tensei Route
import ActionList
import random

class unit():
    def __init__(self, UName, ULevel, UBHP, UBATK, UBSPD, UBDEF, UGHP, UGATK, UGSPD, UGDEF):
        self.Name = UName
        self.Level = ULevel
        self.BHP = UBHP
        self.BATK = UBATK
        self.BSPD = UBSPD
        self.BDEF = UBDEF
        self.GHP = UGHP
        self.GATK = UGATK
        self.GSPD = UGSPD
        self.GDEF = UGDEF
# End of class unit

class ActiveUnit(unit):
    def __init__(self, UName, ULevel, UBHP, UBATK, UBSPD, UBDEF, UGHP, UGATK, UGSPD, UGDEF):
        # Inheriting the unit class
        unit.__init__(self, UName, ULevel, UBHP, UBATK, UBSPD, UBDEF, UGHP, UGATK, UGSPD, UGDEF)
        # Unit's stats
        self.HP = int((round((self.Level - 1) * self.GHP,0) + self.BHP) * 10)
        self.ATK = int((round((self.Level - 1) * self.GATK,0) + self.BATK) * 5)
        self.SPD = int((round((self.Level - 1) * self.GSPD,0) + self.BSPD) * 5)
        self.DEF = int((round((self.Level - 1) * self.GDEF,0) + self.BDEF) * 5)
        # Unit's Sets
        self.skillList = []
        self.addSkill(ActionList.Basic_Attack)
        # Unit's Interval
        self.Interval = 0

    # Prints the Unit's Stats
    def printStats(self):
        print(f"Unit Analysis for {self.Name}")
        print(f"Level: {self.Level}")
        print(f"HP: {self.HP}")
        print(f"ATK: {self.ATK}")
        print(f"SPD: {self.SPD}")
        print(f"DEF: {self.DEF}")
        print("------------------------------------")

    def addSkill(self,skill):
        self.skillList.append(skill)
    
    # Find Skill
    def FindSkill(self):
        ASkill = random.choice(self.skillList)
        while ASkill.cooldown > 0:
            ASkill = random.choice(self.skillList)
        print(f"{self.Name} is going to use {ASkill.name}!")
        return ASkill
    
    # Find Targets
    def FindTargets(self, Skill, OtherTeam):
        Targets = []
        MinDef = 999999
        PrevMinDef = -999999
        RemTargets = 0
        if Skill.targets == 0: # 0 Means that the Skill will target everyone
            return OtherTeam
        else:
            while RemTargets < Skill.targets:
                TargetTeammate = None
                for someunit in OtherTeam:
                    if someunit.DEF > PrevMinDef and someunit.DEF < MinDef and someunit.HP > 0:
                        TargetTeammate = someunit
                Targets.append(TargetTeammate)
                MinDef = 999999
                RemTargets += 1
            TargetNames = []
            for someunit in Targets:
                TargetNames.append(someunit.Name)
            print(TargetNames)
            return Targets
    
    # Attack!
    def DoAction(self, Skill, KnownTargets):
        AttackPower = self.ATK * Skill.ATKMultiplier
        for someunit in KnownTargets:
            DamageDealt = 0
            # Calculate damage: AttackPower - defense
            DamageDealt = AttackPower - someunit.DEF
            if DamageDealt < 0:
                DamageDealt = 0 # What if an attack was so weak it heals?
            # Put that damage dealt into HP
            someunit.HP = someunit.HP - DamageDealt
            if someunit.HP <= 0:
                someunit.HP = 0
                print(f"{someunit.Name} has been KO'd!")
        # Then finally 0 out the interval
        self.Interval = 0
# End of class ActiveUnit
