import MySQLdb as sql, sys, json

set_list = {
	"dtk":      "Dragons of Tarkir",
	"frf":      "Fate Reforged",
	"ktk":      "Khans of Tarkir",
	"jou":      "Journey into Nyx",
	"bng":      "Born of the Gods",
	"ths":      "Theros",
	"dgm":      "Dragon's Maze",
	"gtc":      "Gatecrash",
	"rtr":      "Return to Ravnica",
	"avr":      "Avacyn Restored",
	"dka":      "Dark Ascension",
	"isd":      "Innistrad",
	"nph":      "New Phyrexia",
	"mbs":      "Mirrodin Besieged",
	"som":      "Scars of Mirrodin",
	"roe":      "Rise of the Eldrazi",
	"wwk":      "Worldwake",
	"zen":      "Zendikar",
	"arb":      "Alara Reborn",
	"cfx":      "Conflux",
	"ala":      "Shards of Alara",
	"eve":      "Eventide",
	"shm":      "Shadowmoor",
	"mt":       "Morningtide",
	"lw":       "Lorwyn",
	"fut":      "Future Sight",
	"pc":       "Planar Chaos",
	"ts":       "Time Spiral",
	"tsts":     "Time Spiral `Timeshifted`",
	"cs":       "Coldsnap",
	"ai":       "Alliances",
	"ia":       "Ice Age",
	"di":       "Dissension",
	"gp":       "Guildpact",
	"rav":      "Ravnica: City of Guilds",
	"sok":      "Saviors of Kamigawa",
	"bok":      "Betrayers of Kamigawa",
	"chk":      "Champions of Kamigawa",
	"5dn":      "Fifth Dawn",
	"ds":       "Darksteel",
	"mi":       "Mirrodin",
	"sc":       "Scourge",
	"le":       "Legions",
	"on":       "Onslaught",
	"ju":       "Judgment",
	"tr":       "Torment",
	"od":       "Odyssey",
	"ap":       "Apocalypse",
	"ps":       "Planeshift",
	"in":       "Invasion",
	"pr":       "Prophecy",
	"ne":       "Nemesis",
	"mm":       "Mercadian Masques",
	"ud":       "Urza's Destiny",
	"ul":       "Urza's Legacy",
	"us":       "Urza's Saga",
	"ex":       "Exodus",
	"sh":       "Stronghold",
	"tp":       "Tempest",
	"wl":       "Weatherlight",
	"vi":       "Visions",
	"mr":       "Mirage",
	"hl":       "Homelands",
	"fe":       "Fallen Empires",
	"dk":       "The Dark",
	"lg":       "Legends",
	"aq":       "Antiquities",
	"an":       "Arabian Nights",
	"ori":      "Magic Origins",
	"m15":      "Magic 2015",
	"m14":      "Magic 2014 Core Set",
	"m13":      "Magic 2013",
	"m12":      "Magic 2012",
	"m11":      "Magic 2011",
	"m10":      "Magic 2010",
	"10e":      "Tenth Edition",
	"9e":       "Ninth Edition",
	"8e":       "Eighth Edition",
	"7e":       "Seventh Edition",
	"6e":       "Classic Sixth Edition",
	"5e":       "Fifth Edition",
	"4e":       "Fourth Edition",
	"rv":       "Revised Edition",
	"un":       "Unlimited Edition",
	"be":       "Limited Edition Beta",
	"al":       "Limited Edition Alpha",
	"vma":      "Vintage Masters",
	"me4":      "MTGO Masters Edition IV",
	"me3":      "MTGO Masters Edition III",
	"me2":      "MTGO Masters Edition II",
	"med":      "MTGO Masters Edition",
	"cns":      "Conspiracy",
	"pd3":      "Premium Deck Series: Graveborn",
	"pd2":      "Premium Deck Series: Fire and Lightning",
	"pds":      "Premium Deck Series: Slivers",
	"mm2":      "Modern Masters 2015 Edition",
	"md1":      "Modern Event Deck",
	"mma":      "Modern Masters",
	"dpa":      "Duels of the Planeswalkers",
	"ch":       "Chronicles",
	"c14":      "Commander 2014 Edition",
	"c13":      "Commander 2013 Edition",
	"cma":      "Commander's Arsenal",
	"pc2":      "Planechase 2012 Edition",
	"cmd":      "Commander",
	"arc":      "Archenemy",
	"pch":      "Planechase",
	"v14":      "From the Vault: Annihilation",
	"v13":      "From the Vault: Twenty",
	"v12":      "From the Vault: Realms",
	"fvl":      "From the Vault: Legends",
	"fvr":      "From the Vault: Relics",
	"fve":      "From the Vault: Exiled",
	"fvd":      "From the Vault: Dragons",
	"ddadvd":   "Duel Decks Anthology: Divine vs. Demonic",
	"ddaevg":   "Duel Decks Anthology: Elves vs. Goblins",
	"ddagvl":   "Duel Decks Anthology: Garruk vs. Liliana",
	"ddajvc":   "Duel Decks Anthology: Jace vs. Chandra",
	"ddo":      "Duel Decks: Kiora vs. Elspeth",
	"ddn":      "Duel Decks: Speed vs. Cunning",
	"ddm":      "Duel Decks: Jace vs. Vraska",
	"ddl":      "Duel Decks: Heroes vs. Monsters",
	"ddk":      "Duel Decks: Sorin vs. Tibalt",
	"ddj":      "Duel Decks: Izzet vs. Golgari",
	"ddi":      "Duel Decks: Venser vs. Koth",
	"ddh":      "Duel Decks: Ajani vs. Nicol Bolas",
	"ddg":      "Duel Decks: Knights vs. Dragons",
	"ddf":      "Duel Decks: Elspeth vs. Tezzeret",
	"pvc":      "Duel Decks: Phyrexia vs. The Coalition",
	"gvl":      "Duel Decks: Garruk vs. Liliana",
	"dvd":      "Duel Decks: Divine vs. Demonic",
	"jvc":      "Duel Decks: Jace vs. Chandra",
	"evg":      "Duel Decks: Elves vs. Goblins",
	"cstd":     "Coldsnap Theme Decks",
	"9eb":      "Ninth Edition Box Set",
	"8eb":      "Eighth Edition Box Set",
    # wtf is this crap
	#"dm":       "Deckmasters",
	#"bd":       "Beatdown Box Set",
	#"br":       "Battle Royale Box Set",
	#"at":       "Anthologies",
	#"mgbc":     "Multiverse Gift Box Cards",
	#"uh":       "Unhinged",
	#"ug":       "Unglued",
	#"uhaa":     "Unhinged Alternate Foils",
	#"st2k":     "Starter 2000",
	#"st":       "Starter 1999",
	#"p3k":      "Portal Three Kingdoms",
	#"po2":      "Portal Second Age",
	#"po":       "Portal",
	#"itp":      "Introductory Two-Player Set",
	#"ced":      "Collector's Edition",
	#"cedi":     "International Collectors' Edition",
	#"15ann":    "15th Anniversary",
	#"gpx":      "Grand Prix",
	#"pro":      "Pro Tour",
	#"mgdc":     "Magic Game Day Cards",
	#"wrl":      "Worlds",
	#"wmcq":     "World Magic Cup Qualifiers",
	#"drc":      "Dragon Con",
	#"ptc":      "Prerelease Events",
	#"rep":      "Release Events",
	#"mlp":      "Magic: The Gathering Launch Parties",
	#"sum":      "Summer of Magic",
	#"grc":      "WPN",
	#"cp":       "Champs",
	#"thgt":     "Two-Headed Giant Tournament",
	#"arena":    "Arena League",
	#"fnmp":     "Friday Night Magic",
	#"mprp":     "Magic Player Rewards",
	#"sus":      "Super Series",
	#"hho":      "Happy Holidays",
	#"jr":       "Judge Gift Program",
	#"pot":      "Portal Demogame",
	#"euro":     "European Land Program",
	#"guru":     "Guru",
	#"apac":     "Asia Pacific Land Program",
	#"wotc":     "WotC Online Store",
	#"uqc":      "Celebration Cards",
	#"clash":    "Clash Pack",
	#"mbp":      "Media Inserts",
	#"dcilm":    "Legend Membership"
}

card_file = open('no_lands.txt', 'r')
cards = card_file.read().split('\n')

#secrets
secret_file = open('mysql.secret', 'r')
secrets = secret_file.read().split('\n')
mysql_u = secrets[0]
mysql_p = secrets[1]
mysql_db = secrets[2]


try:
    con = sql.connect('localhost', mysql_u, mysql_p, mysql_db);
    cur = con.cursor()
        
    for edition in set_list:
        statement = 'INSERT INTO mtg_editions(acronym, full_name) VALUES("'+edition+'", "'+set_list[edition]+'")'
        print statement
        cur.execute(statement)
    
    sys.exit()        
        
    for card in cards:
        card = json.loads(card)
        statement = 'INSERT INTO mtg_card_lookup(name, edition, foreign_id, rarity) VALUES("'+str(card['name'])+'", "'+str(card['edition'])+'", '+str(card['foreign_id'])+', '+str(card['rarity'])+')'
        print statement
        cur.execute()
        
    sys.exit()

        
except sql.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
finally:    
    if con:    
        con.close()
    
