## Day 39: Flight Deal Finder  
Track flight prices for popular destinations and get SMS/WhatsApp alerts when a cheaper deal appears. Integrates **Amadeus Flight Offers**, **Sheety (Google Sheets)**, and **Twilio**.

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d39.py)  

### 🧠 Concepts Covered
- API keys & authentication (OAuth2 for Amadeus, bearer/basic for Sheety, SID/token for Twilio)  
- HTTP requests: GET/POST/PUT with query params and JSON payloads  
- Environment variables to protect secrets (`os.environ`)  
- Google Sheet automation via Sheety (read/write/update rows)  
- IATA **city** codes vs **airport** codes (use city IATA codes)  
- Flight search constraints (non-stop, round trip, 1 adult, date window, currency=GBP)  
- Data modeling: passing structured flight results between components  
- Notifications via Twilio (SMS/WhatsApp) with clear, concise deal messages  
- Rate-limit awareness and minimizing network calls  

### 📝 Instructions

#### `data_manager.py` — Google Sheets (Sheety)
1. **Configure endpoints & headers**  
   - Store your Sheety base endpoint (e.g., `SHEETY_PRICES_ENDPOINT`) and auth (Bearer/API key) in environment variables.  
   - Build common headers: `Authorization`, `Content-Type: application/json`.

2. **Fetch the sheet rows**  
   - `get_destination_data()`: `GET` the prices sheet; parse JSON to a list of dicts like:  
     ```python
     [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 200, 'id': 2}, ...]
     ```

3. **Fill missing IATA codes**  
   - `update_iata_codes(rows)`: for each row with empty `iataCode`, call `FlightSearch.get_iata_code(city)` and collect updates.

4. **Write updated codes back**  
   - `PUT` each row by `id` to set `iataCode`. Keep requests minimal (only when changed).

5. **(Optional) Users sheet**  
   - If you maintain a users sheet for multi-recipient alerts, add `get_users()` to `GET` that tab and return names/emails/phones.

6. **Design tips**  
   - Keep IO logic here; **don’t** mix in flight search or Twilio calls.  
   - Add lightweight logging and basic error handling (status codes, timeouts).

---

#### `flight_search.py` — Amadeus (IATA lookup & flight offers)
1. **Authenticate (OAuth2)**  
   - Read `AMADEUS_API_KEY` and `AMADEUS_API_SECRET`.  
   - `get_access_token()`: `POST` to Amadeus token endpoint to receive `access_token` and `expires_in`. Cache it until expiry.

2. **Get city IATA code**  
   - `get_iata_code(city_name)`:  
     - Call **City Search** (e.g., keyword query) and extract the **city** IATA code (not airport).  
     - Return something like `"PAR"`, `"NYC"`, `"TYO"`.

3. **Search flight offers**  
   - `search_flights(origin_city_code, dest_city_code, date_from, date_to)`  
     - Use **Flight Offers Search** with params:  
       - `originLocationCode=origin_city_code` (e.g., `LON`)  
       - `destinationLocationCode=dest_city_code`  
       - `departureDate=YYYY-MM-DD` (tomorrow)  
       - `returnDate=YYYY-MM-DD` (≤ ~6 months from now)  
       - `adults=1`  
       - `currencyCode=GBP`  
       - `nonStop=true`  
       - `max=1` (cheapest single offer)  
     - Parse response; pick the cheapest valid offer.

4. **Return structured data**  
   - Convert the chosen offer into a `FlightData` object (see below) with price, origin/destination cities & codes, out/return dates.

5. **Robustness**  
   - Retry once on token expiry (refresh token then repeat request).  
   - Guard against empty results/bad routes; return `None` for “no flights”.

---

#### `flight_data.py` — Structured result container
1. **Class purpose**  
   - Hold the minimal, clean details you need to compare and notify:  
     - `price` (int/float in GBP)  
     - `origin_city`, `origin_airport` (or city code)  
     - `destination_city`, `destination_airport` (or city code)  
     - `out_date`, `return_date` (ISO strings)  
     - (Optional) `deep_link` or `booking_url` if API provides

2. **Constructor & repr**  
   - Initialize all fields; implement a helpful `__repr__`/`__str__` for debugging logs.

3. **Immutability (optional)**  
   - Consider using `@dataclass(frozen=True)` for clarity and safety.

---

#### `notification_manager.py` — Twilio SMS/WhatsApp
1. **Configure Twilio client**  
   - Load `TWILIO_SID`, `TWILIO_AUTH_TOKEN`, and sender numbers (`TWILIO_FROM_SMS`, `TWILIO_FROM_WHATSAPP`) from environment variables.

2. **Compose message**  
   - Format a concise alert, e.g.:  
     ```
     ✈️ Low price alert! £{price}: {origin_city} → {destination_city}
     Dates: {out_date} → {return_date}
     Route: {origin_code} → {dest_code}
     ```
   - Keep it short; include core info first (price, route, dates).

3. **Send SMS**  
   - `send_sms(message, to_number)`: create a Twilio message with the SMS “from” number.

4. **Send WhatsApp**  
   - `send_whatsapp(message, to_number)`: use the `whatsapp:` prefixed sender/recipient.

5. **Error handling**  
   - Catch Twilio exceptions (invalid number, sandbox issues), log, and continue.

---

#### `main.py` — Orchestration
1. **Load config**  
   - Import modules; read all environment variables; set constants: `ORIGIN_CITY_CODE="LON"`, date window (tomorrow → +6 months).

2. **Init components**  
   - Create instances: `DataManager`, `FlightSearch`, `NotificationManager`.

3. **Pull sheet data**  
   - `destinations = data_manager.get_destination_data()`.  
   - If any row has missing `iataCode`, fetch via `FlightSearch.get_iata_code()` and `DataManager.update_iata_codes()`.

4. **Build date range**  
   - Compute `tomorrow` and `six_months_later` (e.g., `datetime.today() + timedelta(days=1)` and `+ 6*30`).

5. **Search flights per destination**  
   - For each destination:  
     - `flight = flight_search.search_flights("LON", dest['iataCode'], tomorrow, six_months_later)`  
     - If `flight` is `None`, skip.

6. **Compare & alert**  
   - If `flight.price < dest['lowestPrice']`:  
     - Compose message from `FlightData`.  
     - `notification_manager.send_sms(...)` (or WhatsApp).  
     - (Optional) Update the sheet’s `lowestPrice` with the new low.

7. **Minimize API usage**  
   - Only `PUT` rows that change.  
   - Limit destinations during testing (e.g., 5–10 rows) to respect free-tier limits.

8. **Run schedule (optional)**  
   - Add a daily runner (cron, Task Scheduler, GitHub Actions) to check deals automatically.

---

#### `steps.py` — (Optional) Project Checklist
- Quick reference of the above flow for manual verification while developing:
  1) Fill IATA codes → 2) Search flights → 3) Compare prices → 4) Notify → 5) (Optional) Update lowest price.

---

### 🔑 Environment Variables (example)
```bash
# Sheety
export SHEETY_PRICES_ENDPOINT="https://api.sheety.co/xxxxxx/flightDeals/prices"
export SHEETY_BEARER="Bearer your_sheety_token"

# Amadeus
export AMADEUS_API_KEY="your_amadeus_key"
export AMADEUS_API_SECRET="your_amadeus_secret"

# Twilio
export TWILIO_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export TWILIO_AUTH_TOKEN="your_twilio_auth"
export TWILIO_FROM_SMS="+1234567890"
export TWILIO_FROM_WHATSAPP="whatsapp:+14155238886"
export TWILIO_TO="+10987654321"           # or whatsapp:+...
```

### 💡 Tips & Gotchas

- Use city IATA codes (e.g., LON, PAR, NYC), not airport codes.
- Amadeus free tier doesn’t cover every route—test with popular cities.- 
- Sheety free tier ≈ 200 requests/month—only PUT when data changed.
- Log responses minimally; never print secrets.
