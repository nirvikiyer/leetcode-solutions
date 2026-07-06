class Solution:
    def intToRoman(self, num: int) -> str:
        
        result = ""
        str_num = str(num)
        
        if num >= 1000:
            thousand = int(str_num[0])
            result += "M" * thousand
            num -= thousand * 1000
            str_num = str(num)

        if num >= 100:
            hundred = int(str_num[0])
            if hundred >= 5:
                if hundred == 9:
                    result += "CM"
                else:
                    result += "D"
                    result += "C" * (hundred - 5)
            else:
                if hundred == 4:
                    result += "CD"
                else:
                    result += "C" * hundred
            num -= 100 * hundred
            str_num = str(num)
        
        if num >= 10:
            ten = int(str_num[0])
            if ten >= 5:
                if ten == 9:
                    result += "XC"
                else:
                    result += "L"
                    result += "X" * (ten - 5)
            else:
                if ten == 4:
                    result += "XL"
                else:
                    result += "X" * ten
            num -= 10 * ten
            str_num = str(num)
        
        if num >= 0:
            if num >= 5:
                if num == 9:
                    result += "IX"
                else:
                    result += "V"
                    result += "I" * (num - 5)
            else:
                if num == 4:
                    result += "IV"
                else:
                    result += "I" * num
        return result


