# Data Science Foundations II - Nanodegree Program


# [Week 1 - Machine Learn and Data Science](ProblemStatement1)

## [Lesson 2: Introdução a Data Science](ProblemStatement1)


| Quiz   |  Python |
| ------------- |  ------------- 
| 17 : Criando um dataframe | 17_create_dataframe.py  |
| 19 : Brincando com o Pandas - indexando dataframes  | 19_indexando_frames.py |
| 22 : Média de medalhas de ouro, prata e bronze  | 22_avg_medal_count.py  |

## [Lesson 3: Data Wragling](ProblemStatement1) 

| Quiz   |  Python |
| ------------- |  ------------- 
| 11 : CSV Exercise | 11_exercicios_csv.py  |
| 21 : Write Your Own Simple Query  | 21_select_first_50.py  |
| 24 : Write Your Own Complex Query  | 24_aggregate_query.py  |
| 29 : API Exercise  | 29_api_get_request.py  |
| 39 : Imputation Exercise  | 39_imputation.py  |

## [Lesson 4: Machine Learn Introduction](ProblemStatement1) 

| Quiz   |  Python |
| ------------- |  ------------- 
| 15 : Linear Regression | 15_linear_regression.py  |

# [Week 4 - BigData and Map Reduce](ProblemStatement1)

## [Lesson 6: Project](ProblemStatement1)

| Quiz   |  Python Mapper And Reducer |
| ------------- |  ------------- 
|  2 : Sales per Category | q2Mapper.py / q2Reducer |
|  3 : Highest Sale  | q3Mapper.py / q3Reducer  |
|  4 : Total Sales  | q4Mapper.py / q4Reducer  |
|  6 : Hits to Page | q6Mapper.py / q6Reducer  |
|  7 : Hits from IP  | q7Mapper.py / q7Reducer  |
|  8 : Most Popular  | q8Mapper.py / q8Reducer  |




### Hadoop Mapper and Reducer  



**Para testar local windows**

```
type purchases.txt | python q4Mapper.py | sort | python q4Reducer.py

all               
```

**Para testar em Linux**

```
cat newfile.txt | python mapper.py | sort | python reducer.py
```

**Para executar Hadoop Cloudera CDH 5.xx**

```
hadoop jar ///usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.12.0.jar -file q8Mapper.py  -mapper "python q8Mapper.py" -file q8Reducer.py -reducer "python q8Reducer.py" -input access_log -output output
```



## [Project I - Analyzing NY Subway Data](ProblemStatement1)

### Visão geral do projeto
Neste projeto, você analisa os dados do metrô de NY e descobre se mais pessoas andam de metrô quando está chovendo, comparado com quando não está.

Você vai confrontar os dados do metrô de Nova York, usar métodos estatísticos e dados de visualização para tirar uma conclusão interessante sobre o metrô usando o conjunto de dados que você analisou.

### Por que este projeto?

Este projeto apresentará a você os conceitos-chave da ciência de dados. Assim, você estará preparado para projetos posteriores no Nanodegree Analista de Dados, bem como para sua futura carreira como analista de dados.

Além disso, você será exposto a alguns dos dados das bibliotecas de Python mais populares, como Pandas, Numpy e outros.

### O que vou aprender?
Você será exposto a - e aprenderá - habilidades de ciência de dados fundamentais, como:

1. Os dados de disputas
2. Estatística aplicada e aprendizagem de máquina
3. MapReduce
4. Anaconda Scientific Python.

***Jupyter Notebook*** 

Referëncia = analyzing-subway-data-ndfdsi.ipynb


## License
Copyright &copy; 1996-2018 - CGLSOFT IT Serviços Ltda.<br>
Licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
