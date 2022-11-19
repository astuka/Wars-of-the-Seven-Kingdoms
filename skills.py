#SKILLS - Paralyze, Rune Missile, Lich Raise, Fire Nuke
skills = ["Chaos Strike", "Glory of Valoskyr", "Bloodlust", "War Cry", "Heavy Hitter", "Rampage", "Aetherburst", "Thundercracker", "Frostfall", "Firestorm", "Hollow Point", "Wildly Armed", "Rapid Fire", "Reload", "Plaguing Doom", "Scarlet Grace", "Beast Communion", "Plague", "Devil's Kiss", "Deathly Gaze", "Razor's Edge", "Viral Influx", "Umbral Shock", "Divine Sacrifice", "Knight's Honor", "Know Thyself", "Planet Cracker", "Ash and Gunpowder", "Fortify", "Artillery Barrage", "Bushido", "1000 Cuts", "Bloody Slice", "Harakiri", "Evade", "Death on High", "Dragon Communion", "Charge", "Dragon Dive", "God's Chosen", "Divine Strike", "Holy Wrath", "Hammer Throw", "Umbral Collapse", "Astral Lift", "Aethersurge", "Family Feast", "Mise en Scene", "Order Up!", "High Heat", "Carve", "Orchestra", "Chord of Death", "Shanty", "Lullaby", "Dance of All Seasons", "Waltz", "Samba", "Two-Step", "Charm", "Blessing of God", "Holy Writ", "Cleansing Spirit", "Healing Chime", "Holy", "Pool of Radiance", "Deal Breaker", "Infinite Light", "Manta", "Thrash Disposal", "Golden Earth", "Jamais Vu", "Bash", "Catastrophe", "Hades Blast", "Acrobat Kick", "Debilitate"]

class Skill:
    def __init__(self,name, stat, req, type): #required stat (strength, charisma, etc) and then type (combat, other)
        self.name = name
        self.stat = stat
        self.req = req
        self.type = type


