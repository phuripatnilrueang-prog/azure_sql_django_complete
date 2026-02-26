#!/bin/bash

echo "Installing Microsoft ODBC Driver 18 for SQL Server..."

# 1. Install prerequisites
apt-get update
apt-get install -y curl apt-transport-https gnupg2

# 2. Add Microsoft repository keys
curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --yes --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
curl -fsSL https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

# 3. Install the ODBC driver
apt-get update
ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev

echo "Starting Gunicorn server..."

# 4. Start the Django application
gunicorn --bind=0.0.0.0 --timeout 600 azure_project.wsgi:application