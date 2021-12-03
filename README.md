# CSC492 Visual Design for Deep Learning Concepts

The following videos can be used to aid in visualizing concepts when teaching machine learning. They were created to be used by the University of Toronto Mississauga's CSC311: Introduction to Machine Learning and CSC413: Neural Networks and Deep Learning classes and were made in CSC492: Visual Design for Deep Learning Concepts project course.

# Title Card Generation

```python
title = Text("Attention in RNNs", gradient=(BLUE, GREEN)).scale(1.5)
self.play(Write(title))
self.wait(2)
self.play(FadeOut(title))
```

# Installation

To render videos on your local machine Python and manim must be installed.
See [Manim's installation guide](https://docs.manim.community/en/stable/installation.html)

# Convexity of MLP

https://user-images.githubusercontent.com/6016719/144537920-6170799f-a017-486c-9741-187305143b78.mp4

(This visualization is best to be presented as a gif, but will be a video here)
The video demostrates the convexity of a neural network by swapping two nodes (connected by weights colored with red and blue) and showing that there is a another set of weights which will have the same loss as before the swap.

# Batch Normalization

https://user-images.githubusercontent.com/6016719/144537960-5a5df6c9-34fa-4b73-9e2f-df39d51fa0f0.mp4

# Ravines

# Automatic Differentiation
**Note**: **DO NOT** use Manim 0.12.0 to compile the video as Manim has not patched their bug yet. The video was developed with version 0.11.0 and is the prefered version to compile this video

https://play.library.utoronto.ca/watch/15455bbfd3658caed9048343f8721ddc

# Recurrent Neural Networks

https://user-images.githubusercontent.com/6016719/144537988-d265a734-f0a3-4427-b59a-02b804fb2c98.mp4

This video focuses on the computation process in RNN during training using sentimental analysis. The two major scenes are embedding look up and forward pass computation. The embedding lookup shows how we obtained the vectors representing each word from an embedding (e.g. a custom embedding, GloVe, etc.). After we obtained the input, we focus on the time steps one by one, using ` x_i, h_{t-1} ` along with fixed weights `V, W` to calculate ` h_t `.

# Attention

# Transposed Convolutions
The following videos demonstrate different cases of regular convolutions and their equivalent transposed convolutions. 

## No Padding, Unit Strides Convolution

https://user-images.githubusercontent.com/28056407/144511559-02e33e1e-d62b-4033-ad42-379f9cd62a3d.mp4

This video shows regular and transposed convolutions for the case when there is no padding (0x0) and the stride is 1x1. The input is 5x5 and the kernel is 3x3. First the regular convoltion is setup and the kernel is moved around the input, one stride at a time, creating the 3x3 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created and completed, with the kernel moving around and the transposed output being displayed one stride at a time.

## No Padding, Strided Convolution

https://user-images.githubusercontent.com/28056407/144512003-6d4e351b-f8a9-4b30-a4f4-1e415471e729.mp4

This video shows regular and transposed convolutions for the case when there is no padding and the stride is 2x2. The input is 4x4 and the kernel is 2x2. First the regular convoltion is setup and the kernel is moved around the input, one stride (of two units) at a time, creating the 2x2 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created and completed, including the necessary 1x1 stride padding, with the kernel moving around and the transposed output being displayed one stride at a time.

## Padding, Unit Strides Convolution

https://user-images.githubusercontent.com/28056407/144511030-15149988-c2eb-498f-8a42-c7ed2f062b03.mp4

This video shows regular and transposed convolutions for the case when there is 1x1 padding and the stride is 1x1. The input is 3x4 and the kernel is 2x2. First the regular convoltion is setup and the kernel is moved around the input, one stride at a time, creating the 4x5 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created and completed, with the kernel moving around and the transposed output being displayed one stride at a time.

## Padding, Strided Convolution

https://user-images.githubusercontent.com/28056407/144512566-4678b403-4a39-48c2-aec9-0260028d7612.mp4

This video shows regular and transposed convolutions for the case when there is 1x1 padding and the stride is 2x2. The input is 3x4 and the kernel is 3x3. First the regular convoltion is setup and the kernel is moved around the input, one stride (of two units) at a time, creating the 2x2 output. Upon completion, the regular convoltion is moved to the left and then the equivilant transposed convoution is created and completed, including the necessary 1x1 stride padding and 0x1 additional padding, with the kernel moving around and the transposed output being displayed one stride at a time.

# Acknowledgements

The video animations were created using [the community version of Manim](https://github.com/ManimCommunity/manim).

[A guide to convolution arithmetic for deep learning](https://github.com/vdumoulin/conv_arithmetic) was heavily referenced when completing the transposed convolution videos.


