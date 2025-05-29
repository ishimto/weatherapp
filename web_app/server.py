from pathlib import Path
import os
from datetime import date
from flask import Flask, render_template, request, redirect, url_for, send_file, Response
from backend_weather import GeoData
from modules.api_request import WeatherRequest
from modules.envs import *
#from server_logs import logs
import socket
from prometheus_client import generate_latest,  Counter, start_http_server
from UnleashClient import UnleashClient


start_http_server(5000) # Prometheus metrics - service discovery used in K8s

app = Flask(__name__)

city_requests_counter = Counter("city_requests",
                               "Count of weather requests per city",
                               ["city"]
                               )

@app.route('/', methods=["GET"])
def get_location():
    return render_template('index.html', bg_color=BG_COLOR)

@app.route('/version', methods=["GET"])
def version():
    return APP_VERSION


@app.route('/weather', methods=["POST"])
def weather():
    city = request.form["city"]
    amount_of_days = int(request.form["forecast_days"])
    weather_request = WeatherRequest(city=city, amount_of_days=amount_of_days)
    backend = GeoData(weather_request)

    if "error" in backend.json_response:
        return redirect(url_for('general_error', status=backend.status_code, error_message=backend.json_response["error"]["message"]))

    return render_template('weather.html', data=backend.data, amount_of_days=amount_of_days)


@app.route('/contact_us', methods=["POST", "GET"])
def contact_us():   
    if request.method == "GET":
        return render_template('contact_us.html')
    
    if request.method == "POST":
        email = request.form['user_email']
        subject = request.form['subject']
        message = request.form['user_message']
        logs.contact_logger.info(f"CONTACT MESSAGE FROM: {email}, SUBJECT: {subject}  MESSAGE: {message}")

    return redirect('/')


@app.route('/error')
def general_error():
    status = request.args.get('status')
    error_message = request.args.get('error_message')
    continue_message = "Press button below to return home and search again"
    return render_template('error.html', error_message=error_message, continue_message=continue_message), status


@app.errorhandler(404)
def page_not_found(error_message):
    continue_message = "Press button below to return home and search for forecast."
    return render_template('error.html', error_message=error_message, continue_message=continue_message), 404


@app.errorhandler(500)
def server_error(error_message):
    continue_message = "error in server, contact us to fix it. ishimto@contactus.com"
    return render_template('error.html', error_message=error_message, continue_message=continue_message), 500



@app.route('/metrics', methods=["GET"])
def metrics():
    return Response(generate_latest())


def is_enable_flag(FlagName):
    client = UnleashClient(
    url=FLAGS_URL,
    app_name=FLAGS_APP,
    instance_id=FLAGS_instanceID
    ) 

    client.initialize_client()
    return client.is_enabled(FlagName)


@app.route('/testflag', methods=["GET"])
def testflag():
    if is_enable_flag("test"):
        return "Flag Enabeld"
    else:
        return "Flag not enabled"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
