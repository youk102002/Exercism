function collatz(number){
    result = number
    count = 0
  
    while (result > 1){
        if (result % 2 == 0){
            result = result / 2
        }else{
            result = (result * 3) + 1
        }
        count++
    }
    return count
}    
{
   # Vérifie si la valeur est un entier strictement positif (> 0)
    if ($0 !~ /^[1-9][0-9]*$/) {
        print "Error: Only positive integers are allowed" > "/dev/stderr"
        exit 1
    }

    print collatz($0)
}

