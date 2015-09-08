from bs4 import BeautifulSoup
import requests, sys

# card data: http://mag#ic#ca#rd#s.in#fo/frf/en/2.html
# card view: http://m#agi#cc#ar#ds.in#fo/sc#ans/en/frf/2.jpg

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
    # these don't seem desirable to have, necessarily.
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

def get_rarity_val(rarity):
    lookup = {
        "Mythic Rare": 5,
        "Rare":        4,
        "Uncommon":    3,
        "Common":      2,
        "Land":  1,
        "Special":     0
    }

    open = rarity.find('(') + 1
    close = rarity.find(')')
    rarity = rarity[open:close]
    # print '# ' + rarity
    rarity_val = lookup[rarity]
    
    return rarity_val 

def parse_card_info(card_info):
    bNext = False
    page = requests.get(card_info)
    html = page.text

    soup = BeautifulSoup(html, 'html.parser')
    
    #name = title element
    titles = soup.find_all("title")
    for t in titles:
        title = t.text
    open = title.find('(') - 1
    title = title[:open]
    
    #rarity = /html/body/table[3]/tbody/tr/td[3]/small/ -> bolded one
    columns = soup.find_all("table")
    col3 = columns[3]
    bold = col3.find_all("b")
    for b in bold:
        if bNext:
            rarity = b.text
            break
    
        if b.text == 'Editions:':
            bNext = True
    
    rarity_val = get_rarity_val(rarity)    
    
    return {"name": title, "rarity": rarity_val}

def does_url_200(url):
    print "# testing url: "+url
    page = requests.get(url)
    if page.status_code == 200:
        return True
        
    return False

def find_upper_limit(edition):
    upper = 500
    lower = 0

    found = False
    tries = 0
    
    ob = "ma"
    fu = "gic"
    sc = "car"
    at = "ds.i"
    ed = "nfo"
    
    obfuscated = ob + fu + sc + at + ed
    
    #BST
    while (1):
        tries = 1
        test_num = (lower + upper) / 2
        if test_num == lower:
            return test_num
        
        # print "Testing for the limit: " + str(lower) + " + " + str(upper) + " / 2 = " + str(test_num)
        test_url = "http://"+ obfuscated +"/scans/en/"+edition+"/"+ str(test_num) +".jpg"
        if does_url_200(test_url):
            #True = that card exists
            lower = test_num
        else:
            upper = test_num
            
    
for edition in set_list:
    highest = find_upper_limit(edition)

    ob = "ma"
    fu = "gic"
    sc = "car"
    at = "ds.i"
    ed = "nfo"
    
    obfuscated = ob + fu + sc + at + ed
    
    print "Testing "+str(highest)+" cards in "+edition
    for i in range(highest):

        if i == 0:
            continue
            
        #http://ma#gi#cc#ar#ds.i#nf#o/sca#ns/en/frf/2.jpg
        image_link = obfuscated+"/scans/en/"+edition+"/"+str(i)+".jpg"
        
        if not does_url_200(image_link):
            continue
        
        #card data: http://ma#gi#cca#rds.in#fo/frf/en/2.html
        card_info = obfuscated +"/"+edition+"/en/"+str(i)+".html"
        
        name_and_rarity = parse_card_info(card_info)
        
        name_and_rarity['edition'] = edition
        name_and_rarity['foreign_id'] = i
        print name_and_rarity
        
        
print "ALL DONE"
