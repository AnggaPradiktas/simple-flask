# simple-flask

Untuk menjalankan flask apps di local computer, kita dapat melakukan command berikut pada direktori dimana file py ini disimpan

 `
 python3 flask_example.py
 `
 
 Lalu akan muncul output seperti dibawah
 
 ```
 * Serving Flask app "flask_example" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 115-340-665
127.0.0.1 - - [06/Jan/2022 14:26:17] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [06/Jan/2022 14:26:17] "GET /favicon.ico HTTP/1.1" 404 -
 ```

## Flask w/ sqllite & SQLAlchemy

Install SQLAlchemy for Flask

`pip install -U Flask-SQLAlchemy`

Dari dalam terminal cli, kita dapat panggil script berikut [flask_sqllite](https://github.com/AnggaPradiktas/simple-flask/blob/main/flask_sqllite.py)

```
from yourapplication import db
db.create_all()

from yourapplication import User
admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')

db.session.add(admin)
db.session.add(guest)
db.session.commit()
```

Mengakses data yang sudah disimpan menggunakan python cli

```
User.query.all()

User.query.filter_by(username='admin').first()

```

Atau kita juga dapat mengaksesnya langsung menggunkan sqllite

```
sqlite3

.open /tmp/test.db

.database

.tables

SELECT * FROM user;
```
