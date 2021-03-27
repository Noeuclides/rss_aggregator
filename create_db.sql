DROP DATABASE IF EXISTS rss_db;
CREATE DATABASE rss_db;
CREATE USER rss_user WITH PASSWORD 'rss_pass';
ALTER ROLE rss_user SET client_encoding TO 'utf8';
ALTER ROLE rss_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE rss_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE rss_db TO rss_user;
