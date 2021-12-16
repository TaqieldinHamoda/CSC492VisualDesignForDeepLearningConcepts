# CSC492 Visual Design for Deep Learning Concepts

The following videos are provided as visual aid for deep learning concepts. They were created to be used by the **University of Toronto Mississauga**'s *CSC311: Introduction to Machine Learning* and *CSC413: Neural Networks and Deep Learning classes*. These videos were created in *CSC492: Visual Design for Deep Learning Concepts* project course.

**These videos are free to be used by anyone as long as the work produced using them is freely available online and the original project is referenced appropriately.**

# Contents

* [Installation](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts#installation)
  * [Installing Manim](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts#installing-manim)
  * [Rendering the Videos](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts#rendering-the-videos)
* [Attention](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts#attention)
* [Automatic Differentiation](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts#automatic-differentiation)
* [Batch Normalization](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts#batch-normalization)
* [Convexity of MLP](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts#convexity-of-mlp)
* [Ravines](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts#ravines)
* [Recurrent Neural Networks](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts#recurrent-neural-networks)
* [Transposed Convolutions](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts#transposed-convolutions)
  * [No Padding, Unit Strides Convolution](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts#no-padding-unit-strides-convolution)
  * [No Padding, Strided Convolution](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts#no-padding-strided-convolution)
  * [Padding, Unit Strides Convolution](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts#padding-unit-strides-convolution)
  * [Padding, Strided Convolution](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts#padding-strided-convolution)
* [Acknowledgements](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts#acknowledgements)
* [Authors](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts#authors)

# Installation

## Installing Manim
In order to render the videos, Manim must be installed.
Please see [Manim's installation guide](https://docs.manim.community/en/stable/installation.html) for more information.

**Note**: **DO NOT** use Manim 0.12.0 to render the videos as it is unstable at the time of uploading this README. The videos were developed with Manim 0.11.0 and it is the prefered version to render the videos with.

**Note**: since Latex is used in the videos rendered, the [optional dependencies](https://docs.manim.community/en/stable/installation/linux.html#optional-dependencies) must be installed as well.

## Rendering the Videos
To render the videos, you must have access to a terminal and ensure that you are in the directory of your desired video.

Manim provides a rich command-line tool to assist in rendering the scenes. In order to render a video, you must tell Manim the **name of the file** and the **Class** that should be rendered.

Here is an example showing how to render the Attention video:

480p 15fps: `manim -ql attention.py Attention`

1080p 60fps: `manim -qh attention.py Attention`

**Please see Manim's [Configuration Page](https://docs.manim.community/en/stable/tutorials/configuration.html) for more information on rendering videos.**

# Attention
https://user-images.githubusercontent.com/46078134/146457932-0780aae3-3ff7-4cf2-b79a-b4ea2de964c6.mp4

This video demonstrates how attention is used alongside RNNs. Both the encoder (bottom layer) and the decoder (upper layer) units are fully trained
and the weights have been optimized for the translation task presented: translating from English to Spanish. The previous output of the decoder is used alongside the outputs produced from the encoder to calculate the *alpha* (or *attention*) vector. The *alpha* vector provides a weight for each of the encoder's hidden units which helps the decoder determine which hidden unit (read **word**) to **pay more attention to** when determining the correct output.

In the first iteration, the *alpha* vector gives the first hidden unit ("I") a weight of 0.12, the second hidden unit ("Eat") a weight of 0.88, and the third hidden unit ("Apples") a weight of 0.00. This allows the decoder to determine that the word it should output is the Spanish equivalent of the word "eat" and that it is conjucated for the pronoun "I"; as such, "Como" is the output provided.

In the second iteration, the *alpha* vector gives the first hidden unit ("I") a weight of 0.00, the second hidden unit ("Eat") a weight of 0.01, and the third hidden unit ("Apples") a weight of 0.99. Using the previous output ("Como") and the context vector, the decoder is able to determine that the word it should output next is the Spanish equivalent of the word "Apples" and that it should ignore the other English words provided; as such, "Manzanas" is the output provided.

## Raw Video (No Captions)
https://user-images.githubusercontent.com/46078134/145479213-9ca9cfe5-aaab-45ee-8acf-581d16edbbf8.mp4

# Automatic Differentiation

*This Video is a lower quality version (480p, 15fps). A [higher quality version](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts/blob/main/videos/autodiff_high.mp4) can be found in the videos folder*


https://user-images.githubusercontent.com/6016719/145688934-fb0c5df4-d632-4eee-910e-12e03c27434f.mp4



This video demonstrates the forward and backward pass computations using automatic differentiation. The first scene shows the decomposition of the loss function downwards until z1 and z2. The values are placed in the neurons as the forward pass calculations are computed. As the backward pass computations are happening, different edges of the network glow red to show the path the error signal takes. 

# Batch Normalization

https://user-images.githubusercontent.com/6016719/144537960-5a5df6c9-34fa-4b73-9e2f-df39d51fa0f0.mp4

This video demonstrates computing the forward pass compuation of a batch normalization layer of a neural network. First the video shows how data is divided into three batches and passed as input to the network. The video only shows the calculations for the first batch to show how the computations are done. We show the hidden activations for each example in green and how they are normalized using the mean and standard deviation. These values are used in the next scene where the normalized activations are calculated and put inside the neurons of the network.

# Convexity of MLP

https://user-images.githubusercontent.com/6016719/144537920-6170799f-a017-486c-9741-187305143b78.mp4

The video demonstrates that a neural network is neither convex nor concave by swapping two hidden activations h1 and h2 (connected by weights colored blue and red respectively). The corresponding entries in the weight matrices for h1 and h2 are also swapped. It shows that there exists another permutation of weights that will have the same prediction (and therefore the same loss) as before swapping the hidden activations h1 and h2. In the loss space, there will be multiple minimum loss as a result, hence a neural network is neither convex nor concave.

# Ravines

https://user-images.githubusercontent.com/46078134/145517219-9e730257-17bb-4a88-8db6-a519b2fd1fda.mp4

This video demonstrates the impact of normalizing the input on the weight space. The dataset provided has a large difference between the *x1* and *x2* values. As such, the standard deviation is extremely large which results in a ravine in the weight space: the range of values is extremely narrow for one of the weights and extremely wide for the other. One way to resolve this issue, is to normalize the inputs such that they have a **mean of 0** and a **standard deviation of 1**; this will result in a more balanced weight space as seen later on.

# Recurrent Neural Networks


https://user-images.githubusercontent.com/6016719/145839544-0202adcf-2be0-4c2d-a54a-e4675256fc94.mp4



This video focuses on the computation process in RNN during training using sentimental analysis. The purpose of this video is to provide an example of the forward pass process of RNN with concrete numbers. This example has a target t = [1, 0] (happy). The two major scenes are embedding look-up and forward pass computation. The embedding lookup shows how we obtained the vectors representing each word from an embedding (e.g. a custom embedding, GloVe, etc.). After we obtain the input, we focus on the time steps one by one, using x^(I), h^{(t-1)} along with fixed weights V, W to calculate h^{(t)}. The calculation scenes are zoomed-in & only the variables needed are presented to eliminate any distracting elements. The inputs x^{(i)} and hidden units h^{(t)} are colored to show the correlation between the symbols and matrices in the calculation. After we calculated the hidden activation h^{(3)}, we pass the value to a MLP, which will then output the prediction y = [2.1, 0.5].

# Transposed Convolutions
The following videos demonstrate different cases of regular convolutions and their equivalent transposed convolutions. The relationship between the input/output dimensions of the regular and transposed convolutions and how to calculate the dimensions of the transposed convoltion from the regular convolution dimensions is shown.

## No Padding, Unit Strides Convolution

https://user-images.githubusercontent.com/28056407/144645614-d857606a-be06-4b7f-b66b-f545fa77e3b7.mp4

This video shows regular and transposed convolutions for the case when there is no padding (0x0) and the stride is 1x1. The input is 5x5 and the kernel is 3x3. First the regular convoltion is setup and the kernel is moved around the input, one stride at a time, creating the 3x3 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created with a 3x3 input and 2x2 padding, with the kernel moving around and the transposed 5x5 output being displayed one stride at a time.

## No Padding, Strided Convolution

https://user-images.githubusercontent.com/28056407/144645572-27c0d116-b6e6-40e6-9a8a-91746a1206f6.mp4

This video shows regular and transposed convolutions for the case when there is no padding and the stride is 2x2. The input is 4x4 and the kernel is 2x2. First the regular convoltion is setup and the kernel is moved around the input, one stride (of two units) at a time, creating the 2x2 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created with a 2x2 input, 1x1 stride padding, and 1x1 padding, with the kernel moving around and the transposed 4x4 output being displayed one stride at a time.

## Padding, Unit Strides Convolution

https://user-images.githubusercontent.com/28056407/144645697-c195c563-f7a9-4f31-a313-1851dcdef146.mp4

This video shows regular and transposed convolutions for the case when there is 1x1 padding and the stride is 1x1. The input is 3x4 and the kernel is 2x2. First the regular convoltion is setup and the kernel is moved around the input, one stride at a time, creating the 4x5 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created with a 4x5 input, with the kernel moving around and the transposed 3x4 output being displayed one stride at a time.

## Padding, Strided Convolution

https://user-images.githubusercontent.com/28056407/144645654-df1a8d92-8c5f-45f5-ae3a-34c5c305b8b3.mp4

This video shows regular and transposed convolutions for the case when there is 1x1 padding and the stride is 2x2. The input is 3x4 and the kernel is 3x3. First the regular convoltion is setup and the kernel is moved around the input, one stride (of two units) at a time, creating the 2x2 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created with 2x2 input, 1x1 stride padding, 1x1 padding, and 0x1 additional padding, with the kernel moving around and the transposed 3x4 output being displayed one stride at a time.

# Acknowledgements

The video animations were created using [the community version of Manim](https://github.com/ManimCommunity/manim).

[A guide to convolution arithmetic for deep learning](https://github.com/vdumoulin/conv_arithmetic) was heavily referenced when completing the transposed convolution videos.

# Authors

Taqieldin Hamoda

Riley Hannigan

Riddesh Shah

Yiqi (Scott) Shen
