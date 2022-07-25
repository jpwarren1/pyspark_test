from pyspark import SparkContext
from operator import add

def spark_context():
    sc = SparkContext.getOrCreate()
    return sc


def do_word_counts(lines):
    """ count of words in an rdd of lines """

    counts = (lines.flatMap(lambda x: x.split())
                  .map(lambda x: (x, 1))
                  .reduceByKey(add)
             ) 
    results = {word: count for word, count in counts.collect()}
    return results