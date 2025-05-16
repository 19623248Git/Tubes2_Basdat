# Database Kelompok 4

## How to use the script
### Faker

### WARNING: DO NOT OVERWRITE DRG.sql AS IT IS STANDARD DATA

#### Windows
Generate the fake data using
```
python seeder.py > {output_name}.sql
```

#### Linux
Generate the fake data using
```
python3 seeder.py > {output_name}.sql
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
