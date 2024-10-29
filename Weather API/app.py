from flask import Flask, jsonify, request, render_template
import requests

app = Flask('Weather Dashboard')

API_KEY = '7ab4f879ef0804ca67aa589e96c78e27'

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather', methods = ['GET'])
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'})
    weather_data = get_weather_data(city)
    if weather_data.get('cod') != 200:
        return jsonify({'error': 'City not found'}), 404
    return jsonify({
        'city': weather_data['name'],
        'temperature' : weather_data['main']['temp'],
        'description': weather_data['weather'][0]['description'],
        'humidity' : weather_data['main']['humidity']
    })

if __name__ == '__main__':
    app.run(debug=True)