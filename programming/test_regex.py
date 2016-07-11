import re

def validate_phone_number(number):
    if re.match(r'^01[0167899][1-9]\d{6,7}$', number): #r = the shorterm of 'raw'
        return True
    return False

print(validate_phone_number('01012345666'))
print(validate_phone_number('0101233'))
print(validate_phone_number('2ldndsk'))