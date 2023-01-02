This README file provides instructions for running this Flask-based REST API and the purpose of the API.

Project Purpose:

The purpose of this API is to serialize form data and send the data to an SQlite3 tabular database where it can be queried.

Instructions:

1. Run database_creator.py if personal_information.db does not previously exist

2. Run main.py then execute test.py.

2. DO NOT execute "db.create_all" in the main API unless you need to delete the entire db, reconfigure the database or 
launch the entire app into production. Otherwise you will overwrite your database!

3. DO NOT execute database_creator.py UNLESS personal_information.db did not previously exist.

4. Ensure that all necessary dependencies are installed.

5. If the app is being launched into production, change the debug parameter from "false" to "true" inside Rest_API's main.py file.

