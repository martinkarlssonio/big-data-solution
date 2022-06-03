import time    
epochNow = int(time.time())
from pyspark.sql import SparkSession
sparkSession = SparkSession.builder.appName("example-pyspark-read-and-write").getOrCreate()
# Create data
data = [('First', 1), ('Second', 2), ('Third', 3), ('Fourth', 4), ('Fifth', 5)]
df = sparkSession.createDataFrame(data)
df.show()

# Write into HDFS
df.write.csv("hdfs://hadoop-namenode:9000/test/{}.csv".format(epochNow))
# Read from HDFS
df_load = sparkSession.read.csv("hdfs://hadoop-namenode:9000/test/{}.csv".format(epochNow))
df_load.show()