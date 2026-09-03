"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    seats = ["A","B","C","D"]
    for seat in range(number):
            yield seats[seat % 4]

def generate_row_numbers(number):
    """Génère la séquence des numéros de rangée en sautant la rangée 13."""
    row = 1
    count = 0
    while count < number:
        if row == 13:
            row = 14
        
        # Chaque rangée contient 4 sièges (A, B, C, D)
        for _ in range(4):
            if count >= number:
                break
            yield row
            count += 1
            
        row += 1

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    rows = generate_row_numbers(number)
    letters = generate_seat_letters(number)
    
    for row, letter in zip(rows, letters):
        yield f"{row}{letter}"
    
        
        


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seats = generate_seats(len(passengers))
    return dict(zip(passengers, seats))

    


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers :
        yield f"{seat}{flight_id}".ljust(12, "0")
