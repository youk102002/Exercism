BEGIN {
    # Définir les séparateurs de mots : espaces, tirets et caractères de contrôle
    FS = "[- \t]+"
}

{
    acronym = ""
    for (i = 1; i <= NF; i++) {
        # Nettoyer le mot en retirant la ponctuation (garde uniquement lettres et chiffres)
        gsub(/[^a-zA-Z0-9]/, "", $i)
        
        # Si le mot n'est pas vide, extraire la première lettre et la mettre en majuscule
        if ($i != "") {
            acronym = acronym toupper(substr($i, 1, 1))
        }
    }
    print acronym
}