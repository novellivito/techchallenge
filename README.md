# techchallenge
(English)

Follow this procedure to successfully start the app.

BACKEND

- Make sure you have Python 3.12 installed on your computer.
- Open a terminal and navigate to the backend folder.
- Create a virtual environment (venv) with the command: `python -m venv techchallenge-venv`
- Activate the virtual environment with the command: `techchallenge-venv\Scripts\activate` for Windows, `techchallenge-venv\bin\activate` for macOS.
- Install all dependencies with this command: `pip install -r requirements.txt`
- Start the execution of the file with the command: `python main.py`
- The backend will respond on port 8000 (e.g., http://127.0.0.1:8000); available endpoints:

  - http://127.0.0.1:8000/api/v1/products_day
  - http://127.0.0.1:8000/api/v1/products_avg_month
  - http://127.0.0.1:8000/api/v1/products_avg_year

FRONTEND

- Ensure Node.js is installed on your computer.
- Open a terminal and navigate to the frontend-app folder.
- Install all dependencies with the command: `npm install`
- Launch the application with the command: `ng serve -o`


(italian)

Segui questa procedura per avviare correttamente l'app.

BACKEND

- Assicurati di avere installato Python 3.12 sul tuo computer.
- Apri un terminale e posizionati nella cartella backend.
- Crea un ambiente virtuale (venv) con il comando: `python -m venv techchallenge-venv`
- Attiva l'ambiente virtuale con il comando: `techchallenge-venv\Scripts\activate` per Windows, `techchallenge-venv\bin\activate` per macOS.
- Installa tutte le dipendenze con questo comando: `pip install -r requirements.txt`
- Avvia l'esecuzione del file con il comando: `python main.py`
- Il backend risponderà sulla porta 8000 (es. http://127.0.0.1:8000); endpoint disponibili:

  - http://127.0.0.1:8000/api/v1/products_day
  - http://127.0.0.1:8000/api/v1/products_avg_month
  - http://127.0.0.1:8000/api/v1/products_avg_year

FRONTEND

- Assicurati di avere installato Node.js sul tuo computer.
- Apri un terminale e posizionati nella cartella frontend-app.
- Installa tutte le dipendenze con il comando: `npm install`
- Avvia l'applicazione con il comando: `ng serve -o`