import sys

# card data: http://ma#gic#car#ds.in#fo/frf/en/2.html
# card view: http://mag#icc#ar#ds.in#fo/sca#ns/en/frf/2.jpg
ob = "http://ma"
fu = "gic"
sc = "car"
at = "ds.i"
ed = "nfo"
base = ob + fu + sc + at + ed

def generate_booster(edition):






def get_rarity_val(rarity):
    lookup = {
        "Mythic Rare": 5,
        "Rare":        4,
        "Uncommon":    3,
        "Common":      2,
        "Land":        1,
        "Special":     0
    }

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
    
    #BST
    while (1):
        tries = 1
        test_num = (lower + upper) / 2
        if test_num == lower:
            return test_num
        
        # print "Testing for the limit: " + str(lower) + " + " + str(upper) + " / 2 = " + str(test_num)
        test_url = base + "/scans/en/"+edition+"/"+ str(test_num) +".jpg"
        if does_url_200(test_url):
            #True = that card exists
            lower = test_num
        else:
            upper = test_num
            
    
for edition in set_list:
    highest = find_upper_limit(edition)

    print "Testing "+str(highest)+" cards in "+edition
    for i in range(highest):

        if i == 0:
            continue
            
        #http://ma#gic#car#ds.in#fo/scans/en/frf/2.jpg
        image_link = base+"/scans/en/"+edition+"/"+str(i)+".jpg"
        
        if not does_url_200(image_link):
            continue
        
        #card data: http://ma#gic#ca#rds.in#fo/frf/en/2.html
        card_info = base+"/"+edition+"/en/"+str(i)+".html"
        
        name_and_rarity = parse_card_info(card_info)
        
        name_and_rarity['edition'] = edition
        name_and_rarity['foreign_id'] = i
        print name_and_rarity
        
        
print "ALL DONE"
