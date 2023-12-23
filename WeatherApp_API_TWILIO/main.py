import requests
from twilio.rest import Client

account_sid = 'ACa76db7f6398def1e248eb7540146c785'
auth_token = 'aee6ed778038751cf65e5da07a9ccbee'
client = Client(account_sid, auth_token)

params = {
    'q': 'yola',
    'appid': 'fc14f8bd3ab5d138b95bef45cf1d5fd3',
    'units': 'metric'
}


onecall_params = {
    'lon': '9.2095',
    'lat': '12.4782',
    'appid': 'fc14f8bd3ab5d138b95bef45cf1d5fd3',
    'units': 'metric',
    'exclude': 'current,minutely,daily'
}

onecall_url = 'https://api.openweathermap.org/data/2.5/onecall?'

url = 'https://api.openweathermap.org/data/2.5/weather?'

response = requests.get(onecall_url, params=onecall_params)

hourly_data = response.json()['hourly']
first_twelve_data = hourly_data[:13]

for data in first_twelve_data:
    if data['weather'][0]['id'] <= 800:
        print(data['weather'][0]['description'])
        print('bring umbrella')
        message = client.messages.create(
                            body="Come along with your umbrella",
                            from_='+18782016490',
                            to='+2348033333862'
                        )
        print(message)
        print(message.status)

#+18782016490


