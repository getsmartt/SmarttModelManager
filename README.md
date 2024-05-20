<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<h3 align="center">Smartt Model Manager</h3>

  <p align="center">
    a 'Mod Organizer' for AI models
    <br />
    <a href="https://github.com/github_username/repo_name/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## This is a very early beta of a 'model' manager for AI models. 

It is designed to help manage the various versions of models that are used in a project. 
Think of it as a ModOrganizer or Vortex Mod Managed for AI models.  Essentially it is a central repository for all 
(most?) of your CivitAi (and other i.e Hugging Face) models.  You can deploy these models to specific AI software 
(A1111, ComfyUI, etc) .

You would be able to store all your models in a separate location from your software, and deploy them as needed.  
Plans are to use soft-links where applicable.  It is desktop software, and only deploys locally at this point.

Eventually it will have a live interface to CivitAI to download and monitor models.

Note: This is my first 'major' Python project and I am learning as I go, there is a lot of non-pythonic code here.  
There is a lot of repeated code that eventually needs to be moved to functions/classes/etc.  
I have done similar things in different ways in various places of the program.  Sometimes because I learned something
new/better, sometimes because I forgot I had done it before.  I am working on cleaning it up as I go.  
Some code is documented, some is not.  I am working on that as well.  I am also working on adding more comments to 
the code.


<!-- ROADMAP -->
## Roadmap
Lots to do here...
- [ ] Edit models
- [ ] Separate models from versions
- [ ] build deployment
- [ ] build model downloader
- [ ] tag manager
- [ ] better filter bar
- [ ] manual image adder

- [ ] Scanner/Searcher
    - [ ] auto update
    - [ ] flag and download
    - [ ]  auto download
    - [ ]   fetch update status

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

James Smartt - [@getsmartt](https://twitter.com/getsmartt)

Project Link: [https://github.com/getsmartt/SmarttModelManager](https://github.com/getsmartt/SmarttModelManager)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template/tree/master)
* [Civitai.com API Package](https://github.com/kopetri/civitai)
* [A collection of .gitignore templates](https://github.com/github/gitignore/tree/main)
* [Hands-on guides to Python GUI programming](https://www.pythonguis.com/pyside6/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/getsmartt/SmarttModelManager.svg?style=for-the-badge
[contributors-url]: https://github.com/getsmartt/SmarttModelManager/graphs/contributors
[forks-shield]: https://img.shields.io/github/forksgetsmartt/SmarttModelManager.svg?style=for-the-badge
[forks-url]: https://github.com/getsmartt/SmarttModelManager/network/members
[stars-shield]: https://img.shields.io/github/stars/getsmartt/SmarttModelManager.svg?style=for-the-badge
[stars-url]: https://github.com/getsmartt/SmarttModelManager/stargazers
[issues-shield]: https://img.shields.io/github/issues/getsmartt/SmarttModelManager.svg?style=for-the-badge
[issues-url]: https://github.com/getsmartt/SmarttModelManager/issues
[license-shield]: https://img.shields.io/github/license/getsmartt/SmarttModelManager.svg?style=for-the-badge
[license-url]: https://github.com/getsmartt/SmarttModelManager/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/james-smartt
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
