<h1 align="center">
    UrlShortener
</h1>

<p align="center">
  <a href="#-project">Project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rocket-technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#information_source-how-to-run">How to run</a>&nbsp;&nbsp;&nbsp;

</p>

<br>

## 💻 Project

This is just a very simple scrip to manipulate images.

## :rocket: Technologies

This app was made using the following technologies:
- [Python][python]
- [Pip][pip]
- [OpenCV][opencv]
- [NumPy][numPy]
## :information_source: How To Run

To clone and run this application, you'll need [Git](https://git-scm.com) + [Python3][python] + [Pip][pip] installed on your computer.

### Clone and Run the server

<br/>

```bash
# Clone this repository
$ git clone https://github.com/lucastssb/pyImage.git
$ git clone git@github.com:lucastssb/pyImage.git

# Go into the repository
$ cd pyImage

# Install dependencies
$ pip install -r requirements.txt


```

### Manipulate images

You can use flags to manipulate the image.
The first flag is the path to the image and second tells the app what to do with it.

<br/>
Example:

```bash
# Split the image and save the green channel of it in the same folder
$ python app.py image.jpg -g
```
If everything worked out you will find a new image in the same folder as the `app.py` is located.

```bash
# Invert the color of the image and save of it in the same folder
$ python app.py image.jpg -invert
```
### You can also use the following flags
- `-g`: Split the image and save the green channel of it in the same folder
- `-b`: Split the image and save the blue channel of it in the same folder
- `-r`: Split the image and save the red channel of it in the same folder
- `-invert`: Invert the color of the image and save of it in the same folder
- `-gray_scale`: Convert the image to gray scale and save of it in the same folder
- `-rgb`: Split the image into its red, green and blue channels then merge the channels and save in the same folder

<br>

Made with ♥ by Lucas Barbosa :wave: [Get in touch!](https://www.linkedin.com/in/lucas-barbosa-60b56416b/)

[python]: https://www.python.org/
[pip]: https://pip.pypa.io/en/stable/
[opencv]: https://opencv.org/
[numPy]: https://numpy.org/

