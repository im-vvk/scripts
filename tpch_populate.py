#!/usr/bin/env python
# coding: utf-8

import glob
import time
import findspark
findspark.init()
findspark.find()
import pyspark
findspark.find()
from pyspark.sql import SparkSession


spark = SparkSession\
        .builder\
        .appName("tpch")\
        .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/tpch")\
        .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/tpch")\
        .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1")\
        .config("spark.executor.memory", "2g")\
        .config("spark.driver.memory", "4g")\
        .getOrCreate()

db_name = "tpch"
json_files = []

for file in glob.glob("*.json"):
    json_files.append(file)

def populate_db(file_name):
    file_name_without_extension = file_name.split('.')[0]
    df = spark.read.json(file_name, multiLine = "true")
    df.write.format("mongo").mode("append").option("database",db_name).option("collection", file_name_without_extension).save()

strat_time = start_func_time =  end_time = time.time()
for file in json_files:
    strat_time = time.time()
    populate_db(file)
    end_time = time.time()
    print("Time taken to populate %s Collection: %.2f s" %(file.split(".")[0], end_time - strat_time))
end_time = time.time()

print("Total time taken: %.2f s" %(end_time - start_func_time))
spark.stop()



