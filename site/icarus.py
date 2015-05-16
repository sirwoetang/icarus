from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_home():
    return render_template('index.html')


@app.route('/map')
def render_map():
    return render_template('map.html')


@app.route('/charts')
def render_charts():
    return render_template('charts.html')


@app.route('/vehicle_table')
def render_vehicle():
    return render_template('vehicle_table.html')


@app.route('/fuel_table')
def render_fuel_table():
    return render_template('fuel_table.html')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
