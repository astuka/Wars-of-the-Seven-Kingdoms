import random as r 

cultures = ["Asvogod", "Wuxia", "San Soba", "Aten Nu", "Legalia", "Venata", "Amoranth"]

#NAMES- Silmaris, Krog, Zubar, Shandaran, Vashar, Arilo, Matilda, Lyra, Thalion, Domovir, Kirt, Malkor, Kirk, Caun, Kah'Pa, Tietra, Wiegrath, Jenkins, Jonathan, Reynfred
#no changes needed for names, add as many as u want :)
asvogod_female_name = ["Therazina", "Fiona", "Tamara", "Gail", "Freya", "Lydia", "Anya", "Faye", "Gertrude"]
asvogod_male_name = ["Gustav", "Falder", "Brangeth", "Drago", "Geld", "Terag", "Rolf", "Nasgoli", "Odin", "Ragnox", "Skyur", "Korgan", "Lenar", "Zalbrag", "Farnus", "Thordal"]

wuxia_female_name = ["Totori", "Minhsa", "Kesmati", "Aran"]
wuxia_male_name = ["Tenyo", "Hong Lu", "Sentana", "Sedo", "Shinyo", "Kenshi"]

sansoba_female_name = ["Atma", "Ishala", "Jasmina", "Zala", "Bastille", "Aiela", "Aria", "Xena", "Iola"]
sansoba_male_name = ["Alando", "Saleh", "Hammurabi", "Shabab", "Jashar", "Shobach", "Osyris"]

atennu_female_name = ["Juniper", "Sena", "Tigerlily", "Hyacinth", "Elm"]
atennu_male_name = ["Lacroix", "Indoril", "Orwell", "Haudlin", "Ephraim", "Sion", "Cronus", "Ra", "Eamon", "Malathir", "Erasmus", "Eagan", "Morpheus"]

legalia_female_name = ["Pandora", "Pyre", "Indoline", "Jean", "Calliope", "Trisha", "Isolde", "Juliana", "Laura", "Alma"]
legalia_male_name = ["Logan", "Rean", "Bernhardt", "Lantz", "Carpe", "Bran", "Castaban", "Cupid", "Roche", "Arthur", "Gawain", "Desmond", "Zach", "Zweihad", "Lancelot"]

venata_female_name = ["Caroline", "Alice", "Esther", "Polka", "Lucca", "Ariel", "Victoria", "Annette", "Barbara"]
venata_male_name = ["Haringoth", "Julian", "Oliver", "Swaine", "Vivaldi", "Ballister", "Tabor", "Matzo", "Roth", "Linden", "Chopan", "Pildar", "Vernon", "Roscoe", "Kern", "Ronald"]

amoranth_female_name = ["Poppet", "Flitt", "Jakuri","Phoebi", "Mio", "Skara", "Dupree"]
amoranth_male_name = ["Belphegor", "Talon", "Shul'Atok", "Nikademus", "Morgoth", "Kul'Tan", "Charn", "Zod", "Morwick", "Raz", "Ezekiel", "Morath"]

#JOBS - Monk, Chemist, Illusionist, assassin, Warlock
#new jobs need to have changes in job attributes and job preferred weapon
asvogod_female_job = ["Cleric", "Cook", "Shieldbearer", "Witch", "Blacksmith", "Necromancer"]
asvogod_male_job = ["Dragoon", "Shieldbearer", "Berserker", "Merchant", "Blacksmith"]

wuxia_female_job = ["Cleric", "Dancer", "Cook", "Reaper", "Ranger", "Thief", "Necromancer"]
wuxia_male_job = ["Cleric", "Bard", "Samurai", "Reaper", "Ranger", "Thief", "Merchant", "Mage", "Sorcerer", "Necromancer"]

sansoba_female_job = ["Cleric", "Dancer", "Reaper", "Ranger", "Thief", "Merchant", "Mage"]
sansoba_male_job = ["Bard", "Cook", "Gunslinger", "Ranger", "Thief", "Merchant", "Blacksmith", "Mage"]

atennu_female_job = ["Cleric", "Sage", "Witch", "Mage", "Sorcerer", "Druid"]
atennu_male_job = ["Cleric", "Sage", "Spellsword", "Mage", "Sorcerer", "Druid"]

legalia_female_job = ["Cleric", "Bard", "Cook", "Knight", "Gunslinger", "Ranger", "Mage"]
legalia_male_job = ["Bard", "Cook", "Paladin", "Shieldbearer", "Knight", "Gunslinger", "Ranger", "Merchant", "Blacksmith", "Mage", "Sorcerer"]

venata_female_job = ["Cleric", "Bard", "Cook", "Shieldbearer", "Spellsword", "Ranger", "Mage"]
venata_male_job = ["Bard", "Cook", "Dragoon", "Shieldbearer", "Knight", "Spellsword", "Ranger", "Thief", "Merchant", "Blacksmith", "Mage", "Druid"]

amoranth_female_job = ["Cleric", "Bard", "Cook", "Witch", "Mage", "Druid"]
amoranth_male_job = ["Cleric", "Bard", "Cook", "Sage", "Mage", "Sorcerer", "Necromancer", "Druid"]

#RACES
#new races need to have changes in race attributes
asvogod_races = ["Dragonblood", "Half-Orc", "Iron Dwarf", "Venatan", "Dragonkin", "Gnoll", "Lycanthrope", "Snow Elf"]
wuxia_races = ["High Elf", "Low Elf", "Half-Elf", "Legalian", "Wood Elf", "Catfolk", "Vampire"]
sansoba_races = ["Low Elf", "Half-Elf", "Half-Orc", "Hill Dwarf", "Soban", "Lizardfolk", "Rabbitfolk"]
atennu_races = ["Dark Elf", "High Elf", "Half-Elf", "Catfolk", "Pixie", "Rabbitfolk"]
legalia_races = ["High Elf", "Low Elf", "Gnome", "Half-Elf", "Half-Orc", "Legalian", "Soban", "Venatan", "Catfolk", "Lizardfolk", "Rabbitfolk"]
venata_races = ["Dragonblood", "Low Elf", "Half-Elf", "Half-Orc", "Hill Dwarf", "Soban", "Venatan", "Wood Elf", "Lycanthrope", "Painted Elf"]
amoranth_races = ["Dark Elf", "Low Elf", "Gnome", "Half-Elf", "Wood Elf", "Half-Goblin", "Gnoll", "Pixie", "Saytr"]

#FACTIONS - Corpse Brigade
#new factions need to have changes in faction attributes and starting location
asvogod_factions = ["Men of the Mountains", "Asvogod"]
wuxia_factions = ["Adventurer's Guild", "Wuxia"]
sansoba_factions = ["The Caravan", "Free Men", "San Soba"]
atennu_factions = ["Aten Nu"]
legalia_factions = ["Adventurer's Guild", "The Holy Order", "Legalia"]
venata_factions = ["Men of the Mountains", "Free Men", "Adventurer's Guild", "Venata"]
amoranth_factions = ["Amoranth"]

genders = ["Male", "Female"]

class Character:
    def __init__(self, name, gender, race, culture, job, faction, attributes, current_location, renown, alignment, inventory, money, preferred_weapon):
        self.name = name
        self.gender = gender
        self.race = race
        self.culture = culture
        self.job = job
        self.faction = faction
        self.attributes = attributes
        self.current_location = current_location
        self.renown = renown
        self.alignment = alignment
        self.inventory = inventory
        self.money = money
        self.preferred_weapon = preferred_weapon


def generate():
    selected_attributes = { 
        #ATTRIBUTES - gemcutting, swimming, cartography, linguistics, lockpicking
        #new attributes need to have changes across races, classes, and factions, as well as changes to offense/defense and events if necessary
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0,
        "Cooking": 0,
        "Mining": 0,
        "Woodcutting": 0,
        "Smelting": 0,
        "Leatherworking": 0,
        "Enchanting": 0,
        "Summoning": 0,
        "Astral": 0,
        "Umbral": 0,
        "Thunder": 0,
        "Fire": 0,
        "Frost": 0,
        "Acrobatics": 0, 
        "Animal Handling": 0,
        "Athletics": 0,
        "Deception": 0,
        "History": 0,
        "Insight": 0,
        "Intimidation": 0,
        "Investigation": 0,
        "Medicine": 0,
        "Nature": 0,
        "Perception": 0,
        "Performance": 0,
        "Persuasion": 0,
        "Holy": 0,
        "Necromancy": 0,
        "Sleigh of Hand": 0,
        "Stealth": 0,
        "Survival": 0
    }

    selected_culture = cultures[r.randrange(0,len(cultures))]
    selected_gender = genders[r.randrange(0,len(genders))]

    #Select Name and job
    if selected_gender == "Male" and selected_culture == "Asvogod":
        selected_name = asvogod_male_name[r.randrange(0,len(asvogod_male_name))]
        selected_job = asvogod_male_job[r.randrange(0,len(asvogod_male_job))]
    if selected_gender == "Female" and selected_culture == "Asvogod":
        selected_name = asvogod_female_name[r.randrange(0,len(asvogod_female_name))]
        selected_job = asvogod_female_job[r.randrange(0,len(asvogod_female_job))]

    if selected_gender == "Male" and selected_culture == "Wuxia":
        selected_name = wuxia_male_name[r.randrange(0,len(wuxia_male_name))]
        selected_job = wuxia_male_job[r.randrange(0,len(wuxia_male_job))]
    if selected_gender == "Female" and selected_culture == "Wuxia":
        selected_name = wuxia_female_name[r.randrange(0,len(wuxia_female_name))]
        selected_job = wuxia_female_job[r.randrange(0,len(wuxia_female_job))]

    if selected_gender == "Male" and selected_culture == "San Soba":
        selected_name = sansoba_male_name[r.randrange(0,len(sansoba_male_name))]
        selected_job = sansoba_male_job[r.randrange(0,len(sansoba_male_job))]
    if selected_gender == "Female" and selected_culture == "San Soba":
        selected_name = sansoba_female_name[r.randrange(0,len(sansoba_female_name))]
        selected_job = sansoba_female_job[r.randrange(0,len(sansoba_female_job))]

    if selected_gender == "Male" and selected_culture == "Aten Nu":
        selected_name = atennu_male_name[r.randrange(0,len(atennu_male_name))]
        selected_job = atennu_male_job[r.randrange(0,len(atennu_male_job))]
    if selected_gender == "Female" and selected_culture == "Aten Nu":
        selected_name = atennu_female_name[r.randrange(0,len(atennu_female_name))]
        selected_job = atennu_female_job[r.randrange(0,len(atennu_female_job))]

    if selected_gender == "Male" and selected_culture == "Legalia":
        selected_name = legalia_male_name[r.randrange(0,len(legalia_male_name))]
        selected_job = legalia_male_job[r.randrange(0,len(legalia_male_job))]
    if selected_gender == "Female" and selected_culture == "Legalia":
        selected_name = legalia_female_name[r.randrange(0,len(legalia_female_name))]
        selected_job = legalia_female_job[r.randrange(0,len(legalia_female_job))]

    if selected_gender == "Male" and selected_culture == "Venata":
        selected_name = venata_male_name[r.randrange(0,len(venata_male_name))]
        selected_job = venata_male_job[r.randrange(0,len(venata_male_job))]
    if selected_gender == "Female" and selected_culture == "Venata":
        selected_name = venata_female_name[r.randrange(0,len(venata_female_name))]
        selected_job = venata_female_job[r.randrange(0,len(venata_female_job))]

    if selected_gender == "Male" and selected_culture == "Amoranth":
        selected_name = amoranth_male_name[r.randrange(0,len(amoranth_male_name))]
        selected_job = amoranth_male_job[r.randrange(0,len(amoranth_male_job))]
    if selected_gender == "Female" and selected_culture == "Amoranth":
        selected_name = amoranth_female_name[r.randrange(0,len(amoranth_female_name))]
        selected_job = amoranth_female_job[r.randrange(0,len(amoranth_female_job))]
    
    #Select race and faction
    if selected_culture == "Asvogod":
        selected_race = asvogod_races[r.randrange(0,len(asvogod_races))]
        selected_faction = asvogod_factions[r.randrange(0,len(asvogod_factions))]
    
    if selected_culture == "Wuxia":
        selected_race = wuxia_races[r.randrange(0,len(wuxia_races))]
        selected_faction = wuxia_factions[r.randrange(0,len(wuxia_factions))]
    
    if selected_culture == "San Soba":
        selected_race = sansoba_races[r.randrange(0,len(sansoba_races))]
        selected_faction = sansoba_factions[r.randrange(0,len(sansoba_factions))]
    
    if selected_culture == "Aten Nu":
        selected_race = atennu_races[r.randrange(0,len(atennu_races))]
        selected_faction = atennu_factions[r.randrange(0,len(atennu_factions))]

    if selected_culture == "Legalia":
        selected_race = legalia_races[r.randrange(0,len(legalia_races))]
        selected_faction = legalia_factions[r.randrange(0,len(legalia_factions))]

    if selected_culture == "Venata":
        selected_race = venata_races[r.randrange(0,len(venata_races))]
        selected_faction = venata_factions[r.randrange(0,len(venata_factions))]

    if selected_culture == "Amoranth":
        selected_race = amoranth_races[r.randrange(0,len(amoranth_races))]
        selected_faction = amoranth_factions[r.randrange(0,len(amoranth_factions))]

    #attribute adjustments, race: 3 per
    if selected_race == "Dragonblood":
        selected_attributes["Strength"] += 1
        selected_attributes["Constitution"] += 1
        selected_attributes["Survival"] += 1
    if selected_race == "Half-Orc":
        selected_attributes["Strength"] += 1
        selected_attributes["Smelting"] += 1
        selected_attributes["Intimidation"] += 1
    if selected_race == "Iron Dwarf":
        selected_attributes["Constitution"] += 1
        selected_attributes["Mining"] += 1
        selected_attributes["Smelting"] += 1
    if selected_race == "Venatan":
        selected_attributes["Woodcutting"] += 1
        selected_attributes["Leatherworking"] += 1
        selected_attributes["Acrobatics"] += 1
    if selected_race == "Dragonkin":
        selected_attributes["Constitution"] += 1
        selected_attributes["Insight"] += 1
        selected_attributes["Fire"] += 1
    if selected_race == "Gnoll":
        selected_attributes["Mining"] += 1
        selected_attributes["Intimidation"] += 1
        selected_attributes["Enchanting"] += 1
    if selected_race == "Lycanthrope":
        selected_attributes["Strength"] += 1
        selected_attributes["Perception"] += 1
        selected_attributes["Constitution"] += 1
    if selected_race == "Snow Elf":
        selected_attributes["Survival"] += 1
        selected_attributes["Insight"] += 1
        selected_attributes["Smelting"] += 1
    if selected_race == "High Elf":
        selected_attributes["Intelligence"] += 1
        selected_attributes["Wisdom"] += 1
        selected_attributes["Astral"] += 1
    if selected_race == "Low Elf":
        selected_attributes["Sleigh of Hand"] += 1
        selected_attributes["Deception"] += 1
        selected_attributes["Stealth"] += 1
    if selected_race == "Half-Elf":
        selected_attributes["Dexterity"] += 1
        selected_attributes["Perception"] += 1
        selected_attributes["Acrobatics"] += 1
    if selected_race == "Legalian":
        selected_attributes["Athletics"] += 1
        selected_attributes["Charisma"] += 1
        selected_attributes["Persuasion"] += 1
    if selected_race == "Wood Elf":
        selected_attributes["Survival"] += 1
        selected_attributes["Nature"] += 1
        selected_attributes["Animal Handling"] += 1
    if selected_race == "Catfolk":
        selected_attributes["Charisma"] += 1
        selected_attributes["Intelligence"] += 1
        selected_attributes["Acrobatics"] += 1
    if selected_race == "Vampire":
        selected_attributes["Charisma"] += 1
        selected_attributes["Sleigh of Hand"] += 1
        selected_attributes["Dexterity"] += 1
    if selected_race == "Hill Dwarf":
        selected_attributes["Mining"] += 1
        selected_attributes["Leatherworking"] += 1
        selected_attributes["Woodcutting"] += 1
    if selected_race == "Soban":
        selected_attributes["Deception"] += 1
        selected_attributes["Wisdom"] += 1
        selected_attributes["History"] += 1
    if selected_race == "Lizardfolk":
        selected_attributes["Dexterity"] += 1
        selected_attributes["Constitution"] += 1
        selected_attributes["Nature"] += 1
    if selected_race == "Rabbitfolk":
        selected_attributes["Investigation"] += 1
        selected_attributes["Insight"] += 1
        selected_attributes["Intelligence"] += 1
    if selected_race == "Dark Elf":
        selected_attributes["Umbral"] += 1
        selected_attributes["Intelligence"] += 1
        selected_attributes["Wisdom"] += 1
    if selected_race == "Pixie":
        selected_attributes["Astral"] += 1
        selected_attributes["Nature"] += 1
        selected_attributes["Medicine"] += 1
    if selected_race == "Gnome":
        selected_attributes["Intelligence"] += 1
        selected_attributes["Cooking"] += 1
        selected_attributes["Summoning"] += 1
    if selected_race == "Painted Elf":
        selected_attributes["Animal Handling"] += 1
        selected_attributes["Stealth"] += 1
        selected_attributes["Perception"] += 1
    if selected_race == "Half-Goblin":
        selected_attributes["Dexterity"] += 1
        selected_attributes["Woodcutting"] += 1
        selected_attributes["Mining"] += 1
    if selected_race == "Saytr":
        selected_attributes["Cooking"] += 1
        selected_attributes["Performance"] += 1
        selected_attributes["Charisma"] += 1
    
    #attribute adjustments, job: 5 per -- also preferred weapon
    #weapons - staff, pan, lance and shield, hammer, tome, lance, battleaxe, shortsword, circlets, scythe, bow, daggers, lute, katana, pistol, sword and shield, hammer and shield
    # new weapons require changes to job preferences as well as new equipment available
    if selected_job == "Cleric":
        selected_attributes["Holy"] += 1
        selected_attributes["Medicine"] += 1
        selected_attributes["Intelligence"] += 1
        selected_attributes["Astral"] += 1
        selected_attributes["Insight"] += 1

        selected_weapon = "Staff"

    if selected_job == "Cook":
        selected_attributes["Cooking"] += 1
        selected_attributes["Constitution"] += 1
        selected_attributes["Animal Handling"] += 1
        selected_attributes["Survival"] += 1
        selected_attributes["Sleigh of Hand"] += 1

        selected_weapon = "Pan"

    if selected_job == "Shieldbearer":
        selected_attributes["Strength"] += 1
        selected_attributes["Constitution"] += 1
        selected_attributes["Athletics"] += 1
        selected_attributes["Intimidation"] += 1
        selected_attributes["Perception"] += 1

        selected_weapon = "Lance and Shield"

    if selected_job == "Witch":
        selected_attributes["Charisma"] += 1
        selected_attributes["Intelligence"] += 1
        selected_attributes["Umbral"] += 1
        selected_attributes["Necromancy"] += 1
        selected_attributes["Summoning"] += 1

        selected_weapon = "Staff"

    if selected_job == "Blacksmith":
        selected_attributes["Strength"] += 1
        selected_attributes["Mining"] += 1
        selected_attributes["Smelting"] += 1
        selected_attributes["Enchanting"] += 1
        selected_attributes["Perception"] += 1

        selected_weapon = "Hammer"

    if selected_job == "Necromancer":
        selected_attributes["Wisdom"] += 1
        selected_attributes["Intelligence"] += 1
        selected_attributes["Umbral"] += 1
        selected_attributes["Necromancy"] += 1
        selected_attributes["Summoning"] += 1

        selected_weapon = "Tome"

    if selected_job == "Dragoon":
        selected_attributes["Strength"] += 1
        selected_attributes["Acrobatics"] += 1
        selected_attributes["Dexterity"] += 1
        selected_attributes["Constitution"] += 1
        selected_attributes["Athletics"] += 1

        selected_weapon = "Lance"

    if selected_job == "Berserker":
        selected_attributes["Strength"] += 1
        selected_attributes["Constitution"] += 1
        selected_attributes["Intimidation"] += 1
        selected_attributes["Survival"] += 1
        selected_attributes["Athletics"] += 1

        selected_weapon = "Battleaxe"

    if selected_job == "Merchant":
        selected_attributes["Charisma"] += 1
        selected_attributes["Intelligence"] += 1
        selected_attributes["Deception"] += 1
        selected_attributes["Persuasion"] += 1
        selected_attributes["Investigation"] += 1

        selected_weapon = "Shortsword"

    if selected_job == "Dancer":
        selected_attributes["Dexterity"] += 1
        selected_attributes["Acrobatics"] += 1
        selected_attributes["Athletics"] += 1
        selected_attributes["Charisma"] += 1
        selected_attributes["Performance"] += 1

        selected_weapon = "Circlets"

    if selected_job == "Reaper":
        selected_attributes["Umbral"] += 1
        selected_attributes["Strength"] += 1
        selected_attributes["Dexterity"] += 1
        selected_attributes["Constitution"] += 1
        selected_attributes["Enchanting"] += 1

        selected_weapon = "Scythe"

    if selected_job == "Ranger":
        selected_attributes["Perception"] += 1
        selected_attributes["Nature"] += 1
        selected_attributes["Investigation"] += 1
        selected_attributes["Survival"] += 1
        selected_attributes["Animal Handling"] += 1

        selected_weapon = "Bow"

    if selected_job == "Thief":
        selected_attributes["Sleigh of Hand"] += 1
        selected_attributes["Stealth"] += 1
        selected_attributes["Perception"] += 1
        selected_attributes["Deception"] += 1
        selected_attributes["Investigation"] += 1

        selected_weapon = "Daggers"

    if selected_job == "Bard":
        selected_attributes["Charisma"] += 1
        selected_attributes["Performance"] += 1
        selected_attributes["History"] += 1
        selected_attributes["Acrobatics"] += 1
        selected_attributes["Dexterity"] += 1

        selected_weapon = "Lute"

    if selected_job == "Samurai":
        selected_attributes["Strength"] += 1
        selected_attributes["Dexterity"] += 1
        selected_attributes["Athletics"] += 1
        selected_attributes["Perception"] += 1
        selected_attributes["Sleigh of Hand"] += 1

        selected_weapon = "Katana"

    if selected_job == "Mage":
        selected_attributes["Fire"] += 1
        selected_attributes["Frost"] += 1
        selected_attributes["Thunder"] += 1
        selected_attributes["Intelligence"] += 1
        selected_attributes["Enchanting"] += 1

        selected_weapon = "Tome"

    if selected_job == "Sorcerer":
        selected_attributes["Astral"] += 1
        selected_attributes["Umbral"] += 1
        selected_attributes["Intelligence"] += 1
        selected_attributes["Wisdom"] += 1
        selected_attributes["Summoning"] += 1

        selected_weapon = "Staff"

    if selected_job == "Gunslinger":
        selected_attributes["Perception"] += 1
        selected_attributes["Dexterity"] += 1
        selected_attributes["Charisma"] += 1
        selected_attributes["Sleigh of Hand"] += 1
        selected_attributes["Performance"] += 1

        selected_weapon = "Pistol"

    if selected_job == "Sage":
        selected_attributes["Astral"] += 1
        selected_attributes["Umbral"] += 1
        selected_attributes["Intelligence"] += 1
        selected_attributes["Insight"] += 1
        selected_attributes["History"] += 1

        selected_weapon = "Tome"

    if selected_job == "Druid":
        selected_attributes["Nature"] += 1
        selected_attributes["Animal Handling"] += 1
        selected_attributes["Summoning"] += 1
        selected_attributes["Wisdom"] += 1
        selected_attributes["Medicine"] += 1

        selected_weapon = "Staff"

    if selected_job == "Spellsword":
        selected_attributes["Fire"] += 1
        selected_attributes["Thunder"] += 1
        selected_attributes["Frost"] += 1
        selected_attributes["Dexterity"] += 1
        selected_attributes["Athletics"] += 1

        selected_weapon = "Shortsword"

    if selected_job == "Knight":
        selected_attributes["Strength"] += 1
        selected_attributes["Constitution"] += 1
        selected_attributes["Athletics"] += 1
        selected_attributes["Investigation"] += 1
        selected_attributes["Survival"] += 1

        selected_weapon = "Sword and Shield"

    if selected_job == "Paladin":
        selected_attributes["Holy"] += 1
        selected_attributes["Strength"] += 1
        selected_attributes["Constitution"] += 1
        selected_attributes["Investigation"] += 1
        selected_attributes["Intimidation"] += 1

        selected_weapon = "Hammer and Shield"

    #attribute adjustments, faction: 1 per
    if selected_faction == "Men of the Mountains":
        selected_attributes["Mining"] += 1
    if selected_faction == "Asvogod":
        selected_attributes["Survival"] += 1
    if selected_faction == "Adventurer's Guild":
        selected_attributes["Constitution"] += 1
    if selected_faction == "Wuxia":
        selected_attributes["Stealth"] += 1
    if selected_faction == "The Caravan":
        selected_attributes["Performance"] += 1
    if selected_faction == "Free Men":
        selected_attributes["Perception"] += 1
    if selected_faction == "San Soba":
        selected_attributes["Deception"] += 1
    if selected_faction == "Aten Nu":
        selected_attributes["Intelligence"] += 1
    if selected_faction == "The Holy Order":
        selected_attributes["Holy"] += 1
    if selected_faction == "Legalia":
        selected_attributes["Charisma"] += 1
    if selected_faction == "Venata":
        selected_attributes["Strength"] += 1
    if selected_faction == "Amoranth":
        selected_attributes["Nature"] += 1

    #initial placement - asvogod_territory = ["Felghana", "Olbereth", "Orthanc"]
    #wuxia_territory = ["Shendao"]
    #ansoba_territory = ["Anabennar", "Karateka", "The Moorish Gap"]
    #atennu_territory = ["Telos", "Misthaven", "Altes"]
    #legalia_territory = ["Archea", "Solasta", "Mangsvance", "Solitaire"]
    #venata_territory = ["Verdigris", "Aristo", "Condor", "Arabath", "Gilboa"]
    #amoranth_territory = ["Ashwood", "Beggar's Grove", "Ambervale", "Wurmswood", "Nethervale", "The Dreadlands"]
    if selected_faction == "Men of the Mountains":
        selected_location = "Arabath"
    if selected_faction == "Asvogod":
        selected_location = "Orthanc"
    if selected_faction == "Adventurer's Guild":
        selected_location = "Solasta"
    if selected_faction == "Wuxia":
        selected_location = "Shendao"
    if selected_faction == "The Caravan":
        selected_location = "The Moorish Gap"
    if selected_faction == "Free Men":
        selected_location = "Condor"
    if selected_faction == "San Soba":
        selected_location = "Anabennar"
    if selected_faction == "Aten Nu":
        selected_location = "Telos"
    if selected_faction == "The Holy Order":
        selected_location = "Archea"
    if selected_faction == "Legalia":
        selected_location = "Solitaire"
    if selected_faction == "Venata":
        selected_location = "Gilboa"
    if selected_faction == "Amoranth":
        selected_location = "Ashwood"

    adventurer = Character(selected_name,selected_gender,selected_race,selected_culture,selected_job,selected_faction, selected_attributes, selected_location, 0, r.randrange(-10,10), [], 0, selected_weapon)

    return adventurer