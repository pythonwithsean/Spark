from pyspark.sql import SparkSession


def main():
    spark = SparkSession.builder.appName("Test").getOrCreate()
    print(spark.getActiveSession())
    df = spark.read.csv("Nigerian Foods.csv", header=True,inferSchema=True)
    print(df.count())
    df.show(n=5)
    print(df.dtypes)
    df.printSchema()


if __name__ == "__main__":
    main()
