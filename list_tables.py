import psycopg2
import sys

# IMPORTANT: It is recommended to use environment variables or a secret management system
# to store your connection string, rather than hardcoding it in the source code.
# For this example, we are keeping it simple.

# Replace with your actual connection string
# Note: The user provided the password, but it's better to remind them to use a placeholder
# and let them edit the file. However, for this example, I will use the one they provided.
# A better approach would be to read it from an environment variable.
CONNECTION_STRING = "postgresql://neondb_owner:npg_yxlY28rJcMFv@ep-lively-unit-adtogwhk-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require"

def list_tables():
    """
    Connects to a PostgreSQL database and lists all the tables in the public schema.
    """
    # This function is kept for reference, but not called in this version of the script.
    try:
        # Connect to the database
        print("Connecting to the database...")
        conn = psycopg2.connect(CONNECTION_STRING)
        print("Connection successful.")

        # Create a cursor
        cur = conn.cursor()

        # Query to get the list of tables
        cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)

        # Fetch all the rows
        tables = cur.fetchall()

        # Print the table names
        if tables:
            print("\nList of tables in the 'public' schema:")
            for table in tables:
                print(f"- {table[0]}")
        else:
            print("\nNo tables found in the 'public' schema.")

    except psycopg2.OperationalError as e:
        print(f"Error: Could not connect to the database. Please check your connection string and network.", file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        # Close the cursor and connection
        if 'cur' in locals() and cur:
            cur.close()
        if 'conn' in locals() and conn:
            conn.close()
            print("\nConnection closed.")

def list_brands():
    """
    Connects to the database and lists all entries from the 'brands' table.
    """
    try:
        # Connect to the database
        print("Connecting to the database...")
        conn = psycopg2.connect(CONNECTION_STRING)
        print("Connection successful.")

        # Create a cursor
        cur = conn.cursor()

        # Query to get all entries from the brands table
        cur.execute("SELECT * FROM brands;")

        # Fetch all the rows
        brands = cur.fetchall()

        # Print the brands
        if brands:
            print("\nContents of the 'brands' table:")
            # Assuming the table has columns (id, name) or similar. 
            # We'll print all columns for each row.
            for brand in brands:
                print(f"- {brand}")
        else:
            print("\nNo data found in the 'brands' table.")

    except psycopg2.OperationalError as e:
        print(f"Error: Could not connect to the database. Please check your connection string and network.", file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit(1)
    except psycopg2.ProgrammingError as e:
        print(f"Error: A database programming error occurred. This might be due to the table or columns not existing.", file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        # Close the cursor and connection
        if 'cur' in locals() and cur:
            cur.close()
        if 'conn' in locals() and conn:
            conn.close()
            print("\nConnection closed.")

if __name__ == "__main__":
    list_brands()