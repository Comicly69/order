import ccard
import random
import string

print ("VISA:" + ccard.visa())
print ("MASTER:" + ccard.mastercard())
print ("AMEX:" + ccard.americanexpress())
print ("DISCOVER:" + ccard.discover())
genisis = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
print ("Gensis ID:" + genisis)