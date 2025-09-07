import pandas as pd
import mysql.connector
import os
import logging
import time
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('csv_to_sql.log'),
        logging.StreamHandler()  # Also output to console
    ]
)
logger = logging.getLogger(__name__)

# List of CSV files and their corresponding table names
csv_files = [
    ("inventory.csv","inventory"),
    ("products.csv","products"),
    ("purchases.csv","purchases"),
    ("sales.csv","sales"),
    ("vendor_invoices.csv","vendor_invoices"),
    ("vendors.csv","vendors")
]

# Dictionary to map CSV files to their date columns (modify as needed)
date_columns = {
    'inventory.csv': ['receive_date'],  # Example: 'order_date' is a date column in orders.csv
    'purchases.csv': ['order_date','delivery_due_date'],
    'sales.csv': ['sale_date'],
    'vendor_invoices.csv': ['invoice_date','payment_date'],
    'vendors.csv': ['registration_date']
    # Add other CSV files and their date columns as needed
}

# Folder containing the CSV files
folder_path = r'D:\VISHAL\Portfolio Project\Vendor Performance\vendor performance dataset'

def get_sql_type(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return 'INT'
    elif pd.api.types.is_float_dtype(dtype):
        return 'FLOAT'
    elif pd.api.types.is_bool_dtype(dtype):
        return 'BOOLEAN'
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return 'DATETIME'
    else:
        return 'TEXT'

def main():
    # Start timing for the entire process
    overall_start_time = time.time()
    logger.info("Starting CSV to SQL migration process")

    # Connect to the MySQL database
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='vendor_db'
        )
        cursor = conn.cursor()
        logger.info("Successfully connected to MySQL database")

        for csv_file, table_name in csv_files:
            file_path = os.path.join(folder_path, csv_file)
            logger.info(f"Processing {csv_file} for table {table_name}")

            # Start timing for the current CSV file
            file_start_time = time.time()

            # Read CSV and create table
            try:
                # Read the CSV file into a pandas DataFrame, parsing date columns
                parse_dates = date_columns.get(csv_file, [])
                logger.info(f"Reading CSV file: {file_path}")
                csv_start_time = time.time()
                df = pd.read_csv(file_path, parse_dates=parse_dates)
                csv_read_time = time.time() - csv_start_time
                logger.info(f"CSV read time: {csv_read_time:.2f} seconds")

                # Replace NaN with None to handle SQL NULL
                df = df.where(pd.notnull(df), None)

                # Log dtypes and NaN values
                logger.info(f"Column dtypes for {csv_file}:\n{df.dtypes}")
                logger.info(f"NaN values before replacement:\n{df.isnull().sum()}")

                # Clean column names
                df.columns = [col.replace(' ', '_').replace('-', '_').replace('.', '_') for col in df.columns]

                # Generate and execute the CREATE TABLE statement
                columns = ', '.join([f'`{col}` {get_sql_type(df[col].dtype)}' for col in df.columns])
                create_table_query = f'CREATE TABLE IF NOT EXISTS `{table_name}` ({columns})'
                logger.info(f"Executing CREATE TABLE query: {create_table_query}")
                table_start_time = time.time()
                cursor.execute(create_table_query)
                table_create_time = time.time() - table_start_time
                logger.info(f"Table creation time: {table_create_time:.2f} seconds")

                # Insert DataFrame data into the MySQL table
                insert_start_time = time.time()
                row_count = 0
                for _, row in df.iterrows():
                    try:
                        values = tuple(None if pd.isna(x) else x for x in row)
                        sql = f"INSERT INTO `{table_name}` ({', '.join(['`' + col + '`' for col in df.columns])}) VALUES ({', '.join(['%s'] * len(row))})"
                        cursor.execute(sql, values)
                        row_count += 1
                    except mysql.connector.Error as e:
                        logger.error(f"Error inserting row {row_count + 1} into {table_name}: {e}")
                insert_time = time.time() - insert_start_time
                logger.info(f"Inserted {row_count} rows into {table_name} in {insert_time:.2f} seconds")

                # Commit the transaction for the current CSV file
                conn.commit()
                logger.info(f"Committed transaction for {table_name}")

                # Log total time for this CSV file
                file_total_time = time.time() - file_start_time
                logger.info(f"Total processing time for {csv_file}: {file_total_time:.2f} seconds")

            except pd.errors.ParserError as e:
                logger.error(f"Error reading CSV file {csv_file}: {e}")
            except mysql.connector.Error as e:
                logger.error(f"Database error for {csv_file}: {e}")
            except Exception as e:
                logger.error(f"Unexpected error processing {csv_file}: {e}")

    except mysql.connector.Error as e:
        logger.error(f"Error connecting to MySQL database: {e}")
    except Exception as e:
        logger.error(f"Unexpected error during database connection: {e}")
    finally:
        if cursor:
            cursor.close()
            logger.info("Cursor closed")
        if conn and conn.is_connected():
            conn.close()
            logger.info("Database connection closed")

    # Log total execution time
    overall_time = time.time() - overall_start_time
    logger.info(f"Total execution time: {overall_time:.2f} seconds")
    logger.info("CSV to SQL migration process completed")

if __name__ == "__main__":
    main()


