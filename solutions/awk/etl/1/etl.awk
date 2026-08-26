BEGIN {
    FS = "[:,\"\t ]+"
}

{
    score = $1
    for (i = 2; i <= NF; i++) {
        gsub(/[^a-zA-Z]/, "", $i)
        if ($i != "") {
            score_map[tolower($i)] = score
        }
    }
}

END {
    # Parcourt l'alphabet de 'a' à 'z' dans l'ordre
    for (code = 97; code <= 122; code++) {
        lettre = sprintf("%c", code)
        if (lettre in score_map) {
            print lettre "," score_map[lettre]
        }
    }
}