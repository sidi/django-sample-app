# create other users
CREATE USER 'sid'@'%' IDENTIFIED BY 'sid2023';
GRANT ALL PRIVILEGES ON *.* TO 'sid'@'%';
