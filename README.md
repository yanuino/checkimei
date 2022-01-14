# checkimei
Use Luhn formula to check IMEI



## Luhn formula
Source: https://en.wikipedia.org/wiki/Luhn_algorithm

The check digit is computed as follows:

1) Take the original number and starting from the rightmost digit moving left, double the value of every second digit (including the rightmost digit).
2) Replace the resulting value at each position with the sum of the digits of this position's value.
3) Sum up the resulting values from all positions (s).
4) The calculated check digit is equal to `10 − s mod 10`.

## Pseudocode implementation
```
function checkLuhn(string purportedCC) {
    int nDigits := length(purportedCC)
    int sum := integer(purportedCC[nDigits-1])
    int parity := (nDigits-1) modulus 2
    for i from 0 to nDigits - 2 {
        int digit := integer(purportedCC[i])
        if (i+1) modulus 2 = 0
            digit := digit × 2
        if digit > 9
            digit := digit - 9 
        sum := sum + digit
    }
    return (sum modulus 10) = 0
}
```
