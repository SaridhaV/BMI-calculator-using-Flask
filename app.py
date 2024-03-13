from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_bmi():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    height_unit = request.form['height_unit']
    weight_unit = request.form['weight_unit']

    if height_unit == 'cm':
        height /= 100  # Convert cm to meters

    if weight_unit == 'lbs':
        weight *= 0.453592  # Convert pounds to kilograms

    bmi = weight / (height ** 2)
    return render_template('result.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)
