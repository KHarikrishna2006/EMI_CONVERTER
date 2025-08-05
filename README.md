# 🧮 EMI Calculator - Flask Web App

This is a simple **Loan EMI Calculator** built using **Python Flask**. The app takes in the **principal amount**, **annual interest rate**, and **loan duration (in years)** from the user and calculates the **Equated Monthly Installment (EMI)**. It also provides a basic breakdown of the monthly payments.

## 🚀 Features

- User-friendly web interface using **HTML/CSS**
- EMI calculation based on standard formula
- Built with **Flask**, a lightweight Python web framework
- Real-time result rendering after form submission

## 📷 Screenshot

> Add a screenshot here if available (e.g., main page or result display)

## 🛠️ Technologies Used

- Python 3.x
- Flask
- HTML/CSS (optional: Bootstrap for better UI)

## 📐 EMI Formula

The EMI is calculated using:

\[
EMI = \frac{P \times R \times (1 + R)^N}{(1 + R)^N - 1}
\]

Where:  
- `P` = Principal Loan Amount  
- `R` = Monthly Interest Rate = Annual Rate / 12 / 100  
- `N` = Total number of months = Years × 12  

## 📁 Project Structure

```
EMI_CONVERTER/
├── app.py                 # Main Flask app
├── templates/
│   └── index.html         # HTML form & result display
├── static/
│   └── style.css          # Optional CSS styling
└── README.md              # Project documentation
```

## ▶️ How to Run the App

### 1. Clone the repository

```bash
git clone https://github.com/KHarikrishna2006/EMI_CONVERTER.git
cd EMI_CONVERTER
```

### 2. Set up the virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies

```bash
pip install flask
```

### 4. Run the app

```bash
python app.py
```

Then open your browser and visit:  
👉 http://127.0.0.1:5000

## ✨ Example

**Input:**
- Principal: ₹1,00,000
- Interest Rate: 10% annual
- Duration: 2 years

**Output:**
- EMI: ₹4,614.46 per month

## 📌 To Do / Future Improvements

- Add pie chart showing interest vs principal
- Improve UI with Bootstrap
- Add support for currency formatting
- Save user input history (optional DB integration)

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License.
