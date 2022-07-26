from pyspark.sql import functions as SF
from operator import add

def spark_context():
    sc = SparkContext.getOrCreate()
    return sc

def do_word_counts(df):

  df_word_count = (df.withColumn('word', SF.explode(SF.split(SF.col('sentences'), ' ')))
    .groupBy('word')
    .count()
    .sort('count', ascending=False)
 )
  
  return df_word_count