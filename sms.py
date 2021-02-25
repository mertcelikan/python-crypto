import nexmo
import apikeys

phoneNumber = '905309580353'
textMSJ = ''

client = nexmo.Client(key=apikeys.smsKEY, secret=apikeys.smsSECRET)

client.send_message({
    'from': 'Vonage APIs',
    'to': phoneNumber,
    'text': 'Hello from Vonage SMS API',
})

