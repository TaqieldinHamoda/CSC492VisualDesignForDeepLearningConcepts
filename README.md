# CSC492 Visual Design for Deep Learning Concepts

The following videos can be used to aid in visualizing concepts when teaching machine learning. They were created to be used by the University of Toronto Mississauga's CSC311: Introduction to Machine Learning and CSC413: Neural Networks and Deep Learning classes and were made in CSC492: Visual Design for Deep Learning Concepts project course.

# Installation

## Installing Manim
In order to render the videos, Manim must be installed.
Please see [Manim's installation guide](https://docs.manim.community/en/stable/installation.html) for more information.

Note that since Latex is used in the videos rendered, the [optional dependencies](https://docs.manim.community/en/stable/installation/linux.html#optional-dependencies) must be installed as well.

## Rendering the Videos
To render the videos, you must have access to a terminal and ensure that you are in the directory of your desired video.

Manim provides a rich command-line tool to assist in rendering the scenes. In order to render a video, you must tell Manim the **name of the file** and the **Class** that should be rendered.

The following is an example command for rendering the Attention video:

480p 15fps: `manim -ql attention.py Attention`

1080p 60fps: `manim -qh attention.py Attention`

**Please see Manim's [Configuration Page](https://docs.manim.community/en/stable/tutorials/configuration.html) for more information on rendering videos.**

# Attention

https://user-images.githubusercontent.com/46078134/145479213-9ca9cfe5-aaab-45ee-8acf-581d16edbbf8.mp4

# Automatic Differentiation
**Note**: **DO NOT** use Manim 0.12.0 to compile the video as Manim has not patched their bug yet. The video was developed with version 0.11.0 and is the prefered version to compile this video

*This Video is a lower quality version (480p, 15fps). A [higher quality version](https://github.com/rileyhannigan/CSC492VisualDesignForDeepLearningConcepts/blob/main/videos/Autodiff.mp4) can be found in the videos folder*

https://user-images.githubusercontent.com/46078134/145480699-2256b5fd-0307-406d-a0bf-9d58a7fc5921.mp4

This video demonstrates the forward and backward pass computations using automatic differentiation. The first scene shows the decomposition of the loss function downwards until z1 and z2. The values are placed in the neurons as the forward pass calculations are computed. As the backward pass computations are happening, different edges of the network glow red to show the path the error signal takes. 

# Batch Normalization

https://user-images.githubusercontent.com/6016719/144537960-5a5df6c9-34fa-4b73-9e2f-df39d51fa0f0.mp4

This video demonstrates on computing the batch norm for a neural network. First the video shows how input is split up into batches and passed as input to the network. The hidden values are computed using arbitrary weights and shown in green. The next scene shows the calculation of the mean and variance of the hidden units along each dimension. These values are used in the next scene where the norm is calculated and the normalized values are put inside the neurons of the network.

# Convexity of MLP

https://user-images.githubusercontent.com/6016719/144537920-6170799f-a017-486c-9741-187305143b78.mp4

(This visualization is best to be presented as a gif, but will be a video here)
The video demostrates the convexity of a neural network by swapping two nodes (connected by weights colored with red and blue) and showing that there is a another set of weights which will have the same loss as before the swap.

# Ravines

https://user-images.githubusercontent.com/46078134/145495503-ef1c66f1-9ffa-4e4c-9551-9b24b9359564.mp4

This video demonstrates how ravines can be normalized to be easier to work with, and shows a visual representation of this process. 

# Recurrent Neural Networks

https://user-images.githubusercontent.com/6016719/144537988-d265a734-f0a3-4427-b59a-02b804fb2c98.mp4

This video focuses on the computation process in RNN during training using sentimental analysis. The two major scenes are embedding look up and forward pass computation. The embedding lookup shows how we obtained the vectors representing each word from an embedding (e.g. a custom embedding, GloVe, etc.). After we obtained the input, we focus on the time steps one by one, using ` x_i, h_{t-1} ` along with fixed weights `V, W` to calculate ` h_t `.

# Transposed Convolutions
The following videos demonstrate different cases of regular convolutions and their equivalent transposed convolutions. 

## No Padding, Unit Strides Convolution

https://user-images.githubusercontent.com/28056407/144645614-d857606a-be06-4b7f-b66b-f545fa77e3b7.mp4

This video shows regular and transposed convolutions for the case when there is no padding (0x0) and the stride is 1x1. The input is 5x5 and the kernel is 3x3. First the regular convoltion is setup and the kernel is moved around the input, one stride at a time, creating the 3x3 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created and completed, with the kernel moving around and the transposed output being displayed one stride at a time.

## No Padding, Strided Convolution

https://user-images.githubusercontent.com/28056407/144645572-27c0d116-b6e6-40e6-9a8a-91746a1206f6.mp4

This video shows regular and transposed convolutions for the case when there is no padding and the stride is 2x2. The input is 4x4 and the kernel is 2x2. First the regular convoltion is setup and the kernel is moved around the input, one stride (of two units) at a time, creating the 2x2 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created and completed, including the necessary 1x1 stride padding, with the kernel moving around and the transposed output being displayed one stride at a time.

## Padding, Unit Strides Convolution

https://user-images.githubusercontent.com/28056407/144645697-c195c563-f7a9-4f31-a313-1851dcdef146.mp4

This video shows regular and transposed convolutions for the case when there is 1x1 padding and the stride is 1x1. The input is 3x4 and the kernel is 2x2. First the regular convoltion is setup and the kernel is moved around the input, one stride at a time, creating the 4x5 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created and completed, with the kernel moving around and the transposed output being displayed one stride at a time.

## Padding, Strided Convolution

https://user-images.githubusercontent.com/28056407/144645654-df1a8d92-8c5f-45f5-ae3a-34c5c305b8b3.mp4

This video shows regular and transposed convolutions for the case when there is 1x1 padding and the stride is 2x2. The input is 3x4 and the kernel is 3x3. First the regular convoltion is setup and the kernel is moved around the input, one stride (of two units) at a time, creating the 2x2 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created and completed, including the necessary 1x1 stride padding and 0x1 additional padding, with the kernel moving around and the transposed output being displayed one stride at a time.

# Acknowledgements

The video animations were created using [the community version of Manim](https://github.com/ManimCommunity/manim).

[A guide to convolution arithmetic for deep learning](https://github.com/vdumoulin/conv_arithmetic) was heavily referenced when completing the transposed convolution videos.


