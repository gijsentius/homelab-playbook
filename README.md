# README

## Installation of ansible environment

On the host mysqldump and mysql need to be present. Install them with the following command.

```bash
sudo apt-get install -y --no-install-recommends mysql-client
```

You may need to install the Python 3 and MySQL development headers and libraries.

```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config # Debian / Ubuntu
sudo yum install python3-devel mysql-devel pkgconfig # Red Hat / CentOS
```

Then you can install mysqlclient via pip.

```bash
$ pip install mysqlclient
```
