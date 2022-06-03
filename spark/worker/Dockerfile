ARG spark_version="3.0.0"
ARG SPARK_MASTER_HOST="spark-master"
ARG SPARK_MASTER_PORT="7077"
FROM spark-base

ARG build_date

EXPOSE 8081

CMD bin/spark-class org.apache.spark.deploy.worker.Worker spark://${SPARK_MASTER_HOST}:${SPARK_MASTER_PORT} >> logs/spark-worker.out
