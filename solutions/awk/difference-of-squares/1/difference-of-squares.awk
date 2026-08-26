BEGIN{ FS = "," }
# cas square_of_sum
function square_of_sum(number){
    sum = 0
    for (i = 1; i <= number; i++){
        sum = sum + i
    }
    return (sum^2)
}

# cas sum_of_squares
function sum_of_squares(number){
    sum = 0 
    for (i = 1; i <= number; i++){
        sum = sum + (i^2)
    }
    return (sum)
}

# difference
function difference(number){
    return square_of_sum(number) - sum_of_squares(number)
}

$1 == "square_of_sum"{
    print square_of_sum($2)
}
$1 == "sum_of_squares"{
    print sum_of_squares($2)
}
$1 == "difference"{
    print difference($2)
}