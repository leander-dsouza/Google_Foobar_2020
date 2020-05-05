import base64

MESSAGE = '''
F0ISGwcGFxcASFVAQRZVQVENEUZCREIRCx8DEBsGRFcUFFZFRgsXERcBHgoRXU0RFVZSCgoTGhdC Ul5TSBwUAkNXV10OCQRJSEVVBRAHHB8XVF9WWhhCQVREQgcKHwAWEQRVFR8USxcADAYMBhdUT09a RkJTVVFLSUFJAgodQ1NVVV0WWFwSExE=
''' #<encrypted>''</encrypted>

KEY = 'leanderdsouza1234' #your username

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))

#OUTPUT
#{'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}

