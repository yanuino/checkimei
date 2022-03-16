class CheckIMEI():
    def __init__(self, purportedCC):
        self.purportedCC = purportedCC

        self.nDigits = len(self.purportedCC)
        self.sumDigit = int(self.purportedCC[self.nDigits-1])
        parity =(self.nDigits-1) % 2
        print('Len: {}, Sum: {}, Parity: {}'.format(self.nDigits, self.sumDigit, parity))


    def split(self):
        print('IMEI: {}'.format(self.purportedCC))
        print('TAC: {}'.format(self.purportedCC[0:8]))
        print('SNR: {}'.format(self.purportedCC[8:14]))
        print('CD: {}'.format(self.purportedCC[14]))

    def checkLuhn(self):
        luhn = 0
        for i in range(self.nDigits - 1):
            digit = int(self.purportedCC[i])
            if ((i+1)%2) == 0:
                digit = digit * 2
                if digit > 9:
                    digit = digit - 9
            luhn = luhn + digit
        luhn = 10 - luhn % 10
        return luhn == self.sumDigit

    
if __name__ == '__main__':
    check = CheckIMEI('865336041527575')
    check.split()
    print(check.checkLuhn())
    check = CheckIMEI('865336041527567')
    check.split()
    print(check.checkLuhn())
    