PARTS = [
    ("house that Jack built.", ""),
    ("malt", "lay in the "),
    ("rat", "ate the "),
    ("cat", "killed the "),
    ("dog", "worried the "),
    ("cow with the crumpled horn", "tossed the "),
    ("maiden all forlorn", "milked the "),
    ("man all tattered and torn", "kissed the "),
    ("priest all shaven and shorn", "married the "),
    ("rooster that crowed in the morn", "woke the "),
    ("farmer sowing his corn", "kept the "),
    ("horse and the hound and the horn", "belonged to the "),
]


def build_verse_body(index):
    """Construit récursivement les vers d'une strophe avec des sauts de ligne."""
    if index == 0:
        return PARTS[0][0]

    subject, action = PARTS[index]
    return f"{subject} that {action}" + build_verse_body(index - 1)


def recite(start_verse, end_verse):
    """Retourne la liste des strophes de start_verse à end_verse."""
    verses = []

    for verse_num in range(start_verse - 1, end_verse):
        header = "This is the "
        body = build_verse_body(verse_num)
        verses.append(header + body)

    return verses