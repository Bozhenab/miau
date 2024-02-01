with open("allnouns.txt", "r", encoding="utf-8") as r:
    with open("words5.txt", "w", encoding="utf-8") as w:
        for i in r:
            if len(i.strip()) == 5:
                w.write(i)