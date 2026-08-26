BEGIN {
    FS = ","    # comma is the field separator
}

# Task 1: When the first field is "needs_license",
#         print "true" if the second field contains "car" or "truck".
$1 == "needs_license" {
    print ($2 ~ /car|truck/ ? "true" : "")
}

# task 2 :
$1 == "resell_price" {
    original_price = $2
    age = $3

    if (age < 3) {
        factor = 0.8
    } else if (age <= 10) {
        factor = 0.7
    } else {
        factor = 0.5
    }

    print original_price * factor
}