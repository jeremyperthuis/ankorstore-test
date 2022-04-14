# Ankostore test
Perthuis Jeremy

## I Project Description

This project embedded a mini flask server plus a Selenium based scrapping script.

 - Scrapper : The scrapper retrieve informations from Google maps results, and persists information in a database.

 - Flask server : The server expose data through a simple API. 

## II Installation

### Requirements
- Ubuntu based environement
- Python 3.9
- Chromium 100

### Procedure

1. Clone repository
    ```bash
    git clone https://github.com/jeremyperthuis/ankorstore-test.git && cd ankorstore-test 
    ```
2. Add permission for sh files
   ```
   chmod a+x install.sh launch_server.sh launch_scrapping.sh -v 
   ```

3. Install python environment
    ```bash
    ./install.sh
    ```

4. Launch scrapping
    ```bash
    ./launch_scrapping.sh
    ```
5. Launch flaks server
    ```bash
    ./launch_server.sh
    ```

6. Test API endpoint by copying this link in a browser
    ```
    http://127.0.0.1:5000/api/v1/company
    ```
