import random as r
import items as i

class Enemy:
    def __init__(self, name, offense, defense, money, items):
        self.name = name
        self.offense = offense
        self.defense = defense
        self.money = money
        self.items = items


#ENEMIES - Black Knight, Skinwalker, Harpy, Mindbender, Wild Vampire, Wild Lycanthrope, Siren, Gargoyle, Mountain Stalker, Giant Scorpion, Lich
#low level - "Goblin", "Deserter", "Kobold", "Slime", "Shambler", "Armored Lizard", "Warg"
bandit = Enemy("Bandit", r.randrange(2,5), r.randrange(2,5), r.randrange(0,10), [])

#mid level - "Gryphon", "Blade Widow", "Minotaur", "Orc", "Hurly Burly", "Clinger", "Slaver", "Blood Orc", "Forest Troll", "Frost Troll", "Wurmhund", "Lesser Demon", "Succubus", "Gemcaster", "Armored Dinosaur", "Gorgon", "Mimic", "Golem", "Umbral Mage"

#high level - "Dreadwulf", "Megataur", "Ogre", "Wurmrunner", "Greater Demon", "Armored Drake", "Comet Chaser", "Jotun"


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
