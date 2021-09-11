CREATE USER test_user WITH PASSWORD 'test_pswd';

CREATE DATABASE test_blog;
GRANT ALL PRIVILEGES ON DATABASE test_blog TO test_user;
