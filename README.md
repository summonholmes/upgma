# upgma
Demonstration of the UPGMA hierarchal clustering algorithm in Pandas and Seaborn

## Introduction
The Unweighted Pair Group Method with Arithmetic Mean (UPGMA) algorithm is a bottom up agglomerative/hierarchical clustering algorithm commonly performed on genetic distance matrices.  Running the UPGMA algorithm generally allows for construction of a dendrogram.  The code in this repository utilizes Pandas and Seaborn for data visualization and vectorization capabilities.

In the context of this repository, UPGMA performs deterministically.  Therefore, results will always be the same for every run.  In addition, as long as the data integrity is preseverd, the data may organized in any order and the results will still remain the same.

## Start
![alt text](https://raw.githubusercontent.com/summonholmes/upgma/master/Start.png)

## Finish
![alt text](https://raw.githubusercontent.com/summonholmes/upgma/master/Finish.png)

## Results
```
{('Man', 'Monkey'): 0.5,
 ('Turtle', 'Chicken'): 4.0,
 (('Man', 'Monkey'), 'Dog'): 6.25,
 (('Turtle', 'Chicken'), (('Man', 'Monkey'), 'Dog')): 7.875,
 ((('Turtle', 'Chicken'), (('Man', 'Monkey'), 'Dog')), 'Tuna'): 14.1875,
 (((('Turtle', 'Chicken'), (('Man', 'Monkey'), 'Dog')), 'Tuna'), 'Moth'): 18.21875}
```

## Dependencies
* python3-numpy
* python3-pandas
* python3-seaborn

## Running the Code
Execute the upgma.py file in an IPython environment.

Tables may be viewed by running commands such as:
```
upgma.upgma_records[('Man', 'Monkey')]
upgma.upgma_records[(((('Turtle', 'Chicken'), (('Man', 'Monkey'), 'Dog')), 'Tuna'),'Moth')]
```

The phylogenetic distances may be viewed by running:
```
upgma.phylogeny
```
