---
author: "Anish Goyal"
title: "Privacy Policy"
description: "This page details the privacy policy of my website and explains how I handle your data."
summary: "I don't track my users. I only collect default server logs and delete those from time to time."
eyecatcher: "Basically, I don't track you."
tags: [general, privacy, data]
readingtime: "3"
date: 2024-10-13
modified: 2024-10-13
---

## My Commitment to Privacy
*I don’t track you. Here's why you should believe me:*
- **Limited Data Collection**: I only collect standard server logs.
- **Regular Log Purging**: These logs are purged routinely, save for some robot traffic.
- **AWS Server**: Although the website isn't completely self hosted, all digital queries are security encrypted by Cloudflare Tunnel before being sent to the server. Additionally, I do not endorse AWS in any capacity; it merely provides the infrastructure for my site.

## Information I Do Collect

### Web Server Logs
For every request received by my NGINX server, the following information is logged:
- Your IP address
- The HTTP response code for the request
-  `User-agent` and `referrer` headers
- The requested page
- The time of the request

This is all collected by the NGINX logger, according to the default configuration. My website does not use cookies, scripts, or collect any information outside the scope of this. For those of you that *don't* want your IP address logged, I am working on setting up a site node on the Tor network; for now, you can use a proxy.

### Cusdis Comments
The comments below each post on my site is powered by [Cusdis](https://cusdis.com/), a lightweight, private, open source commenting framework. All comments on my site are completely anonymized; however, you can (optionally) supply an email address to be notified if anyone responds to your comment.

## Data Retention
AWS log entries are kept for three days max. Before they are purged, I may retain `User-Agent` request headers that indicate bot activity.

## Usage of Your Information
I utilize server logs primarily to detect Denial of Service (DoS) attacks, monitor bots, and analyze search engine interactions for my personal knowledge.

## Avoiding Unwanted Data Collection
I take specific measures to avoid receiving unnecessary information from users:
- **No Third-Party Content**: My web content does not connect to any third-party services that aren’t governed by this privacy policy. This is enforced through a strict `Content-Security-Policy` HTTP header that blocks third-party content.
- **Controlled Header Information**: While web browsers may share various headers that could contain identifying data, I do not log any HTTP headers not explicitly mentioned in the "Web Server Logs" section. However, I cannot prevent user agents from sending these headers.
- **JavaScript Restrictions**: I have disabled any JavaScript execution on my site through the `Content-Security-Policy` header, ensuring that no scripts can load or run on my pages.
- **TLS Security Measures**: I use an “OCSP Must-Staple” directive in my TLS certificates, which enhances security by preventing user agents from contacting certificate authorities.
- **Referrer Policy**: I employ a `Referrer-Policy: no-referrer` header to prevent any referrer information from being shared when users click on links. 
- **DNS Query Controls**: To avoid speculative DNS queries that could leak information about the current page, I send an `X-DNS-Prefetch-Control: off` header, which is respected by modern browsers.
- **Minimizing User Identifiers**: My website does not transmit network traffic in response to media queries, aside from potentially returning dark image variants based on the `prefers-color-scheme` media query, which is insufficient for unique identification.
- **Security against Content Injection**: I’ve implemented a secure TLS cipher suite to prevent network and Internet service providers from injecting or altering requests.
- **HTTP Security Protocols**: To mitigate risks associated with insecure connections, I use a `Strict-Transport-Security` header and participate in HSTS-Preload lists, enhancing security for users accessing my site.
- **Cloudflare**: I use Cloudflare Tunnel to encrypt all digital queries before they reach the server. This ensures that all data is secure and protected from unauthorized access.
        
## `<EOF>`
Your privacy is important to me, and I strive to maintain a transparent and secure environment. If you have any questions or concerns regarding this policy, please feel free to reach out.