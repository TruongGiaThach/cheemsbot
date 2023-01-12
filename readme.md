<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/TruongGiaThach/cheemsbot">
    <img src="assets/CheemsIcons.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Cheemsbot from Rasa</h3>

  <p align="center">
    Powered by <b>Rasa Open Source</b> | To assist in e-commerce support conversations
    <br />
    <a href="https://rasa.com/docs/rasa/glossary"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="">View Demo</a>
    ·
    <a href="https://github.com/TruongGiaThach/cheemsbot/issues">Report Bug</a>
    ·
    <a href="https://github.com/TruongGiaThach/cheemsbot/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![CheemsBot](https://i.imgur.com/bnAOaY1.png)

A chatbot capable of reading, deciphering intents from user messages, and output appropriate responses based on it.

Assist in searching for products and narrowing down searches through conversations.

Place orders and track the status of an order.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* Rasa Open Source 3.3
* [![Rasa][Python.js]][Python-url]

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* Install rasa 3.3.3
    ```sh
    pip3 install rasa==3.3.3
    ```
* Install python 3.8.0+

* Create a new virtual environment by choosing a Python interpreter[v.3.8.0] and making a ./venv directory to hold it
    ```sh
    python3 -m venv ./venv
    ```
* Activate virtual env
  ```sh
  venv/Scripts/activate
  source ./venv/bin/activate
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/TruongGiaThach/cheemsbot.git
   ```
2. Activate virtual env

3. Mount the model `(models/20220716-025700-trusting-normal.tar.gz)`

4. Run the rasa shell command
    ```sh
    rasa shell
    ```
<p align="right">(<a href="#top">back to top</a>)</p>

### Run this repo
```sh
rasa run  --cors "*" --enable-api

rasa run actions
```



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

## Run cheemsbot:
 
```shell
docker compose up
rasa run actions --auto-reload
```
 
```shell
rasa run shell
```

```
rasa run  --cors "*" --enable-api
```




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/shreyasdatta/e-Commerce-chatbot-rasa.svg?style=for-the-badge
[contributors-url]: https://github.com/shreyasdatta/e-Commerce-chatbot-rasa/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/shreyasdatta/e-Commerce-chatbot-rasa.svg?style=for-the-badge
[forks-url]: https://github.com/shreyasdatta/e-Commerce-chatbot-rasa/network/members
[stars-shield]: https://img.shields.io/github/stars/shreyasdatta/e-Commerce-chatbot-rasa.svg?style=for-the-badge
[stars-url]: https://github.com/shreyasdatta/e-Commerce-chatbot-rasa/stargazers
[issues-shield]: https://img.shields.io/github/issues/shreyasdatta/e-Commerce-chatbot-rasa.svg?style=for-the-badge
[issues-url]: https://github.com/shreyasdatta/e-Commerce-chatbot-rasa/issues
[license-shield]: https://img.shields.io/github/license/shreyasdatta/e-Commerce-chatbot-rasa.svg?style=for-the-badge
[license-url]: https://github.com/shreyasdatta/e-Commerce-chatbot-rasa/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ShreyasDatta
<!-- [product-screenshot]: https://i.imgur.com/bnAOaY1.png -->


[Python.js]: https://img.shields.io/badge/python-3.8-brightgreen
[Python-url]: https://www.python.org/downloads/release/python-380/
