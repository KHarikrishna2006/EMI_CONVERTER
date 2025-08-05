# EMI Calculator 💰📊

A simple and user-friendly **EMI (Equated Monthly Installment) Calculator** built using **Python Flask**. This tool helps users calculate monthly EMIs, total interest, and total payment based on the loan amount, interest rate, and loan duration.

---

## 🚀 Features

- Calculate EMI based on user inputs.
- Shows:
  - Monthly EMI
  - Total Interest Payable
  - Total Payment
- Clean and responsive user interface using HTML & CSS.
- Flask-powered backend for real-time calculation.

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS
- **Backend:** Python (Flask)

---

## 📸 Screenshots
<img width="1920" height="1008" alt="Screenshot 2025-08-05 213248" src="https://github.com/user-attachments/assets/36570927-3753-40c6-a5f9-8e4aa98f7cc8" />

)

---

## 🧮 Formula Used

```
EMI = [P × R × (1 + R)^N] / [(1 + R)^N – 1]
```

Where:
- **P** = Principal loan amount
- **R** = Monthly interest rate (Annual rate / 12 / 100)
- **N** = Loan tenure in months

---

## 📂 Project Structure

```
EMI_CONVERTER/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

---

## ▶️ Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KHarikrishna2006/EMI_CONVERTER.git
   cd EMI_CONVERTER
   ```

2. **Create a virtual environment (optional):**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install flask
   ```

4. **Run the Flask server:**
   ```bash
   python app.py
   ```

5. **Visit in browser:**
   ```
   http://127.0.0.1:5000
   ```

---

## 🙌 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🧑‍💻 Author

**K. Hari Krishna**

GitHub: [@KHarikrishna2006](https://github.com/KHarikrishna2006)
