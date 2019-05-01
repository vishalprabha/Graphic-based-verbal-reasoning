# Graphic based verbal reasoning

Graphic based verbal reasoning is the task of answering natural-language questions about images. Recently the idea of answering question based on the given image has gathered a lot of interest in the research community, however, no significant amount of work has been done. Current models mainly rely on extracting image and question features to learn their joint feature relation. The issue with such kind of approaches is that we do not know if the model architecture is capable of learning the semantic distinction of the given image and question. So we intend to reiterate the whole solution process by building a better deep learning model capable of extracting the features of the image, which is further backed up by an existing object detection model. We further concentrate on `proficient natural language processing techniques to extract relevant semantics from question to answer, unlike the current methods available. So by fusing the capabilities of computer vision by deep learning and natural language processing, we seek to cave into new dimensions of artificial intelligence.

## Dependency

You can install the dependencies from the "requirements.txt" file after creating a virtualenv with python 3.6

> python install -r requirements.txt

In case of issues manually install the below mentioned versions


1. Keras version 2.0+
   * Modular deep learning library based on python

2. Tensorflow 1.2+
    (Might also work with Theano. I have not tested Theano
    after the recent commit, use commit 0f89007 for Theano)

3. scikit-learn 0.18 or lesser
   * Quintessential machine library for python

4. Spacy version 2.0+
    * Used to load Glove vectors (word2vec)
    * To upgrade & install Glove Vectors (Important step don't forget)
       * python -m spacy download en_vectors_web_lg

5. OpenCV
    * OpenCV is used only to resize the image and change the color channels,
    * You may use other libraries as long as you can pass a 224x224 BGR Image (NOTE: BGR and not RGB)

6. VGG 16 Pretrained Weights
    * Please download the weights file [vgg16_weights.h5](https://drive.google.com/file/d/0Bz7KyqmuGsilT0J5dmRCM0ROVHc/view)

## iPython Notebook

Jupyter/iPython Notebook has examples and interactive components to understand the working of the various components used

# VQA Training

components to train the VQA model are present in the VQA_Build folder

### Training

The first thing you need to do is to download the data and do some preprocessing. Head over to the `data/` folder and run

```
$ python vqa_preprocessing.py --download True --split 1
```

`--download Ture` means you choose to download the VQA data from the [VQA website](http://www.visualqa.org/) and `--split 1` means you use COCO train set to train and validation set to evaluation. `--split 2 ` means you use COCO train+val set to train and test set to evaluate. After this step, it will generate two files under the `data` folder. `vqa_raw_train.json` and `vqa_raw_test.json`

Once you have these, we are ready to get the question and image features. Back to the main folder, run

```
$ python prepro.py --input_train_json data/vqa_raw_train.json --input_test_json data/vqa_raw_test.json --num_ans 1000
```

to get the question features. `--num_ans` specifiy how many top answers you want to use during training. You will also see some question and answer statistics in the terminal output. This will generate two files in your main folder, `data_prepro.h5` and `data_prepro.json`. To get the image features, run

```
$ th prepro_img.lua -input_json data_prepro.json -image_root path_to_image_root -cnn_proto path_to_cnn_prototxt -cnn_model path to cnn_model
```

Place the following three generated files in the data directory --

	* 'data/data_prepro.json'
	* 'data/data_img.h5'
	* 'data/data_prepro.h5'

To call our DeeperLSTM model pass the argument -model and name of the file.

 For e.g `python train -model DeeperLSTM`

Copy the output to the main directory models to test the VQA


## Usage

> python demo.py -image_file_name `path_to_file` -question "Question to be asked"

e.g

> python demo.py -image_file_name test.jpg -question "Is there a man in the picture?"


Expected Output :
095.2 %  train
00.67 %  subway
00.54 %  mcdonald's
00.38 %  bus
00.33 %  train station


## Runtime

  * CPU (i7-5820K CPU @ 3.30GHz                   : 35.9 seconds (Is this strange or not ?)
