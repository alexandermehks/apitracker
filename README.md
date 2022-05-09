# Keeps an eye on your imported API for changes

### Installing requirements
 ```bash
pip3 install -r requirements.txt
```

### Build
 ```bash
Windows: python3 build.py 
Linux:./build.py
```


### Running tests

 ```bash
python3 -m pytest
```

### Endpoints
***All endpoints should be included in src-> endpoints.json***

*No authorization* 

```json
{ 
 "url": "your_api_endpoint",
 "auth": "none"
}
```

*Basic authorization*
```json
{ 
 "url": "your_api_endpoint",
 "auth": "basic",
 "username": "your_username",
 "password": "your_password"
}
```
