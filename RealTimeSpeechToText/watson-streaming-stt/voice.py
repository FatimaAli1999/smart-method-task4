url = 'https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/ddab86f7-3536-4465-8b11-c2cfd1496797'
apikey = 'v5QKaIfX0OHTu-egfx1UKpr_arEeN4KQatf85mWLbEuz'

from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

with open('output.txt', 'r') as f:
	text = f.readlines()
	text = [line.replace('\n','') for line in text]
	text = ''.join(str(line) for line in text)


with open('./speech.mp3', 'wb') as audio_file:
	res = tts.synthesize(text,accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
	audio_file.write(res.content)
