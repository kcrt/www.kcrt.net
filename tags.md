---
title: タグ一覧
---

{% comment %} ===== タグ一覧をPage, Postから抽出 {% endcomment %}
{% assign tagnames = site.pages[0].tags %}

{% comment %} ----- 1. Pageから {% endcomment %}
{% for apage in site.pages %}
    {% assign ntags = apage.tags | size %}
    {% unless ntags == 0 %}
        {% assign tagnames = tagnames | concat: apage.tags | uniq %}
    {% endunless %}
{% endfor %}

{% comment %} ----- 2. Postから {% endcomment %}
{% assign posttagnames = "" %}
{% for tag in site.tags %}
    {% assign posttagnames = posttagnames | append: tag[0] %}
    {% assign posttagnames = posttagnames | append: "," %}
{% endfor %}
{% assign posttagnames = posttagnames | split: "," %}
{% assign tagnames = tagnames | concat: posttagnames | uniq %}

{% comment %} ===== タグ名からページを作成 {% endcomment %}
{% comment %} ----- 0. 目次 {% endcomment %}
## タグ一覧
{% for tag in tagnames %}
- [{{ tag }}](#{{ tag }})
{% endfor %}

{% for tag in tagnames %}

    {% assign tag5 = tag | slice: 0, 6 %}
    {% if tag == "AYOR" or tag5 == "scope:" %}
        {% continue %}
    {% endif %}
    {% assign hasPageItem = false %}

## {{ tag }}
    {% comment %} ----- 1. Pageから {% endcomment %}
    {% for apage in site.pages %}
        {% if apage.tags contains tag %}
            {% if hasPageItem == false %}
### 固定記事
                {% assign hasPageItem = true %}
            {% endif %}
- [{{apage.title}}]({{apage.url}})
        {% endif %}
    {% endfor %}

    {% comment %} ----- 2. Postから {% endcomment %}

    {% for sitetag in site.tags %}
        {% unless sitetag[0] == tag %}
            {% continue %}
        {% endunless %}
        {% if sitetag[1].size >0 %}
            {% if hasPageItem == true %}
### ポスト
            {% endif %}
            {% for post in sitetag[1] %}
- [{{post.title}}]({{ post.url }})
            {% endfor %}
        {% endif %}
        {% break %}
    {% endfor %}

{% endfor %}

