
# Project Name
-----
## AI For Social Good
### Application which prevents suicide by detecting suicidal thoughts and messages in social media sites.
-----
![summary](./Assets/main.jpg)

## Project Description
A suicide note used to be the mode of final communication of a person taking his/her own life. But the rise of social media and online communities like Reddit creates safe and anonymous spaces for individuals to be vulnerable and share their thoughts about their mental health and plans about taking their own lives. My project aims to use Natural Language Processing(NLP) tools to analyse text data  learn what words are used in a virtual suicide note. With the help of Machine Learning classifiers, and Deep Learning Models i aim to accurately identify individuals at risk of suicide.

### Project Details
* To do this task i needed to scrap two reddits. Mostly people in depression are likely to commit sucide and the one posting sucide notes.So i decided to go with two subreddits depression and suicide.
* I scraped the data of reddits containing depression and suicide.I scraped nearly 3000 posts.
* I cleand the data and removed duplicate records and total number of posts left for training was 2000.
* I  performed text analysis (both unigram and bigram)  and visulisation of most occuring words in both reddits.
* I performed vectorization of text data and applied Random Forest , Xgboost and MultinomialNB for classification which obtained an  accuracy of 72%.
* I used Multilayer Bidirectional LSTM to build a model which has an accuracy of 66 %.

### Technology
* Deep Learning
* Tensorflow
* Keras
* Machine Learning


### Methods
* LSTM
* Bidirectional LSTM
* TFIDF
* Bag Of Words
* XGBOOST
* Radom Forest
* Multinomial Naive Bayes 



### Usage
* All the dataset used can be found in `./Dataset`
* To perform data collection codes can be found in `./Data Collection`
* To Build Models codes can be found in `./Src`
* All Models can be found in `./Models`


`Note:` I have only used only 2000 reddits to train so accuracy seems to be less , accuracy can be improved by extracting more data form different other social media sites.





