## Day 40: Flight Club  
An upgraded version of the **Flight Deal Finder** project. 
This version adds a customer sign-up system via a Google Form, supports indirect flights, and sends email notifications in addition to SMS alerts.  

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d40.py)  

---

### 🧠 Concepts Covered
- API requests, responses, parameters  
- Sheety API integration for multiple sheets (`prices` and `users`)  
- Amadeus API for flight offers (direct & indirect flights)  
- Environment variable management with `.env`  
- Sending SMS/WhatsApp alerts using Twilio  
- Sending emails with `smtplib` and SMTP servers  
- Object-Oriented Programming with multiple classes  
- Handling multiple API endpoints and authentication  

---

### 📝 Instructions

#### Step 1 - Create a Google Form for Customer Signups
1. Open **Google Drive**, right-click, and create a new **Google Form**.  
2. Add fields to collect:  
   - First Name  
   - Last Name  
   - Email  
3. Disable **limit to 1 response** and email collection for easier testing.  
4. Link the form to your existing **Flight Deals Google Sheet**.  
5. Rename the new response tab to `users`.  
6. Submit some test data to verify it appears in the sheet.

---

#### Step 2 - Configure Sheety for User Data
1. Log into **Sheety** and re-sync your Google Sheet.  
2. Ensure that both tabs (`prices` and `users`) appear.  
3. Enable `POST` requests for adding new users and `PUT` requests for updating data.  
4. Save endpoints for both tabs in your `.env` file as:  
   - `SHEETY_PRICES_ENDPOINT`  
   - `SHEETY_USERS_ENDPOINT`

---

#### Step 3 - Populate IATA Codes
1. Use the Amadeus API to retrieve city-level IATA codes for each destination.  
2. Update the `prices` sheet with IATA codes automatically via Sheety API.

---

#### Step 4 - Search for Cheap Flights
1. Query flights from **London (LON)** to each listed destination.  
2. Parameters:  
   - Round trip  
   - Currency: GBP  
   - Dates: Tomorrow → 6 months from now  
   - Adults: 1  
3. Compare flight prices with those listed in the `prices` sheet.

---

#### Step 5 - Handle Indirect Flights
1. Modify `check_flights()` in `FlightSearch` to accept a `is_direct` parameter (default `True`).  
2. If no direct flights are found, retry search with `is_direct=False`.  
3. Update `FlightData` class to include a `stops` attribute for stopover flights.  
4. Always display the **final destination airport code**, not just stopover airports.

---

#### Step 6 - Retrieve Customer Emails
1. Create `get_customer_emails()` in `DataManager` to fetch emails from the `users` sheet.  
2. Store these emails in a list for notifications.

---

#### Step 7 - Send Notifications
1. Send SMS/WhatsApp alerts using Twilio.  
2. Send email notifications to all customers using `smtplib`.  
3. Store SMTP credentials (`SMTP_ADDRESS`, `EMAIL`, `APP_PASSWORD`) in `.env`.  
4. Adjust message content to indicate whether a flight is **direct or indirect**.

---

### 📦 Classes Overview

#### `DataManager`
Handles all interactions with Google Sheets via Sheety API.  
- `get_destination_data()` → Fetches all data from `prices` sheet.  
- `update_destination_codes()` → Updates IATA codes for destinations.  
- `get_customer_emails()` → Retrieves user emails from `users` sheet.

---

#### `FlightSearch`
Communicates with the Amadeus API for city codes and flight data.  
- `get_destination_code(city)` → Returns IATA code for a given city.  
- `check_flights(origin, destination, from_time, to_time, is_direct=True)` → Returns flight data.  

---

#### `FlightData`
Data model for each flight deal. Stores:  
- Price  
- Origin city & airport  
- Destination city & airport  
- Outbound date & return date  
- Stopover information (if any)

---

#### `NotificationManager`
Manages communication with users via SMS and email.  
- `send_sms(message)` → Sends SMS/WhatsApp alerts using Twilio.  
- `send_emails(emails, message)` → Sends emails with flight deals to all users.

---

#### `main.py` (Workflow)
1. Fetch destination data from `prices` sheet.  
2. Populate missing IATA codes.  
3. Search for cheapest flights (direct first, then indirect).  
4. Notify all customers via SMS and email if prices are below target.  

---

### 🔑 Environment Variables
Store these variables in a `.env` file for security:  
- `SHEETY_PRICES_ENDPOINT`  
- `SHEETY_USERS_ENDPOINT`  
- `AMADEUS_API_KEY`  
- `AMADEUS_API_SECRET`  
- `TWILIO_ACCOUNT_SID`  
- `TWILIO_AUTH_TOKEN`  
- `TWILIO_PHONE_NUMBER`  
- `SMTP_ADDRESS`  
- `EMAIL`  
- `APP_PASSWORD`

---

💡 **Extra Challenges**:
- Schedule this script to run daily using cron or Windows Task Scheduler.  
- Add support for multiple origin airports.  
- Send push notifications using another API (e.g., Pushover).  
- Display deals in a simple web dashboard.

---
