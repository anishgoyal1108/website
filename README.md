# Personal Website

![](https://i.imgur.com/XmeMcrV.gif)

## Overview

This repository contains the source code for my personal website, a minimalist and privacy-conscious static site built using [Hugo](https://gohugo.io/), a fast and flexible static site generator. The site features:

- **Blog posts** and **cybersecurity competition write-ups** synchronized with an Obsidian Vault, deployed automatically using GitHub Actions.
- **Fast content delivery**, with a focus on minimal JavaScript, no intrusive ads, and no user tracking.
- Hosted on **AWS** with a **Caddy** server backend, ensuring efficient and secure site delivery.

The website reflects my interests in minimalism, privacy, and cybersecurity, and is designed to be lightweight and easy to navigate.

## Features

- **Minimalistic Design:** Simple, clean, and easy-to-navigate layout with no unnecessary elements.
- **Privacy-Focused:** No third-party tracking, no invasive ads, and minimal client-side JavaScript.
- **Automated Deployment:** Blog posts are synchronized from an Obsidian Vault and automatically deployed using GitHub Actions.
- **Optimized for Speed:** Built for fast loading times and efficient resource usage using Hugo for static content generation.
- **Secure Hosting:** Deployed on an AWS server with Caddy handling the web server functionalities.
  
## Technologies Used

- **Hugo:** Static site generator used to build the website.
- **HTML, CSS, JS:** Core front-end technologies used for the site’s minimalistic design.
- **Obsidian Vault:** Used to write and store blog posts and write-ups, which are then synchronized and deployed via GitHub Actions.
- **GitHub Actions:** Automates deployment of new content from Obsidian Vault to the web server.
- **AWS (Amazon Web Services):** Hosting and serving the static website content.
- **Caddy:** Web server running in the backend to serve the site and manage HTTPS.

## Continuous Deployment

This repository includes a GitHub Actions workflow that:

- Synchronizes the content from the Obsidian Vault.
- Automatically builds and deploys the site when changes are committed to the repository.
