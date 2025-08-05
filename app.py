from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def emi_calculator():
    if request.method == 'POST':
        principal = float(request.form['principal'])
        annual_rate = float(request.form['rate'])
        years = int(request.form['years'])

        monthly_rate = annual_rate / 12 / 100
        months = years * 12

        emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
        total_payment = emi * months
        total_interest = total_payment - principal

        return render_template('index.html', emi=round(emi, 2), total_payment=round(total_payment, 2),
                               total_interest=round(total_interest, 2), principal=principal)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
