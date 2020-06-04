
# Project Name
-----
## AI For Social Good
### Application which prevents suicide by detecting suicidal thoughts and messages in social media sites.
-----
![summary](./Assets/main.jpg)

### About The Project
A suicide note used to be the mode of final communication of a person taking his/her own life. But the rise of social media and online communities like Reddit creates safe and anonymous spaces for individuals to be vulnerable and share their thoughts about their mental health and plans about taking their own lives. My project aims to use Natural Language Processing(NLP) tools to analyse text data  learn what words are used in a virtual suicide note. With the help of Machine Learning classifiers, and Deep Learning Models i aim to accurately identify individuals at risk of suicide.

### Project Details
* To do this task i scraped two reddits. Mostly people in depression are likely to commit sucide and the one posting sucide notes.So i decided to go with two subreddits depression and suicide.
* Scraped the data of reddits containing depression and suicide.I scraped nearly 3000 posts.
* Cleand the data and removed duplicate records and total number of posts left for training was 2000.
* Performed text analysis (both unigram and bigram)  and visulisation of most occuring words in both reddits.
* Performed vectorization (Both Bag of Words and TFIDF Vectorizer) and trained the model using Random Forest Classifier , Xgboost Classifier and MultinomialNB for classification. Multinomial NB with count vectorizer gives the highest accuracy of 72%.
* Also trained the model using  Multilayer Bidirectional LSTM to build a model which has an accuracy of 67 %.

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
* Tensorflow.js
* Multinomial Naive Bayes 



### Usage
* All the dataset used : `Dataset`
* Data Collection code : `Data Collection`
* All The source code / Model Development codes: `Src` 
* All the Pretrained Models : `Models`


`Note:` I have only used only 2000 reddits to train so accuracy is  less , Accuracy can be improved by extracting more data form different other social media sites.


### License

Distributed under the MIT License. See `LICENSE` for more information.<br/>



