### Specifiche Tecniche del Progetto:

Breve descrizione del progetto realizzato 

Seguendo quanto richiesto nella traccia, è stata realizzata un web-application che svolge i task richiesti .

L'applicazione si divide in due progetti, ovvero backend e frontend .

Per il backend è stato utilizzato il framework FastAPI per l'implementazione degli endpoint REST, mentre per la gestione dei dati, contenuti nel file data.csv, è stata utilizzata la libreria pandas .

Non si è considerato di utilizzare database sql o relativi framework (SqlAlchemy) perchè non vi era evidente vantaggio .
Non si è consierato di implementare un servizio di autenticazione perchè non richiesto. Sarebbe stato possibile tramite FastAPI tramite ad esempio OAuth2 .

Per il frontend è stato utilizzato il framework angular, con l'implementazione material per l'UI 

Di seguito una descrizione più completa

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

2. **Funzioni di calcolo:**
   - Le funzioni `calc_products_day_count`, `calc_products_month`, e `calc_products_year` eseguono calcoli specifici sui dati per ottenere conteggi giornalieri, medie mensili e medie annuali dei prodotti.
   - tutte le funzioni eseguono l'elaborazione iniziale, salvando i dati in oggetti cache, evitando ulteriori elaborazioni inutili, data la presenza di dati statici.

3. **FilterBuilder:**
   - La classe FilterBuilder è implementata per la costruzione dinamica di filtri basati sui parametri di ricerca come factory, area, anno, mese, e giorno.

#### Main.py (Endpoint API con FastAPI):

1. **Endpoint API:**
   - Sono implementati tre endpoint principali per ottenere dati relativi ai prodotti giornalieri, mensili e annuali.
   - Gli endpoint accettano parametri opzionali per filtrare i dati in base a factory, area, anno, mese, e giorno.
   - tutti gli endpoint gestiscono la paginazione tramite i parametri skip e limit

2. **CORS Middleware:**
   - Il middleware CORS è utilizzato per gestire le richieste cross-origin, consentendo l'accesso alle risorse API da origini specifiche.

3. **Avvio del Server:**
   - Il server FastAPI è avviato utilizzando l'istanza di uvicorn con l'host e la porta specificati.

4. **Gestione dell'Autenticazione (NON IMPLEMENTATA):**
   - FastAPI consente la gestione dell'autenticazione, ad esempio attraverso l'implementazione di route protette con token JWT.

5. **Gestione del Routing (NON IMPLEMENTATA):**
   - La struttura del routing è mantenuta semplice inizialmente, ma può essere estesa in futuro per gestire una crescente complessità dell'applicazione.


#### Frontend (Angular):

- **Framework Frontend**: Angular
- **Libreria UI**: Angular Material

### Struttura del Progetto:

1. **Modulo Dashboard con Routing**:
   - Il modulo Dashboard implementa un routing proprio, diverso da quello dell'applicazione principale . Questa scelta è stata operata in funzione di potenziali sviluppi futuri, ponendo le basi per un routing scalabile e organizzato.

2. **Componente DashboardComponent**:
   - Contiene la struttura della dashboard, composta da:
     - Header
     - Sidenav
     - Content

3. **DashboardService**:
   - Service responsabile della comunicazione con il backend FastAPI. Sono implementate le seguenti funzioni :
      - getProductsDay : esegue una GET all'endpoint `products_day` del backend, tramite parametri opzionali per filtrare i risultati e ottenere un set limitato di dati 
      - getProductsAvgMonth : esegue una GET all'endpoint `products_avg_month` del backend, tramite parametri opzionali per filtrare i risultati e ottenere un set limitato di dati 
      - getProductsAvgYear : esegue una GET all'endpoint `products_avg_year` del backend, tramite parametri opzionali per filtrare i risultati e ottenere un set limitato di dati 

4. **Componente ProductsDayComponent**:
   - Visualizza i dati letti dal backend (route: `/products-day`).
   - Implementa la paginazione e tutti i filtri utente:
     - Factory
     - Area
     - Year
     - Month
     - Day

5. **Componente ProductsAvgMonthComponent**:
   - Visualizza i dati letti dal backend (route: `/products-avg-month`).
   - Implementa la paginazione e tutti i filtri utente:
     - Factory
     - Area
     - Year
     - Month

6. **Componente ProductsAvgYearComponent**:
   - Visualizza i dati letti dal backend (route: `/products-avg-month`).
   - Implementa la paginazione e tutti i filtri utente:
     - Factory
     - Area
     - Year
     
