from pyspark.sql import SparkSession


def main():
    spark = SparkSession.builder.appName("Test").getOrCreate()
    df = spark.read.csv("Nigerian Foods.csv", header=True)
    print(df.count())


if __name__ == "__main__":
    main()
