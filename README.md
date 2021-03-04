<div align="center">

# AI For Social Good

## Suicidal Ideation Detection In Online Social Content

</div>

---

## Getting Started

The rise of social media and online communities creates safe and anonymous spaces for individuals to share their thoughts about their mental health and express their feelings and sufferings in online communities. In order to prevent suicide, it is necessary to detect suicide-related posts and users' suicide ideation in cyberspace by natural language processing methods. I focused on the online community called Reddit and the social networking website Twitter, and classify users' posts with potential suicide and without suicidal risk through texts features processing , machine learning and deep learning based methods.

## Datasets

Collected two sets of data from Reddit and Twitter. The Reddit data set includes (2958) suicidal ideation samples and a number of non-suicide texts (5381). The Twitter dataset has totally (3000) tweets with suicidal ideation.
Reddit Data was scraped from subreddits like 'suicide watch' ,'depression', 'anxiety' etc.
Twitter data was collected by quering keywords like 'end my life', 'die' etc.

**The Twitter word cloud (left) and Reddit word cloud (right) are shown as follow:**

<div align="center">
 <img alt="Demo" src="./WordClouds/twitter.png" height="300px" width="400px" />
 &nbsp; &nbsp;
 <img alt="Demo" src="./WordClouds/reddit.png" height="300px" width="400px"/>
</div>

## Feature Processing

- To do this task i scraped two reddits. Mostly people in depression are likely to commit sucide and the one posting sucide notes. So i decided to go with two subreddits depression and suicide.
- Scraped the data of reddits containing depression and suicide. I scraped nearly 3000 posts.
- Cleand the data and removed duplicate records and total number of posts left for training was 2000.
- Performed text analysis (both unigram and bigram) and visulisation of most occuring words in both reddits.
- Performed vectorization (Both Bag of Words and TFIDF Vectorizer) and trained the model using Random Forest Classifier , Xgboost Classifier and MultinomialNB for classification. Multinomial NB with count vectorizer gives the highest accuracy of 72%.
- Also trained the model using Multilayer Bidirectional LSTM to build a model which has an accuracy of 67 %.

## Results

Part of experimental results as below on

| Model        | Acc.     | Pre.     | Rec.     | F1       | AUC      |
| ------------ | -------- | -------- | -------- | -------- | -------- |
| RF + TFIDF   | 0.941440 | 0.958286 | 0.906931 | 0.931861 | 0.986029 |
| LSTM + GLOBE | 0.961845 | 0.964161 | 0.948894 | 0.956437 | 0.991860 |

## Usage

- `Dataset` : All the collected and cleaned dataset
- `Data_Collection` : Code for scraping data from reddit and twitter
- `Src` : All The source code for text preprocessing and building ml models
- `Pretrained_Models` : All the Pretrained Models and tokenizers:

## License

Distributed under the MIT License. See `LICENSE` for more information.<br/>
