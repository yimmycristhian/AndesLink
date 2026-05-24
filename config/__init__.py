import sys

# 1. Bypass MariaDB/MySQL version check for older local servers (e.g. MariaDB 10.4)
try:
    from django.db.backends.base.base import BaseDatabaseWrapper
    BaseDatabaseWrapper.check_database_version_supported = lambda self: None
except ImportError:
    pass

# 2. Disable RETURNING clause features for older MariaDB/MySQL versions (e.g. MariaDB < 10.5)
try:
    from django.db.backends.mysql.features import DatabaseFeatures
    DatabaseFeatures.can_return_columns_from_insert = False
    DatabaseFeatures.can_return_rows_from_bulk_insert = False
except ImportError:
    pass

# 3. Use PyMySQL as a drop-in replacement for mysqlclient (needed for Vercel/Serverless deployment)
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
