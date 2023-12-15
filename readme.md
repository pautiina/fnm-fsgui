## Flowspec-GUI: create Flowspec rules & deploy to FNM Adv.

### Run it

Clone the git repository
```bash
git clone https://github.com/pirmins/fnm-fsgui.git
```
Create a Python virtual environment (developped with Python 3.11)
```bash
cd fsgui
python3 -m venv myenv
```

Activate the virtual environment
```bash 
. myenv/bin/activate
```

Install the dependencies from requirements.txt
```bash 
pip install -r requirements.txt
```

Define your own Fastnetmon API env. variables

```bash 
export FNM_API_ENDPOINT="http://127.0.0.1:10007"
export FNM_API_USER=admin
export FNM_API_PASSWORD=password
```

Hardcoded defaults if no ENV VARs found are:
```python
DEFAULT_API_ENDPOINT = "http://127.0.0.1:10007"
DEFAULT_API_USER = "fnmadmin"
DEFAULT_API_PASSWORD = "fnmpassword"
```

Create a Django superuser
```bash 
python3 manage.py createsuperuser
```

Start the Django app with runserver
```bash 
python3 manage.py runserver "0.0.0.0:8000"
```

## GUI

Login page

![image](https://github.com/pirmins/fnm-fsgui/assets/49155818/ab91f295-cef6-4cab-b83f-499fc1c7413e)




Welcome page

![image](https://github.com/pirmins/fnm-fsgui/assets/49155818/b95139ca-6c4e-4666-b02c-e559b2f6e02c)






### Admin View

Admin Networks Panel (sees all networks allocated)

![image](https://github.com/pirmins/fnm-fsgui/assets/49155818/84e0df74-200c-4d19-b12c-024595b044a1)



Admin Flowspec Panel (sees all flowspec rules created)

![image](https://github.com/pirmins/fnm-fsgui/assets/49155818/09d75b78-2240-4564-9f9a-21b0e911b07a)






### User View

User Networks page (sees only what networks he's been allocated)

![image](https://github.com/pirmins/fnm-fsgui/assets/49155818/055f84a9-a9e8-4c5d-ae20-40ebbb7fc60d)



User Flowspec panel (sees/can create flowspec rules for his allocated networks)

![image](https://github.com/pirmins/fnm-fsgui/assets/49155818/fd5f59b3-b8f0-4ced-a1be-60499a11c925)




