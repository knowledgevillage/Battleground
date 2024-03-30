import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("answers").getOrCreate()

path=f"S:\GitRepo\Battleground\SparkSpear\inc_t1_datafile_2023.csv"

print("hello")

df=spark.read.option("header",'True').option('delimiter', ',').csv(path)
df.printSchema()
df.show(2)