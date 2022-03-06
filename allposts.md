---
title: "過去の記事一覧"
permalink: /allposts
---

{% assign year=9999 %}
{% for post in site.posts %}
    {% assign postyear = post.date | date: "%Y" %}
    {% if postyear != year %}
        {% assign year=postyear %}
## {{year}}
    {% endif %}

- [{{ post.title }}]({{post.url}})

{% endfor %}
