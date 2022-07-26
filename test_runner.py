# Databricks notebook source
!pip install pytest==7.1.2

# COMMAND ----------

from transformations import a_transformation as at
from pyspark.sql import types as T
import sys
import pytest
import os

# COMMAND ----------

sys.dont_write_bytecode = True

# COMMAND ----------

repo = os.getcwd()
os.chdir(repo)

# COMMAND ----------

sys.dont_write_bytecode = True

# COMMAND ----------

retcode = pytest.main([".", "-p", "no:cacheprovider"])

# COMMAND ----------


