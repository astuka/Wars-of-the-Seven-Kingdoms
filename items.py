#ITEMS - crystalized teardrop, oil flask


class Item:
    def __init__(self,name, type, price):
        self.name = name
        self.type = type
        self.price = price

#CRAFTING
tempered_bone = Item("Tempered Bone", "crafting", 5)
essence_powder = Item("Essence Powder", "crafting", 5)
cocoon = Item("Cocoon", "crafting", 5)
winter_shard = Item("Winter Shard", "crafting", 5)
magical_clay = Item("Magical Clay", "crafting", 5)
fire_stone = Item("Fire Stone", "crafting", 5)
volanic_ash = Item("Volcanic Ash", "crafting", 5)
silver_feather = Item("Silver Feather", "crafting", 5)
sun_stone = Item("Sun Stone", "crafting", 5)

#BUFF
stardust = Item("Stardust", "buff", 5)
beast_pellet = Item("Beast Pellet", "buff", 5)
antiseptic = Item("Antiseptic", "buff", 5)
bandage = Item("Bandage", "buff", 5)
laudanum = Item("Laudanum", "buff", 5)
caffeine_pill = Item("Caffeine Pill", "buff", 5)

#ARTIFACT
fatetaker = Item("Fatetaker", "artifact", 5)
kivas_heart = Item("Kiva's Heart", "artifact", 5)
kingslayer = Item("Kingslayer", "artifact", 5)
dining_menagerie = Item("Chef Oscar's Royal Dining Menagerie", "artifact", 5)
dragensmoor = Item("Dragensmoor", "artifact", 5)
hrothgars_fury = Item("Hrothgar's Fury", "artifact", 5)
great_equalizer = Item("The Great Equalizer", "artifact", 5)
shadaloo_silk = Item("Shadaloo Silk", "artifact", 5)
codex_aten_nu = Item("Codex of Aten Nu", "artifact", 5)
dawn_dusk = Item("Dawn & Dusk", "artifact", 5)
heartbreaker = Item("Heartbreaker", "artifact", 5)
lifeweaver = Item("Lifeweaver", "artifact", 5)
mjolnir = Item("Mjolnir", "artifact", 5)
spellbinder = Item("Spellbinder", "artifact", 5)
masamune = Item("Masamune", "artifact", 5)

obtainable_artifacts = [fatetaker, kivas_heart,kingslayer, dining_menagerie,dragensmoor,hrothgars_fury,great_equalizer,shadaloo_silk,codex_aten_nu,dawn_dusk,heartbreaker,lifeweaver,mjolnir,spellbinder,masamune]

#weapon - "Molotov"
#weapon types - staff, pan, lance and shield, hammer, tome, lance, battleaxe, shortsword, circlets, scythe, bow, daggers, lute, katana, pistol, sword and shield, hammer and shield
class Item:
    def __init__(self,name, type, offense, defense, price):
        self.name = name
        self.type = type
        self.offense = offense
        self.defense = defense 
        self.price = price


#equipment types - chainmail, plate armor

