# Arabic Movie Genres Multi-Label Classifier

## Objectives:

- [x] scraping the movies data [genres, poster image] from IMDB
- [x] Preprocessing the data
  - [x] cleaning the data (remove additional spaces, lowercase the chars, ..)
  - [x] putting the data into csv file 
  - [x] create onehot encoding of the genres
  - [x] save the data with onehot encoding of the genres 
- [x] Create simple CNN model and train it on the small images
  - [x] Save the model 
- [x] Make prediction script `predict.py` 



## Dependencies 

### Training

- Python 3.x
- Tensorflow 2.0
- Matplotlib: for visualizations
- tqdm: beautiful progress bar for loops
- Pandas: handling .csv files
- Numpy: numerical computations

### Scrapping 

- Python 3.x
- BeautifulSoup: scrapping data
- Pandas



## Make prediction

`predict.py --image <image path>`

## Example 

- Actual Labels

  [Booha](https://www.imdb.com/title/tt0478404/): Comedy, Romance

 

![](/media/kelwa/DEV/Projects/Arabic Movies Poster Multi-lable classification/example.png)

