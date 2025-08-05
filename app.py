from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_emi(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    total_payment = emi * months
    total_interest = total_payment - principal
    return round(emi, 2), round(total_payment, 2), round(total_interest, 2)

@app.route('/', methods=['GET', 'POST'])
def emi_calculator():
    if request.method == 'POST':
        try:
            principal = float(request.form['principal'])
            annual_rate = float(request.form['rate'])
            years = int(request.form['years'])

            emi, total_payment, total_interest = calculate_emi(principal, annual_rate, years)

            return render_template('index.html',
                                   emi=emi,
                                   total_payment=total_payment,
                                   total_interest=total_interest,
                                   principal=principal)
        except (ValueError, ZeroDivisionError):
            return render_template('index.html', error="Invalid input. Please enter valid numeric values.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
