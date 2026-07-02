class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'IV':'v','IX':'x','XL':'l','XC':'c','CD':'d','CM':'m'}
        replacements = [("IV", "v"), ("IX", "x"), ("XL", "l"), ("XC", "c"), ("CD", "d"), ("CM", "m")]
        for old,new in replacements:
            s = s.replace(old,new)
        roman_values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'v':4,'x':9,'l':40,'c':90,'d':400,'m':900}
        integer_total = sum(roman_values.get(numeral,0) for numeral in s)
        return integer_total
