# Back up tool for Valheim

* Requires Python
* To install the requrements run `pip install requirements.txt`
* Populate client secrets see below

By default the backup will run every 10 mins. To edit the time variable on line 12.

## How to populate client secrets

1) Go to APIs Console and make your own project.
2) Search for ‘Google Drive API’, select the entry, and click ‘Enable’.
3) Select ‘Credentials’ from the left menu, click ‘Create Credentials’, select ‘OAuth client ID’.
4) Now, the product name and consent screen need to be set -> click ‘Configure consent screen’ and follow the instructions. Once finished:
Select ‘Application type’ to be Web application.

        a) Enter an appropriate name.
        b) Input http://localhost:8080 for ‘Authorized JavaScript origins’.
        c)  Input http://localhost:8080/ for ‘Authorized redirect URIs’.
        d) Click ‘Save’.
5) Click ‘Download JSON’ on the right side of Client ID to download client_secret_<really long ID>.json.

The downloaded file has all authentication information of your application. Rename the file to “client_secrets.json” and place it in this directory.