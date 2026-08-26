BEGIN {
    # define the field separator
    FS = ","
}

{
    # generate and print the output for each record
    print "#"$1 ", " $2 " =" , (($3 $4) + ($5 $6)) / 2 
}
