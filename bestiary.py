import random as r
import items as i

class Enemy:
    def __init__(self, name, type, offense, defense, money, items):
        self.name = name
        self.type = type
        self.offense = offense
        self.defense = defense
        self.money = money
        self.items = items

#PLEASE NOTE: offense, defense, money, items all need to be adjusted later

#animals
giant_scorpion = Enemy("Giant Scorpion", "animals", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
dire_wolf = Enemy("Dire Wolf", "animals", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
armored_lizard = Enemy("Armored Lizard", "animals", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
warg = Enemy("Warg", "animals", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
gryphon = Enemy("Gryphon", "animals", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
armored_dinosaur = Enemy("Armored Dinosaur", "animals", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
armored_drake = Enemy("Armored Drake", "animals", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])


#humanoid
black_knight = Enemy("Black Knight", "humanoid", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
wild_vampire = Enemy("Wild Vampire", "humanoid", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
wild_lycanthrope = Enemy("Wild Lycanthrope", "humanoid", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
goblin = Enemy("Goblin", "humanoid", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
deserter = Enemy("Deserter", "humanoid", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
kobold = Enemy("Kobold", "humanoid", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
bandit = Enemy("Bandit", "humanoid", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
orc = Enemy("Orc", "humanoid", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
slaver = Enemy("Slaver", "humanoid", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
blood_orc = Enemy("Blood Orc", "humanoid", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
umbral_mage = Enemy("Umbral Mage", "humanoid", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
ogre = Enemy("Ogre", "humanoid", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])

#monsters
skinwalker = Enemy("Skinwalker", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
harpy = Enemy("Harpy", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
mindbender = Enemy("Mindbender", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
siren = Enemy("Siren", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
gargoyle = Enemy("Gargoyle", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
mountain_stalker = Enemy("Mountain Stalker", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
slime = Enemy("Slime", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
blade_widow = Enemy("Blade Widow", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
minotaur = Enemy("Minotaur", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
hurly_burly = Enemy("Hurly Burly", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
clinger = Enemy("Clinger", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
forest_troll = Enemy("Forest Troll", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
frost_troll = Enemy("Frost Troll", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
wurmhund = Enemy("Wurmhund", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
gemcaster = Enemy("Gemcaster", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
gorgon = Enemy("Gorgon", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
mimic = Enemy("Mimic", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
golem = Enemy("Golem", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
dreadwulf = Enemy("Dreadwulf", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
megataur = Enemy("Megataur", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
wurmrunner = Enemy("Wurmrunner", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
comet_chaser = Enemy("Comet Chaser", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
jotun = Enemy("Jotun", "monster", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])

#undead 
lich = Enemy("Lich", "undead", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
shambler = Enemy("Shambler", "undead", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
lesser_demon = Enemy("Lesser Demon", "undead", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
succubus = Enemy("Succubus", "undead", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])
greater_demon = Enemy("Greater Demon", "undead", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])


#location enemies
felghana_enemies = []
olbereth_enemies = []
orthanc_enemies = []
shendao_enemies = []
anabennar_enemies = []
karateka_enemies = [bandit]
moorish_enemies = []
telos_enemies = []
misthaven_enemies = []
altes_enemies = []
archea_enemies = []
solasta_enemies = []
mangsvance_enemies = []
solitaire_enemies = []
verdigris_enemies = []
aristo_enemies = []
condor_enemies = []
arabath_enemies = []
gilboa_enemies = []
ashwood_enemies = []
beggar_enemies = []
ambervale_enemies = []
wurmswood_enemies = []
nethervale_enemies = []
dreadlands_enemies = []
