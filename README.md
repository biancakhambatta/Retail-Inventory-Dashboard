# Retail Inventory Dashboard

**A full-stack dashboard that turns retail sales data into clear business metrics.**

It shows total inventory items, gross sales, total profit and overall profit margin, highlights the most profitable product, and includes a searchable inventory table. Built with a Flask API, a PostgreSQL database and a Tailwind CSS interface.

---

## Features

- **Business metrics:** total inventory items, gross sales, total profit and overall profit margin, calculated in the database
- **Product insights:** the product with the highest profit
- **Searchable inventory table:** a scrollable table with instant search filtering in the browser
- **Responsive dark interface** built with Tailwind CSS

## Tech stack

| Layer | Tools |
|---|---|
| Backend | Python, Flask, Flask-SQLAlchemy |
| Database | PostgreSQL |
| Frontend | HTML, Tailwind CSS, JavaScript |

## API endpoints

| Endpoint | Returns |
|---|---|
| `GET /` | The dashboard page |
| `GET /api/products` | All products with their id, name, sales and profit |
| `GET /api/analytics/summary` | Total items, total sales, total profit and overall profit margin (%) |

Profit margin is calculated as total profit divided by total sales, times 100.

## Project structure

~~~
inventory-backend/
  app.py              Flask app, database configuration and startup
  models.py           Database model (SuperstoreProduct)
  routes.py           Page route and API endpoints
  requirements.txt    Python dependencies
  templates/
    index.html        Dashboard interface
superstore_data/
  samplesuperstore.csv   Sample sales data
~~~

## Run it locally

You will need Python 3 and PostgreSQL installed.

1. Clone the repository and install the dependencies:

   ~~~
   git clone https://github.com/biancakhambatta/Retail-Inventory-Dashboard.git
   cd Retail-Inventory-Dashboard/inventory-backend
   pip install -r requirements.txt
   ~~~

2. Create a PostgreSQL database named `superstore_db`.

3. In the `inventory-backend` folder, create a file called `.env` containing your PostgreSQL password:

   ~~~
   DB_PASSWORD=your_password_here
   ~~~

   The app connects as the `postgres` user on `localhost:5432`.

4. Start the app once to create the `superstore_product` table:

   ~~~
   python app.py
   ~~~

5. Load the sample data: import the **Product Name**, **Sales** and **Profit** columns from `superstore_data/samplesuperstore.csv` into the `superstore_product` table (for example with the Import/Export tool in pgAdmin).

6. Open http://localhost:5000 in your browser.

## Data

The sample data is the Sample Superstore dataset, downloaded from Kaggle.

## Limitations and next steps

- The product list endpoint returns every row at once. For larger data I would add pagination and server-side search.
- The app runs on the Flask development server with debug mode on. A production setup would use a proper server such as Gunicorn.
- Automated tests for the summary calculations, such as profit margin on a small known dataset.
