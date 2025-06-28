# FastAPI Bazaar Commands Reference

This file consolidates all the key commands used during Milestone 3 and related setup, using Docker Compose, Alembic, and MySQL.

---

## 1. Docker Cleanup & Start

```bash
# Stop and remove containers and network
docker-compose down

#List available volumes
docker volume ls

# Remove the MySQL volume for a fresh DB initialization
docker volume rm fastapi-bazaar_db_data

# Build images and start services in detached mode
docker-compose up -d --build
```

---

## 2. Enter the Web Container

```bash
# Open a shell inside the FastAPI (web) container
docker-compose exec web bash
```

---

## 3. Initialize Alembic Migrations

```bash
# Inside the web container, initialize the migrations folder
alembic init app/db/migrations
```

---

## 4. Generate & Apply Migrations

```bash
# Create an auto-generated migration based on SQLAlchemy models
docker-compose exec web alembic revision --autogenerate -m "create products table"

# Apply all migrations to the database
docker-compose exec web alembic upgrade head
```

---

## 5. Inspect Tables via DB Container

```bash
# Enter the MySQL (db) container
docker-compose exec db bash

# Inside the db container, list tables in your database
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" \
  -e "SHOW TABLES;" "$MYSQL_DATABASE"

# Show table structure for 'products'
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" \
  -e "DESCRIBE products;" "$MYSQL_DATABASE"

# Show full CREATE TABLE DDL
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" \
  -e "SHOW CREATE TABLE products\G" "$MYSQL_DATABASE"
```

---

## 6. One-Liner Host Commands (Non-Interactive)

```bash
# List tables from host without interactive shell
docker-compose exec db sh -c 'mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW TABLES;" "$MYSQL_DATABASE"'

# Describe products table via one-liner
docker-compose exec db sh -c 'mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "DESCRIBE products;" "$MYSQL_DATABASE"'
```

---

## 7. Renaming or Recreating Database

### Option A: Fresh Rename (Lose existing data)

```bash
# Update .env with new MYSQL_DATABASE
# Then:
docker-compose down
docker volume rm fastapi-bazaar_db_data
docker-compose up -d --build
docker-compose exec web alembic revision --autogenerate -m "initial schema"
docker-compose exec web alembic upgrade head
```

### Option B: In-Place Create & Grant (Preserve data)

```bash
docker-compose exec db bash
mysql -uroot -p"$MYSQL_ROOT_PASSWORD" -e "
CREATE DATABASE IF NOT EXISTS new_db_name;
GRANT ALL PRIVILEGES ON new_db_name.* TO '$MYSQL_USER'@'%';
FLUSH PRIVILEGES;
"
exit

# Update .env (MYSQL_DATABASE=new_db_name)
docker-compose up -d --build web
docker-compose exec web alembic revision --autogenerate -m "initial schema"
docker-compose exec web alembic upgrade head
```
