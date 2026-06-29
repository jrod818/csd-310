# Name: Jose Rodriguez
# Date: 2026-06-28
# Assignment: CSD-310 Module 5 Assignment - Movies Setup
# Description: This program tests the connection to the movies database using
# login values stored in a hidden .env file.

import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values

# Load database login information from .env file.
secrets = dotenv_values('.env')

config = {
    'user': secrets['USER'],
    'password': secrets['PASSWORD'],
    'host': secrets['HOST'],
    'database': secrets['DATABASE'],
    'raise_on_warnings': True
}

try:
    # Connect to the movies database.
    db = mysql.connector.connect(**config)

    # Display successful connection message.
    print('\nDatabase user {} connected to MySQL on host {} with database {}'.format(
        config['user'], config['host'], config['database']
    ))

    input('\nPress any key to continue...')

except mysql.connector.Error as err:
    # Display connection error information.
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('The supplied username or password are invalid')

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('The specified database does not exist')

    else:
        print(err)

finally:
    # Close database connection if it was created.
    if 'db' in locals() and db.is_connected():
        db.close()
