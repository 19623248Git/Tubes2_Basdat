# Database Kelompok 4

## How to use
### Faker
#### Windows
Generate the faked data using
```
python faker.py < {filename}
```

#### Linux
Generate the faked data using
```
python3 faker.py < {filename}
```

then, append the generated commands into your sql

### Database
Source the SQL into MariaDB using 
```
mariadb -u root -p < {filename}.sql
```
OR, inside mariadb
```
SOURCE {filename}.sql
```
