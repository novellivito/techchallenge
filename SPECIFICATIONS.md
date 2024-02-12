### Specifiche Tecniche del Progetto:

#### Backend (FastAPI):

1. **Framework Utilizzato:**
   - Il backend è sviluppato in Python utilizzando il framework FastAPI per la gestione delle API.
   - FastAPI è scelto per la sua alta performance, facilità di sviluppo e supporto nativo per la programmazione asincrona.

#### Gestione Dati con Pandas:

1. **Libreria Utilizzata:**
   - La gestione dei dati è implementata utilizzando la libreria Pandas.
   - Pandas è scelto per la sua potenza e versatilità nella manipolazione e analisi dei dati tabulari.

2. **Caricamento Iniziale e Cache:**
   - Il file CSV (data.csv) viene caricato al primo utilizzo attraverso il metodo `load_data` della classe `DataService`.
   - Per evitare di rielaborare i dati ad ogni chiamata, sono implementati oggetti cache come `product_day`, `product_month`, e `product_year`.

#### Struttura del Backend (dataservice.py):

1. **Classe DataService:**
   - La classe DataService gestisce il dominio dei dati dell'applicazione.
   - Implementa funzioni per il caricamento iniziale dei dati, calcoli specifici sui dati, e la gestione di oggetti cache.

2. **Calcolo dei Prodotti:**
   - Le funzioni `calc_products_day_count`, `calc_products_month`, e `calc_products_year` eseguono calcoli specifici sui dati per ottenere conteggi giornalieri, medie mensili e medie annuali dei prodotti.

3. **FilterBuilder:**
   - La classe FilterBuilder è implementata per la costruzione dinamica di filtri basati sui parametri di ricerca come factory, area, anno, mese, e giorno.

#### Main.py (Endpoint API con FastAPI):

1. **Endpoint API:**
   - Sono implementati tre endpoint principali per ottenere dati relativi ai prodotti giornalieri, mensili e annuali.
   - Gli endpoint accettano parametri opzionali per filtrare i dati in base a factory, area, anno, mese, e giorno.

2. **CORS Middleware:**
   - Il middleware CORS è utilizzato per gestire le richieste cross-origin, consentendo l'accesso alle risorse API da origini specifiche.

3. **Avvio del Server:**
   - Il server FastAPI è avviato utilizzando l'istanza di uvicorn con l'host e la porta specificati.

4. **Gestione dell'Autenticazione:**
   - FastAPI consente la gestione dell'autenticazione, ad esempio attraverso l'implementazione di route protette con token JWT.

5. **Gestione del Routing:**
   - La struttura del routing è mantenuta semplice inizialmente, ma può essere estesa in futuro per gestire una crescente complessità dell'applicazione.

Queste specifiche tecniche aggiornate includono la possibilità di sviluppare la gestione dell'autenticazione con FastAPI e la possibilità di estendere la gestione del routing in futuro, se necessario.


#### Frontend (Angular):

- **Framework Frontend**: Angular
- **Libreria UI**: Angular Material

### Struttura del Progetto:

1. **Modulo Dashboard con Routing**:
   - Il modulo Dashboard deve gestire le route relative alla dashboard.

2. **Componente Dashboard**:
   - Contiene la struttura della dashboard, composta da:
     - Header
     - Sidenav
     - Content

3. **DashboardService**:
   - Service responsabile della comunicazione con il backend FastAPI.

4. **Componente ProductsDay**:
   - Visualizza i dati letti dal backend (route: `/products-day`).
   - Implementa la paginazione e tutti i filtri utente:
     - Factory
     - Area
     - Year
     - Month
     - Day

### Comunicazione Frontend-Backend:

- Il servizio `DashboardService` dovrebbe gestire la comunicazione HTTP con il backend FastAPI, includendo le chiamate necessarie per ottenere i dati di ProductsDay.

### Paginazione:

- Implementato un sistema di paginazione nel componente ProductsDay per la visualizzazione dei dati.

### Filtri Utente:

- Implementati filtri utente nel componente ProductsDay per i seguenti criteri:
  - Factory
  - Area
  - Year
  - Month
  - Day

