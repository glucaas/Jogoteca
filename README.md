# Jogoteca

CRUD Library of games using flask and SQLAlchemy

## Requirements

Make sure you have the following prerequisites installed on your system:

- Python
- Docker-compose
- WSL + Docker or Docker Desktop

## How to Run the Application

1. Open your WSL or Docker Desktop terminal.

2. Run the following command to start the application using Docker Compose:

   ```bash
   docker-compose -d
   ```

3. Retrieve the IP address of your container by running the command:

   ```bash
   docker inspect my-local-db
   ```

Copy the obtained IP address.

Paste the copied IP address into the "Config.py" file under the servidor property.

Start the application by executing the following commands:

```bash
docker-compose up -d
python3 jogoteca.py
```

## How to check dabase content

since the my-local-db container is running you can connect to the container and look up to the tables using the terminal commands.

To enter in the container and sign in on the MySql Environment

```bash
mysql -h 172.25.0.1 -P 3306 -u root -p
```

**NOTE**: this IP Address is the same that you have in your my-local-db container network, thus, can be different.

Some useful commands:

- List databases:

```bash
SHOW DATABASES;
```

- Select a database:

```bash
USE NOME_DO_BANCO_DE_DADOS;
```

- List tables in the current database:

```bash
SHOW TABLES;
```

- View the structure of a table:

```bash
DESCRIBE NOME_DA_TABELA;
```

- Execute SQL queries:

```bash
SELECT * FROM NOME_DA_TABELA;
```

- Exit MySQL:

```bash
EXIT;
```
