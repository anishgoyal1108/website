---
author: "Anish Goyal"
title: "How This Site Was Made"
description: "A page describing how this website was made."
summary: "This page details the entire stack on which this website was made, including the layout, posts, and automation, using Hugo, GitHub Actions, and an AWS server."
eyecatcher: "Discover the tech stack that powers this website."
tags: [general, backend, hugo, aws, nginx, github-actions]
readingtime: "5"
date: 2024-10-12
modified: 2024-10-13
---

## Overview

This post details the creation and technology stack behind my personal website, built with a focus on minimalism, privacy, and accessibility. The site is powered by [Hugo](https://gohugo.io/), a fast and flexible static site generator that allows for seamless deployment and management of content. You can also check out the [privacy policy](/blog/privacy-policy) to learn more about how I use your data.

### Key Features

- **Minimalistic Design**: The site features a clean and straightforward layout, prioritizing ease of navigation and readability.
- **Privacy-Focused**: I have intentionally avoided third-party tracking, invasive ads, and unnecessary JavaScript, ensuring a safe browsing experience.
- **Automated Deployment**: By utilizing GitHub Actions, my blog posts and content are automatically synchronized from my Obsidian Vault and deployed with ease.
- **Fast and Secure Hosting**: The website is hosted on **AWS**, with an **NGINX** server backend, allowing for efficient and secure delivery of content.

### Technologies Used

- **Hugo**: The backbone of my website, providing a powerful static site generation framework.
- **HTML and CSS**: Core technologies for creating the site’s clean and minimalistic design.
- **Obsidian Vault**: This is my personal knowledge management tool, where I write and store blog posts, which are synchronized to the website.
- **GitHub Actions**: Automates the deployment process, ensuring that any new content is seamlessly published.
- **AWS (Amazon Web Services)**: Hosting provider for my website, offering reliable and scalable infrastructure.
- **NGINX**: Acts as the web server, efficiently handling requests and serving content.
- **Cloudflare**: Manages DNS and provides a CDN for optimized content delivery.
- **Git**: Revision control system for managing changes to the website content.
- **Obsidian**: Personal knowledge management tool for writing and organizing blog posts.

## The IndieWeb Movement
This website follows the principles behind the [IndieWeb movement](https://indieweb.org/), which advocates for decentralized personal websites that prioritize content clarity and user ownership. The IndieWeb movement emphasizes the importance of owning your content and data, rather than relying on third-party platforms. By hosting my website on AWS and using Hugo to generate static content, I maintain full control over my online presence and ensure that my readers can access my content without any intermediaries. I would have went fully self-hosted instead of deploying to an AWS server if I could, but I am on campus and the network blocks incoming connections. 


## Continuous Deployment
This website is continuously deployed using GitHub Actions, which automates the process of updating content and deploying changes.

### My Workflow
My content creation and deployment workflow revolves around a git revisioning system. I use Obsidian to manage all content on the website, as well as notes in my personal life. This allows for easy organization and editing of blog posts before they go live.

Once I’ve completed a blog post, I commit my changes to Git and push them to the repository. My automated GitHub Actions deployment script, which looks like this:

```yaml
name: CI
on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Hugo setup
        uses: peaceiris/actions-hugo@v3.0.0
        with:
          hugo-version: latest
          extended: false
          
      - name: Build
        run: hugo --environment production
        
      - name: Deploy via Rsync Deployments Action
        uses: Burnett01/rsync-deployments@7.0.1
        with:
          switches: -avzr --delete
          path: public/
          remote_path: ${{ secrets.REMOTE_PATH }}
          remote_host: ${{ secrets.REMOTE_HOST }}
          remote_user: ${{ secrets.REMOTE_USER }}
          remote_key: ${{ secrets.DEPLOY_KEY }}

      - name: Create SSH key file
        run: |
          echo "${{ secrets.DEPLOY_KEY }}" > ssh_key
          chmod 600 ssh_key

      - name: Restart NGINX
        run: |
          ssh -o StrictHostKeyChecking=no -i ssh_key ${{ secrets.REMOTE_USER }}@${{ secrets.REMOTE_HOST }} 'sudo systemctl restart nginx'

      - name: Test Success
        uses: rjstone/discord-webhook-notify@v1
        if: success()
        with:
          severity: info
          details: Website deployment successful!
          webhookUrl: ${{ secrets.DISCORD_WEBHOOK }}
          
      - name: Test Failure
        uses: rjstone/discord-webhook-notify@v1
        if: failure()
        with:
          severity: error
          details: Website deployment failed!
          webhookUrl: ${{ secrets.DISCORD_WEBHOOK }}
          
      - name: Test Canceled
        uses: rjstone/discord-webhook-notify@v1
        if: cancelled()
        with:
          severity: warn
          details: Warning while deploying website!
          webhookUrl: ${{ secrets.DISCORD_WEBHOOK }}
```

This workflow synchronizes content from the Obsidian Vault, builds the website using Hugo, and deploys it via rsync to my AWS server. It even restarts NGINX to ensure that changes are reflected immediately. If there are any issues during deployment, I receive notifications through a Discord webhook, allowing me to address problems promptly.

## Accessibility and Inclusive Design

### Accessibility
Accessibility is a cornerstone of my website design philosophy. I intentionally avoided using JavaScript, creating a static site that is easier for users with outdated browsers or those accessing the site through parsers or RSS feeds. As highlighted by the [HTML Hobbyist](https://www.htmlhobbyist.com):

> You were able to land on this website and just start reading… how refreshing was that? No layout shifts caused by loading ads. No begging for you to allow web notifications. No pop-up appeals to sign up for our newsletter. Just simple, relatively unadulterated HTML.


### Inclusivity
I strive to create a design that is inclusive for everyone. My primary focus is on supporting underrepresented ways to read a page. Many users don’t interact with a website through a standard web browser. They may be using accessibility tools, navigating on small viewports, or utilizing machine translators. Others may access the site on restricted networks or through uncommon browsers. Acknowledging these diverse needs is crucial to fostering a truly inclusive digital environment.

One of the core principles I embrace is inclusivity by default. Web pages should not rely on overlays or other personalization features if the underlying design can accommodate all users from the outset. Personalization should serve as a fallback rather than the primary solution. For instance, users on the Tor network, students using school computers, or individuals in restrictive corporate environments should not have to "make websites work for them"; that responsibility lies with me as the webmaster.

Moreover, I believe in the idea of restricted enhancement, which limits all design enhancements to those that address specific accessibility, security, performance, or significant usability challenges faced by users. This approach encourages the use of older or widely-supported features while minimizing purely cosmetic changes. I focus on maintaining a textual website that is maximally inclusive by emphasizing semantic HTML (POSH) and keeping unnecessary complexities at bay. 

**Other than the commenting system for posts, is not a single line of Javascript on this website, and I aim to keep it that way.**

## Commenting System
I use [Cusdis](https://cusdis.com/) for the commenting system on my website. Cusdis is a privacy-friendly, open-source commenting system that doesn't track users or require them to sign in. It's lightweight, easy to integrate, and respects user privacy, making it an ideal choice for my privacy-focused website. To include Cusdis on my site, I simply added the following code snippet to my Hugo `single.html` layout:

```html
  <h4>Comments:</h4>
  <div id="cusdis_thread" data-host="https://cusdis.com"
    data-app-id="REDACTED FOR SECURITY"
    data-page-id="{{ .File.UniqueID }}"
    data-page-url="{{ .Permalink }}"
    data-page-title="{{ .Title }}"
    data-theme="dark">
  <script async src="https://cusdis.com/js/cusdis.es.js"></script>
  <script defer>window.CUSDIS_LOCALE = { powered_by: ' ',}</script>
```

## Front Matter Variables
I use customized front matter variables in my Hugo content files to provide metadata about each post. These variables include:

- *Eyecatcher* - A brief description of the post "to catch the eye" of the reader
- *Tags* - A list of tags that categorize the post
- *Reading Time* - An estimate of the time required to read the post
- *Publication Date* - The date the post was published
- *Modified Date* - The date the post was last modified
  - I use the "Obsidian Linter" plugin to automatically populate the last modified date
- *Summary* - A concise summary of the post's content (not actually displayed anywhere on the site, but used by search engines and RSS feeds)
- *Description* - A brief description of the post (used for meta tags and social media sharing)

Here is an example of the front matter for this post:
```yaml
author: "Anish Goyal"
title: "How This Site Was Made"
description: "A page describing how this website was made."
summary: "This page details the entire stack on which this website was made, including the layout, posts, and automation, using Hugo, GitHub Actions, and an AWS server."
eyecatcher: "Discover the tech stack that powers this website."
tags: [general, backend, hugo, aws, nginx, github-actions]
readingtime: "5"
date: 2024-10-12
modified: 2024-10-13
```

## Hugo Theme
I used the [hugo-simple](https://github.com/maolonglong/hugo-simple) theme to create this website, but it is so heavily modified that it is essentially a custom theme at this point. The theme provides a clean and minimalistic design that aligns with my preferences for a simple and easy-to-navigate layout. I have customized the theme extensively to suit my needs, including modifying the layout, typography, and color scheme to create a unique and personalized look for my website. It's also worth noting that the theme is designed to be lightweight and fast-loading, ensuring a smooth browsing experience for visitors.

## `<EOF>`
If you're interested in the source code for this website, you can find it on my projects page, or [this GitHub repository](https://github.com/anishgoyal1108/website). I believe that by keeping the site lightweight and user-friendly, I can create a better experience for my readers while also reflecting my interests in minimalism, privacy, and cybersecurity.