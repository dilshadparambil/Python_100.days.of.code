## Day 66: Café & Wifi REST API ☕💻  

In this project, I created a **RESTful API** for managing café data using **Flask** and **SQLAlchemy**.  
The API supports all the core **CRUD operations** (`GET`, `POST`, `PATCH`, `DELETE`) and allows developers to interact with a café database programmatically.  
All endpoints were tested and documented using **Postman**, and a public documentation link is provided for reference.  

📄 [View My Code](my_code/d66.py)  📄 [View Solution](solution/solution.py) 
📄 [View My Html](my_code/templates/index.html)  📄 [View Solution Html](solution/templates/index.html) 
📄 [API Documentation](https://documenter.getpostman.com/view/48698162/2sB3QCRCs8)  

---

### 🧠 Concepts Covered
- **RESTful API principles**: resource-based URLs, proper use of HTTP verbs.  
- **GET** → Retrieve cafés (random, all, or by location).  
- **POST** → Add a new café entry (secured with API key).  
- **PATCH** → Update specific café details (e.g., coffee price).  
- **DELETE** → Remove a café entry (requires API key).  
- **Postman API Testing**: validating endpoints with different inputs and scenarios.  
- **Postman Documentation**: sharing API usage instructions in a standardized format.  
- **SQLAlchemy ORM**: defining models, creating tables, and executing queries.  
- **Serialization to JSON**: converting SQLAlchemy models to dictionaries for API responses.  
- **Error Handling**: custom JSON responses with appropriate HTTP status codes (403, 404).  

---

### 📝 Instructions

#### 1. **Setup & Installation**
1. Clone the project or copy the code.  
2. Install dependencies from `requirements.txt`:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask server:  
   ```bash
   python d66.py
   ```
4. The API will be available at `http://127.0.0.1:5000/`.  

#### 2. **Database Schema**
The SQLite database `cafes.db` contains one table: **Cafe**.  

| Field          | Type     | Description                              |
|----------------|----------|------------------------------------------|
| id             | Integer  | Primary key (auto-increment).            |
| name           | String   | Name of the café (unique, required).     |
| map_url        | String   | Google Maps link to the café.            |
| img_url        | String   | Image link of the café.                  |
| location       | String   | City or area where café is located.      |
| seats          | String   | Seating capacity description.            |
| has_toilet     | Boolean  | Availability of restroom.                |
| has_wifi       | Boolean  | Availability of Wi-Fi.                   |
| has_sockets    | Boolean  | Availability of power sockets.           |
| can_take_calls | Boolean  | Whether phone calls can be taken.        |
| coffee_price   | String   | Average coffee price (e.g., `£2.50`).    |

---

### 📌 API Endpoints

#### **1. Home Route**
`GET /`  
- Displays a welcome page with a link to Postman docs.  

---

#### **2. Get Random Café**
`GET /random`  
- Returns details of a random café.  

✅ Example Response:
```json
{
  "cafe": {
    "id": 3,
    "name": "Old Harbour Cafe",
    "map_url": "https://goo.gl/maps/12345",
    "img_url": "https://images.com/cafe.jpg",
    "location": "London",
    "seats": "20-30",
    "has_toilet": true,
    "has_wifi": true,
    "has_sockets": false,
    "can_take_calls": true,
    "coffee_price": "£2.50"
  }
}
```

---

#### **3. Get All Cafés**
`GET /all`  
- Returns all cafés stored in the database.  

✅ Example Response:
```json
{
  "cafes": [
    {"id": 1, "name": "Cafe Nero", "location": "Paris", ...},
    {"id": 2, "name": "Costa Coffee", "location": "London", ...}
  ]
}
```

---

#### **4. Search Café by Location**
`GET /search?loc=Paris`  
- Searches cafés in a specific city/location.  

✅ Example Success Response:
```json
{
  "cafes": [
    {"id": 4, "name": "Le Paris Café", "location": "Paris", ...}
  ]
}
```

❌ Example Error Response:
```json
{
  "error": {
    "Not Found": "Sorry, we dont have a cafe at that location"
  }
}
```

---

#### **5. Add a New Café**
`POST /add?api-key=TopSecretAPIKey`  
- Adds a new café record.  
- Requires **API Key** (`TopSecretAPIKey`).  
- Accepts **form-data**:  

| Key            | Value (Example) |
|----------------|-----------------|
| name           | "Cafe Latte"    |
| map_url        | "https://goo.gl/maps/xyz" |
| img_url        | "https://images.com/cafe.jpg" |
| location       | "Berlin" |
| seats          | "15-20" |
| has_toilet     | 1 |
| has_wifi       | 1 |
| has_sockets    | 0 |
| can_take_calls | 1 |
| coffee_price   | "€3.00" |

✅ Success Response:
```json
{
  "response": {
    "Success": "Successfully added new Cafe"
  }
}
```

❌ Error Response (wrong API key):
```json
{
  "error": {
    "Not Found": "Sorry, That's not allowed, make sure you have a correct api_key"
  }
}
```

---

#### **6. Update Coffee Price**
`PATCH /update-price/<cafe_id>?new_price=£3.50`  
- Updates the coffee price of a given café.  

✅ Success Response:
```json
{
  "Success": "Successfully updated the price"
}
```

❌ Error Response:
```json
{
  "error": {
    "Not Found": "Sorry, a cafe with that id was not found in database"
  }
}
```

---

#### **7. Delete a Café**
`DELETE /report-closed/<cafe_id>?api-key=TopSecretAPIKey`  
- Deletes a café by ID.  
- Requires **API Key**.  

✅ Success Response:
```json
{
  "Success": "Successfully Deleted cafe"
}
```

❌ Error Response:
```json
{
  "error": {
    "Not Found": "Sorry, a cafe with that id was not found in database"
  }
}
```

---

### 🔎 Testing with Postman
- All endpoints were tested with **Postman**.  
- Tested success cases and error handling.  
- Published **Postman Documentation** for easy use:  
👉 [Postman Docs Link](https://documenter.getpostman.com/view/48698162/2sB3QCRCs8)  

---

### 💡 Extra Challenge Ideas
- Implement **PUT** to update multiple fields at once.  
- Add **authentication & user roles** (e.g., admin-only for POST/DELETE).  
- Introduce **pagination** for `/all` results.  
- Add **rating & reviews system** for each café.  
- Deploy API to **Heroku/Render** for public access.  

---
