"""
Flatonacci secuence is a secuence which is result from the same given secuence 
plus the sum of the last 3 numbers of the secuence. 

The challenge is to create a flatonacci function that given a signature returns the first 
n elements - signature included of the so seeded sequence. So, if we are to 
start our Flatonacci sequence with [1, 1, 1] as a starting input (AKA signature) and n = 8,
we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31]

Another example; if signature is the secuence [0, 0, 1] we should get some thing
like:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]

- Signature will always contain 3 numbers 
- n will always be a non-negative number
- if n == 0, then return an empty list and be ready for anything else which is not
clearly specified ;)

Note. Please note that we are gonna test the funcion against a lot of different signatures and n's
"""

def validate_input(signature: list, n: int) -> None:

    if len(signature) != 3:
        raise ValueError(f'Flatonacci needs a signature of 3 numbers, you provided {len(signature)} numbers.')

    if not all( (isinstance(number, int) or isinstance(number, float)) for number in signature):
        raise ValueError(f'Flatonacci only accepts numbers for signature values, you provided {signature}')

    if not isinstance(n, int):
        raise ValueError(f'Flatonacci only accepts integer numbers for n, you provided {n}')

    if n < 0:
        raise ValueError(f'Flatonacci needs a non-negative number for n, you provided {n}.')

    
    
def flatonacci(signature: list, n: int) -> list:
    validate_input(signature, n)
    sequence = []
    added_numbers = int()

    if n == 0:
        return []
    else:
        sequence = [s for s in signature]
        if n >= len(signature):
            added_numbers = n - len(signature)
        else:
            added_numbers = n

    for s in range(added_numbers):
        sequence.append(sum(sequence[-3:]))
    
    return sequence