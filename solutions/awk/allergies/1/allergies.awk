BEGIN {
    items[1] = "eggs"
    items[2] = "peanuts"
    items[3] = "shellfish"
    items[4] = "strawberries"
    items[5] = "tomatoes"
    items[6] = "chocolate"
    items[7] = "pollen"
    items[8] = "cats"

    FS = ","
}
$2 == "allergic_to" {
    score = $1
    target_item = $3
    is_allergic = "false"

    for(i = 1; i <= 8; i++){
        valeur = 2^(i-1)
        
        if (and(score, valeur) && items[i] == target_item){
            is_allergic = "true"
            break
        }        
    }
    print is_allergic
}
$2 == "list"{
    score = $1
    allergies = ""

    for (i =1 ; i <=8; i++){
        valeur = 2^(i-1)
        if(and(score,valeur)){
            allergies = (allergies == "" ? items[i]:allergies "," items[i])
        }
    }
    print allergies
}
