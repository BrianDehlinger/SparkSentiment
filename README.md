# SparkSentiment

Apache Spark and Sentiment Anaylsis of the 61 United States National Parks in Real Time on Twitter. The main focus of this project will be to gain hands on experience designing and presenting an end-to-end solution to a big data problem. Ideally, this will showcase my skills in software engineering, data visualization, and design in general.

# Technologies for consideration:

### Chosen

```
Elasticsearch - For ease of use, indexing abilities, and easy queries
```

### Considering

```
Kibana - For easy integration with elasticsearch.
Plotly - For nice visualizations
Dash - For dashboard visualization creation.
```

### Also Considering

```
Spark Streaming
Apache Kafka
MLLib
Postgresql
Dash - for dashboard visualization creation
AWS
```

# Status

The rapid prototype was a success and was done using a tutorial. The program at this moment takes a hardcoded input to search as a term on Twitter. The results are then fed to elasticsearch on a docker container. The data is then fed to Kibana for visualization in real time. The program is fully functional. 

Currently, I am working on deciding on a method to allow for concurrency. I want to first test out threading and see if it is possible to distribute thread instances across Spark. I found this Medium article: https://medium.com/@rbahaguejr/threaded-tasks-in-pyspark-jobs-d5279844dac0 Data delivery needs to be assured with hashing in a production environment. Encryption probably doesn't need to occur as this data is publicly accessible. 

I also want to see how to preprocess the data. Preliminary testing reveals that a lot of tweets might involve other languages, emojis, words like brooooooo, yeesssss, and so forth. Emojis and long words might actually be useful for sentiment analysis but clearly there exists a lot of variation and the data needs to be cleaned. I think pandas might be good for a development envirionment to prototype to see how possible this is, but it probably is not good for production use in this case.

I've been looking at expanding data sources to also include other sites. I've also thought of other possible use cases like examining words associated with sentiment and their distribution. This would involve some of the same functions but they may differ slightly on use case. Decorators might be useful here.

# Goals

```
More Natural Language processing
Kibana vs Plotly/Dash
Visualize Data on National Parks
```

## Acknowledgments

* Hat tip to https://realpython.com/twitter-sentiment-python-docker-elasticsearch-kibana/


