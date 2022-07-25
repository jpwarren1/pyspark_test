# Databricks notebook source
!pip install pytest==7.1.2

# COMMAND ----------

from transformations import a_transformation as at

# COMMAND ----------

sc = at.spark_context()

# COMMAND ----------

test_input = [
        ' hello spark ',
        ' hello again spark spark'
    ]
input_rdd = sc.parallelize(test_input, 1)

# COMMAND ----------

results = at.do_word_counts(input_rdd)

# COMMAND ----------

results

# COMMAND ----------

!python -m pytest

# COMMAND ----------


