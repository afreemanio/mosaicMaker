# mosaicMaker: Photographic Mosaic Command Line Tool

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<p align="left">
  <p align="left">
    <a href="https://github.com/afreemanio/mosaicMaker/issues">Report Bug</a>
    ·
    <a href="https://github.com/afreemanio/mosaicMaker/issues">Request Feature</a>
    <br />
    <br />
    Photographic Mosaic Command Line Tool
    <br />
    <br />

  </p>

</p>

## Content

<!-- no toc -->

- [mosaicMaker: Photographic Mosaic Command Line Tool](#mosaicmaker-photographic-mosaic-command-line-tool)
  - [Content](#content)
  - [About The Project](#about-the-project)
    - [Built With](#built-with)
    - [Features](#features)
  - [Installation](#installation)
  - [Contributing](#contributing)
  - [Contact](#contact)
  - [License](#license)

<!-- ABOUT THE PROJECT -->

## About The Project

This is a Python project created for my Winter 2021 Semester at the King's University, my final project for CMPT450: Image Processing.

It creates photomosaic images from all images in the "inputImages" folder, based on tiling the specified input on the command line, and saves everything to the outputImages folder.

Next steps are to make it look fancier by adding more pretty command line stuff like help (error codes), proper argument parsing, etc.

Thank you!

<p>
  <a href="https://github.com/afreemanio/mosaicMaker/">
    <img src="https://imgur.com/OXnn6kk.jpg" alt="" width="875">
  </a>
</p>
With a special thanks to Dr. Michael Janzen.
<p align="left">
    <br />
</p>

Photographic mosaics (Photomosaics) are pictures that have been divided into tiled sections, with each tile being replaced with another image that resembles the colour of the tile it replaces. The effect has each pixel in the original image replaced by another distinct image – so at low magnification, the original image appears as normal, but when magnified, one can see that the original picture is made up of many smaller images.

Refer to https://en.wikipedia.org/wiki/Photographic_mosaic for more information on Photographic Mosaics.

### Built With

- [Python 3.9.1](https://www.python.org/)

### Features

- Creation of Photomosaics of specified height and width.
- Automatically uses the best photos from the provided source directory (/tileImages/).
- Automatically adjusts the brightness to ensure accuracy to the source image.
- Works with most common image filetypes! If its supported in Pillow, it's supported here!
- Simple and easy to install and run!


## Installation

1.  Download the repository files (project) directly from the download section or clone this project by entering the following command:

        git clone https://github.com/afreemanio/mosaicMaker.git

2.  Navigate to the repository using your terminal of choice

3.  Add source photos to the tileImages folder that will be the tiles (small pictures) in your Photographic Mosaic

4.  Add source files to the sourceImages folder that will be the main (bigger) photo in your Photographic Mosaic

5.  With Python installed, navigate to /src/, and run it using this format:

    python main.py [image from sourceImages + .ext] [output width] [output height] [number of tiles in x direction] [number of tiles in y direction]

  For example:

    python main.py samuel.jpg 1000 1000 100 100

  To run the program specifying ../sourceImages/samuel.jpg as the base image, 1000x1000 as the width/height of your final Photomosiac, with 100(w)x100(h)=10000 tiles in total.

## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/CoolNewFeature`)
3. Commit your Changes (`git commit -m 'Add some CoolNewFeature'`)
4. Push to the Branch (`git push origin feature/CoolNewFeature`)
5. Open a Pull Request

<!-- CONTACT -->

## Contact

Andrew Freeman - [@afreemanio](https://twitter.com/afreemanio) - andrewfreeman234@gmail.com

Project Link: [https://github.com/afreemanio/mosaicMaker](https://github.com/afreemanio/mosaicMaker)

## License

Copyright (c) 2021 Andrew Freeman

Distributed under and usage provided for under the MIT License. See [LICENSE][license-url] for the full details.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/afreemanio/mosaicMaker.svg?style=for-the-badge
[contributors-url]: https://github.com/afreemanio/mosaicMaker/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/afreemanio/mosaicMaker.svg?style=for-the-badge
[forks-url]: https://github.com/afreemanio/mosaicMaker/network/members
[stars-shield]: https://img.shields.io/github/stars/afreemanio/mosaicMaker.svg?style=for-the-badge
[stars-url]: https://github.com/afreemanio/mosaicMaker/stargazers
[issues-shield]: https://img.shields.io/github/issues/afreemanio/mosaicMaker.svg?style=for-the-badge
[issues-url]: https://github.com/afreemanio/mosaicMaker/issues
[license-shield]: https://img.shields.io/github/license/afreemanio/mosaicMaker.svg?style=for-the-badge
[license-url]: https://github.com/afreemanio/mosaicMaker/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/afreemanio
[product-screenshot]: https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Pierre_ciseaux_feuille_l%C3%A9zard_spock_aligned.svg/1024px-Pierre_ciseaux_feuille_l%C3%A9zard_spock_aligned.svg.png
