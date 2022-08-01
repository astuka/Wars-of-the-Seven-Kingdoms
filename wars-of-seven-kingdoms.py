import random as r
import character_creator as c
import bestiary as b
import items as i

#lore notes
#venata and asvogod both have dragoons because they were up north where dragons were
#mythril is found in the mountains between venata and asvogod -- they often fight over it
#valosykr -- valhalla equivalent for asvogod
#necromancy is banned in aten nu
#goblins are usually peasant workers among orc tribes
#sages are gifted magic students, sorcerers are veterans, mages are the rest of the lot
#-vance is a common suffix in Legalian towns (meaning literally "town")

#DEITIES - Ishtar, Saami

#LOCATIONS - Killbragant, Al Khazan, Dragenvance, Darkmoon, Dranor, Edo, Vindale, Tyr, Mandal, Lanathor, Riva, Stygian Abyss, Darkspyre, Trinsic, Serpentine Isles, Kendor, Mordvania
#new locations need changes to map nodes, kingdom territories, and enemy spawns
all_locations = ["Felghana", "Olbereth", "Orthanc","Shendao","Anabennar", "Karateka", "The Moorish Gap", "Telos", "Misthaven", "Altes","Archea", "Solasta", "Mangsvance", "Solitaire","Verdigris", "Aristo", "Condor", "Arabath", "Gilboa","Ashwood", "Beggar's Grove", "Ambervale", "Wurmswood", "Nethervale", "The Dreadlands"]

class Kingdom:
    def __init__(self, name, territory, status):
        self.name = name
        self.territory = territory
        self.status = status

asvogod = Kingdom("Asvogod",["Felghana", "Olbereth", "Orthanc"], {"Asvogod": "Self", "Wuxia": "Peace", "San Soba": "Peace", "Aten Nu": "Peace", "Legalia": "Peace", "Venata": "Peace", "Amoranth": "Peace"})
wuxia = Kingdom("Wuxia",["Shendao"], {"Asvogod": "Peace", "Wuxia": "Self", "San Soba": "Peace", "Aten Nu": "Peace", "Legalia": "Peace", "Venata": "Peace", "Amoranth": "Peace"})
sansoba = Kingdom("San Soba",["Anabennar", "Karateka", "The Moorish Gap"], {"Asvogod": "Peace", "Wuxia": "Peace", "San Soba": "Self", "Aten Nu": "Peace", "Legalia": "Peace", "Venata": "Peace", "Amoranth": "Peace"})
atennu = Kingdom("Aten Nu",["Telos", "Misthaven", "Altes"], {"Asvogod": "Peace", "Wuxia": "Peace", "San Soba": "Peace", "Aten Nu": "Self", "Legalia": "Peace", "Venata": "Peace", "Amoranth": "Peace"})
legalia = Kingdom("Legalia",["Archea", "Solasta", "Mangsvance", "Solitaire"], {"Asvogod": "Peace", "Wuxia": "Peace", "San Soba": "Peace", "Aten Nu": "Peace", "Legalia": "Self", "Venata": "Peace", "Amoranth": "Peace"})
venata = Kingdom("Venata",["Verdigris", "Aristo", "Condor", "Arabath", "Gilboa"], {"Asvogod": "Peace", "Wuxia": "Peace", "San Soba": "Peace", "Aten Nu": "Peace", "Legalia": "Peace", "Venata": "Self", "Amoranth": "Peace"})
amoranth = Kingdom("Amoranth",["Ashwood", "Beggar's Grove", "Ambervale", "Wurmswood", "Nethervale", "The Dreadlands"], {"Asvogod": "Peace", "Wuxia": "Peace", "San Soba": "Peace", "Aten Nu": "Peace", "Legalia": "Peace", "Venata": "Peace", "Amoranth": "Self"})

kingdoms = [asvogod,wuxia,sansoba,atennu,legalia,venata,amoranth]

#SKILLS - Paralyze, Rune Missile
skills = ["Chaos Strike", "Glory of Valoskyr", "Bloodlust", "War Cry", "Heavy Hitter", "Rampage", "Aetherburst", "Thundercracker", "Frostfall", "Firestorm", "Hollow Point", "Wildly Armed", "Rapid Fire", "Reload", "Plaguing Doom", "Scarlet Grace", "Beast Communion", "Plague", "Devil's Kiss", "Deathly Gaze", "Razor's Edge", "Viral Influx", "Umbral Shock", "Divine Sacrifice", "Knight's Honor", "Know Thyself", "Planet Cracker", "Ash and Gunpowder", "Fortify", "Artillery Barrage", "Bushido", "1000 Cuts", "Bloody Slice", "Harakiri", "Evade", "Death on High", "Dragon Communion", "Charge", "Dragon Dive", "God's Chosen", "Divine Strike", "Holy Wrath", "Hammer Throw", "Umbral Collapse", "Astral Lift", "Aethersurge", "Family Feast", "Mise en Scene", "Order Up!", "High Heat", "Carve", "Orchestra", "Chord of Death", "Shanty", "Lullaby", "Dance of All Seasons", "Waltz", "Samba", "Two-Step", "Charm", "Blessing of God", "Holy Writ", "Cleansing Spirit", "Healing Chime", "Holy", "Pool of Radiance", "Deal Breaker", "Infinite Light", "Manta", "Thrash Disposal", "Golden Earth", "Jamais Vu", "Bash", "Catastrophe", "Hades Blast", "Acrobat Kick", "Debilitate"]

roster = []
hallofheroes = []

for i in range(20):
    adventurer = c.generate()
    roster.append(adventurer)

game = True

#game loop
while game:
    #before rolling
    
    player_input = input("What do you wish to do?\n")

    if "roster" in player_input:
        for i in roster:
            print(i.name+", the "+i.gender+" "+i.race+" "+i.job+". Currently in "+i.current_location+".")

    if "run" in player_input:
        for i in range(20):
            roll = r.randrange(0,17)
            if roll == 0: #paladin v. witch/necromancer/reaper
                person1 = roster[r.randrange(0,len(roster))]
                person2 = roster[r.randrange(0,len(roster))]
                if person1 != person2 and person1.job == "Paladin" and (person2.job == "Necromancer" or person2.job == "Witch" or person2.job == "Reaper") and person1.current_location == person2.current_location:
                    print(person1.name+" the "+person1.race+" "+person1.job+" has spotted a "+person2.job+" while staying in "+person1.current_location+", and challenges them to a duel.")
                    if (person1.attributes["Strength"] + person1.attributes["Dexterity"] + person1.attributes["Intelligence"] + person1.attributes["Summoning"] + person1.attributes["Astral"] + person1.attributes["Umbral"] + person1.attributes["Thunder"] + person1.attributes["Fire"] + person1.attributes["Frost"] + person1.attributes["Perception"] + person1.attributes["Holy"] + person1.attributes["Necromancy"]) > (person2.attributes["Constitution"] +  person2.attributes["Acrobatics"] + person2.attributes["Athletics"] + person2.attributes["Medicine"] + person2.attributes["Holy"] + person2.attributes["Survival"]):
                        print(person1.name+ " won the duel, slaying "+person2.name+".")
                        for item in person2.inventory:
                            person1.inventory.append(item)
                        roster.remove(person2)
                        person1.renown += 10
                    else:
                        print(person1.name+" was defeated by "+person2.name+", getting slain in the process.")
                        for item in person1.inventory:
                            person2.inventory.append(item)
                        roster.remove(person1)
                        person2.renown += 10      

            if roll == 1: #generic duel
                person1 = roster[r.randrange(0,len(roster))]
                person2 = roster[r.randrange(0,len(roster))]
                if person1 != person2 and person1.current_location == person2.current_location and person1.alignment <= 5 and person2.alignment <= 5:
                    print(person1.name+" the "+person1.race+" "+person1.job+" has challenged "+person2.name+" the "+person2.race+" "+person2.job+" to a duel.")
                    if (person1.attributes["Strength"] + person1.attributes["Dexterity"] + person1.attributes["Intelligence"] + person1.attributes["Summoning"] + person1.attributes["Astral"] + person1.attributes["Umbral"] + person1.attributes["Thunder"] + person1.attributes["Fire"] + person1.attributes["Frost"] + person1.attributes["Perception"] + person1.attributes["Holy"] + person1.attributes["Necromancy"]) > (person2.attributes["Constitution"] +  person2.attributes["Acrobatics"] + person2.attributes["Athletics"] + person2.attributes["Medicine"] + person2.attributes["Holy"] + person2.attributes["Survival"]):
                        print(person1.name+ " won the duel, slaying "+person2.name+".")
                        for item in person2.inventory:
                            person1.inventory.append(item)
                        roster.remove(person2)
                        person1.renown += 10
                    else:
                        print(person1.name+" was defeated by "+person2.name+", getting slain in the process.")
                        for item in person1.inventory:
                            person2.inventory.append(item)
                        roster.remove(person1)
                        person2.renown += 10

            if roll == 2: #healer
                person1 = roster[r.randrange(0,len(roster))]
                if person1.attributes["Medicine"] > 0 or person1.attributes["Holy"] > 0:
                    print(person1.name+" the "+person1.race+" "+person1.job+" has healed some people in the area, gaining alignment and renown as well as improving their skill.")
                    person1.renown += 10
                    person1.alignment += 1
                    person1.attributes["Medicine"] += 1

            if roll == 3: #party
                party_location = all_locations[r.randrange(0,len(all_locations))]
                print("There was a party at "+party_location+". All those present gained 1 Constitution from all the good food and drink.")
                for i in roster:
                    if i.current_location == party_location:
                        i.attributes["Constitution"] += 1

            if roll == 4: #summoning check
                person1 = roster[r.randrange(0,len(roster))]
                if person1.attributes['Summoning'] == 0:
                    print(person1.name+" the "+person1.race+" "+person1.job+" tried to summon a lesser demon. Unfortunately for them, they didnt have the skills to control it, and it ended up eviscerating their body.")
                    roster.remove(person1)
                else:
                    print(person1.name+" the "+person1.race+" "+person1.job+" tried to summon a lesser demon, and succeeded. They gained skill in Summoning.")
                    person1.attributes['Summoning'] += 1
                    person1.renown += 5

            if roll == 5: #exercise
                person1 = roster[r.randrange(0,len(roster))]
                print(person1.name+" did some physical exercise, improving their Athletics.")
                person1.attributes["Athletics"] += 1

            if roll == 6: #survival check
                person1 = roster[r.randrange(0,len(roster))]
                if person1.attributes["Survival"] == 0 and person1.attributes["Nature"] == 0:
                    print(person1.name+" the "+person1.race+" "+person1.job+" got lost in the woods. Unfortunately, they did not have the skills to get out and survive.")
                    roster.remove(person1)
                else:
                    print(person1.name+" the "+person1.race+" "+person1.job+" got lost in the woods. But thanks to their Survival and Nature skill, they were able to get out unscathed.")
                    person1.attributes["Survival"] += 1
                    person1.renown += 5
            
            if roll == 7: #thieving attempt
                person1 = roster[r.randrange(0,len(roster))]
                if person1.alignment < 0:
                    if person1.attributes["Stealth"] == 0 or person1.attributes["Sleigh of Hand"] == 0:
                        print(person1.name+" the "+person1.race+" "+person1.job+" unsuccessfully tried to steal, and was sent to the town jail (except not really because I haven't added this feature yet LOL)")
                    else:
                        stolen_money = r.randrange(0,100)
                        print(person1.name+" the "+person1.race+" "+person1.job+" successfully stole "+str(stolen_money)+" gold while thieving.")
                        person1.money += stolen_money
                        person1.attributes["Stealth"] += 1
                        person1.alignment -= 1

            if roll == 8: #trap check
                person1 = roster[r.randrange(0,len(roster))]
                if person1.attributes["Insight"] >= 1 or person1.attributes["Investigation"] >= 1 or person1.attributes["Perception"] >= 1:
                    print(person1.name+" the "+person1.race+" "+person1.job+" almost fell into a trap. Fortunately, they were able to spot it beforehand.")
                    person1.attributes["Perception"] += 1
                else:
                    print(person1.name+" the "+person1.race+" "+person1.job+" fell into a trap and died.")
                    roster.remove(person1)

            if roll == 9: #battling
                person1 = roster[r.randrange(0,len(roster))]

                if person1.current_location == "Karateka":
                    selected_enemy = b.karateka_enemies[r.randrange(0,len(b.karateka_enemies))]
                    print(person1.name+" the "+person1.race+" "+person1.job+" is battling a "+selected_enemy.name)
                    #win/lose based on who gets beaten
            
            if roll == 10: #viking raid
                raids = ["Aristo", "Verdigris"] #viking raid locations, check these
                raided = raids[r.randrange(0,len(raids))]
                raid_offense = r.randrange(0,100)
                raid_defense = r.randrange(0,100)
                town_offense = 0
                town_defense = 0

                print("A viking raid has occurred in the land of "+raided)

                for i in roster:
                    if i.current_location == raided: #make it so that asvogodians dont help?
                        town_offense += i.attributes["Strength"] + i.attributes["Dexterity"] + i.attributes["Intelligence"] + i.attributes["Summoning"] + i.attributes["Astral"] + i.attributes["Umbral"] + i.attributes["Thunder"] + i.attributes["Fire"] + i.attributes["Frost"] + i.attributes["Perception"] + i.attributes["Holy"] + i.attributes["Necromancy"] 
                        town_defense += i.attributes["Constitution"] +  i.attributes["Acrobatics"] + i.attributes["Athletics"] + i.attributes["Medicine"] + i.attributes["Holy"] + i.attributes["Survival"]

                if town_offense - raid_defense > raid_offense - town_defense:
                    print("The town has successfully fought off the invasion, earning renown for all those involved.")
                    for i in roster:
                        if i.current_location == raided:
                            i.attributes["Constitution"] += 1
                            i.renown += 10
                else:
                    print("The vikings have successfully raided the village.")
                    for i in roster:
                        if i.current_location == raided:
                                print(i.name+" the "+i.race+" "+i.job+" has been killed in the raid on "+raided)
                                roster.remove(i)

            if roll == 11: #war declaration
                kingdom1 = kingdoms[r.randrange(0,len(kingdoms))]
                kingdom2 = kingdoms[r.randrange(0,len(kingdoms))]

                if kingdom1 != kingdom2 and kingdom1.status[kingdom2.name] == "Peace" and kingdom2.status[kingdom1.name] == "Peace":
                    kingdom1.status[kingdom2.name] = "War"
                    kingdom2.status[kingdom1.name] = "War"
                    print(kingdom1.name+" has declared war on "+kingdom2.name+"!")
                    #check for allies

            if roll == 12: #hall of heroes
                person1 = roster[r.randrange(0,len(roster))]
                if person1.renown > 100 and person1 not in hallofheroes:
                    print(person1.name+" the "+person1.race+" "+person1.job+" now has enough renown to join the hall of heroes!")
                    hallofheroes.append(person1)
                    print("The Hall of Heroes now contains:")
                    for i in hallofheroes:
                        print(i.name+" the "+i.race+" "+i.job)

            if roll == 13: #battle
                kingdom1 = kingdoms[r.randrange(0,len(kingdoms))]
                kingdom2 = kingdoms[r.randrange(0,len(kingdoms))]

                if kingdom1.status[kingdom2.name] == "War" and kingdom2.status[kingdom1.name] == "War": 
                    battlegrounds = [*kingdom1.territory, *kingdom2.territory]
                    battle_location = battlegrounds[r.randrange(0,len(battlegrounds))]
                    print("A battle has occurred in "+battle_location+" between "+kingdom1.name+" and "+kingdom2.name+"!")
                    king1_offense = 0
                    king1_defense = 0
                    king2_offense = 0
                    king2_defense = 0
                    king1_team = []
                    king2_team = []
                    for i in roster:
                        if i.faction == kingdom1.name:
                            king1_team.append(i) 
                            king1_offense += i.attributes["Strength"] + i.attributes["Dexterity"] + i.attributes["Intelligence"] + i.attributes["Summoning"] + i.attributes["Astral"] + i.attributes["Umbral"] + i.attributes["Thunder"] + i.attributes["Fire"] + i.attributes["Frost"] + i.attributes["Perception"] + i.attributes["Holy"] + i.attributes["Necromancy"] 
                            king1_defense += i.attributes["Constitution"] +  i.attributes["Acrobatics"] + i.attributes["Athletics"] + i.attributes["Medicine"] + i.attributes["Holy"] + i.attributes["Survival"]
                        if i.faction == kingdom2.name:
                            king2_team.append(i)
                            king2_offense += i.attributes["Strength"] + i.attributes["Dexterity"] + i.attributes["Intelligence"] + i.attributes["Summoning"] + i.attributes["Astral"] + i.attributes["Umbral"] + i.attributes["Thunder"] + i.attributes["Fire"] + i.attributes["Frost"] + i.attributes["Perception"] + i.attributes["Holy"] + i.attributes["Necromancy"] 
                            king2_defense += i.attributes["Constitution"] +  i.attributes["Acrobatics"] + i.attributes["Athletics"] + i.attributes["Medicine"] + i.attributes["Holy"] + i.attributes["Survival"]
                    if king1_offense - king2_defense > king2_offense - king2_defense:
                        print(kingdom1.name+" has won the battle!")
                        if battle_location in kingdom2.territory:
                            print(kingdom1.name+" has captured "+battle_location+"!")
                            kingdom1.territory.append(battle_location)
                            kingdom2.territory.remove(battle_location)
                        if len(king2_team) >= 1:
                            slain = king2_team[r.randrange(0, len(king2_team))]
                            print(slain.name+" the "+slain.race+" "+slain.job+" has been killed battle!")
                            roster.remove(slain)
                    else:
                        print(kingdom2.name+" has won the battle!")
                        if battle_location in kingdom1.territory:
                            print(kingdom2.name+" has captured "+battle_location+"!")
                            kingdom2.territory.append(battle_location)
                            kingdom1.territory.remove(battle_location)
                        if len(king1_team) >= 1:
                            slain = king1_team[r.randrange(0, len(king1_team))]
                            print(slain.name+" the "+slain.race+" "+slain.job+" has been killed battle!")
                            roster.remove(slain)
            
            if roll == 14: #performance check
                person1 = roster[r.randrange(0,len(roster))]
                print(person1.name+" the "+person1.race+" "+person1.job+" did a performance in "+person1.current_location+".")

                if person1.attributes["Performance"] == 0:
                    print("Unfortunately, their performance wasn't high enough and they were panned. Still, they did gain some experience.")
                    person1.attributes["Performance"] += 1
                else:
                    performance_money = 10 * person1.attributes["Performance"]
                    print("People enjoyed "+person1.name+"'s performance! They gained "+str(performance_money)+" in gold.")
                    person1.money += performance_money
                    person1.renown += 10
                    person1.attributes["Performance"] += 1

            if roll == 15: #investing
                person1 = roster[r.randrange(0,len(roster))]
                if person1.money >= 1000:
                    print(person1.name+" the "+person1.race+" "+person1.job+" has gained quite a bit of money, and decided to invest it.")
                    chance = r.randrange(0,2)
                    if chance == 0:
                        person1.money = person1.money / 2
                        print("Unfortunately, the investment failed and "+person1.name+"'s gold fell to "+str(person1.money))
                    else:
                        person1.money = person1.money * 2
                        print("The investment worked out, and "+person1.name+"'s gold increased to "+str(person1.money)+"!")
            
            if roll == 16:#new adventurer
                adventurer = c.generate()
                roster.append(adventurer)
                print("A new adventurer named "+adventurer.name+" the "+adventurer.race+" "+adventurer.job+" has shown up in "+adventurer.current_location+".")

                    







    #after rolling
    #game end check
    if len(wuxia.territory)==0 and len(sansoba.territory)== 0 and len(atennu.territory)== 0 and len(legalia.territory)== 0 and len(venata.territory) == 0 and len(amoranth.territory) == 0:
        print("Asvogod wins! The game is over.")
        game = False
    if len(asvogod.territory)==0 and len(sansoba.territory)== 0 and len(atennu.territory)== 0 and len(legalia.territory)== 0 and len(venata.territory) == 0 and len(amoranth.territory) == 0: 
        print("Wuxia wins! The game is over.")
        game = False
    if len(asvogod.territory)==0 and len(wuxia.territory)== 0 and len(atennu.territory)== 0 and len(legalia.territory)== 0 and len(venata.territory) == 0 and len(amoranth.territory) == 0:# NEEDS FIXING
        print("San Soba wins! The game is over.")
        game = False
    if len(wuxia.territory)==0 and len(sansoba.territory)== 0 and len(asvogod.territory)== 0 and len(legalia.territory)== 0 and len(venata.territory) == 0 and len(amoranth.territory) == 0:# NEEDS FIXING
        print("Aten Nu wins! The game is over.")
        game = False
    if len(wuxia.territory)==0 and len(sansoba.territory)== 0 and len(atennu.territory)== 0 and len(asvogod.territory)== 0 and len(venata.territory) == 0 and len(amoranth.territory) == 0:# NEEDS FIXING
        print("Legalia wins! The game is over.")
        game = False
    if len(wuxia.territory)==0 and len(sansoba.territory)== 0 and len(atennu.territory)== 0 and len(legalia.territory)== 0 and len(asvogod.territory) == 0 and len(amoranth.territory) == 0:# NEEDS FIXING
        print("Venata wins! The game is over.")
        game = False
    if len(wuxia.territory)==0 and len(sansoba.territory)== 0 and len(atennu.territory)== 0 and len(legalia.territory)== 0 and len(venata.territory) == 0 and len(asvogod.territory) == 0:# NEEDS FIXING
        print("Amoranth wins! The game is over.")
        game = False

    #Map Nodes
    for i in roster:
        if i.current_location == "Felghana":
            visitable_locations = ["Felghana", "Olbereth", "Orthanc", "Aristo", "Verdigris"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Olbereth":
            visitable_locations = ["Olbereth", "Felghana", "Orthanc", "Arabath"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Orthanc":
            visitable_locations = ["Orthanc", "Felghana", "Olbereth"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Shendao":
            visitable_locations = ["Shendao", "Ashwood", "Solitaire"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Anabennar":
            visitable_locations = ["Anabennar", "Karateka", "The Moorish Gap", "Gilboa"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Karateka":
            visitable_locations = ["Karateka", "Anabennar", "The Moorish Gap"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "The Moorish Gap":
            visitable_locations = ["The Moorish Gap", "Anabennar", "Karateka", "Condor"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Telos":
            visitable_locations = ["Telos", "Misthaven", "Altes"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Misthaven":
            visitable_locations = ["Misthaven", "Telos", "Altes"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Altes":
            visitable_locations = ["Altes", "Misthaven", "Telos", "Aristo"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Archea":
            visitable_locations = ["Archea", "Wurmswood", "Solasta"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Solasta":
            visitable_locations = ["Solasta", "Gilboa", "Archea", "Mangsvance", "Solitaire"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Mangsvance":
            visitable_locations = ["Mangsvance", "Solitaire", "Solasta", "Ambervale"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Solitaire":
            visitable_locations = ["Solitaire", "Shendao", "Ashwood", "Mangsvance", "Solasta"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Verdigris":
            visitable_locations = ["Verdigris", "Felghana", "Aristo", "Gilboa"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Aristo":
            visitable_locations = ["Aristo", "Arabath", "Felghana", "Altes", "Verdigris"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Condor":
            visitable_locations = ["Condor", "Arabath", "The Moorish Gap"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Arabath":
            visitable_locations = ["Arabath", "Olbereth", "Condor", "Aristo"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Gilboa":
            visitable_locations = ["Gilboa", "Anabennar", "Solasta", "Verdigris"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Ashwood":
            visitable_locations = ["Ashwood", "Shendao", "Solitaire", "Ambervale", "Beggar's Grove"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Beggar's Grove":
            visitable_locations = ["Beggar's Grove", "Ashwood", "Nethervale"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Ambervale":
            visitable_locations = ["Ambervale", "Mangsvance", "Ashwood"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Wurmswood":
            visitable_locations = ["Wurmswood", "Archea", "Nethervale"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "Nethervale":
            visitable_locations = ["Nethervale", "The Dreadlands", "Wurmswood", "Beggar's Grove"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        if i.current_location == "The Dreadlands":
            visitable_locations = ["The Dreadlands", "Nethervale"]
            i.current_location = visitable_locations[r.randrange(0,len(visitable_locations))]
        

