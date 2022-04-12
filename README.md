# Ankostore test
Perhtuis Jeremy



## Installation

### Requirements
- Ubuntu based environement
- Python 3.9
- Chromium 100

### Procedure

1. Clone repository
```bash
 git clone https://github.com/jeremyperthuis/ankorstore-test.git && cd ankorstore-test && chmod a+x install.sh
 
```

2. Launch scrapping
```bash
sudo apt-get update && \
sudo apt-get install -y chromium-browser
```

3. Launch API server
```bash
chmod a+x install.sh
./install.sh
```

4. Test API
```
    http://127.0.0.1:5000/api/v1/company
```