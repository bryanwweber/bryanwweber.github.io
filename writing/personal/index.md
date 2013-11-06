---
layout: default
title: Personal Writing
section: writing personal
---
  <h1>All posts categorized as Personal Writing.</h1>
  <ul class="posts">
    {% for post in site.categories.personal %}
      <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
      {% if post.content contains '<!--more-->' %}
          {{ post.content | split:'<!--more-->' | first }}
      {% else %}
          <p>No excerpt, sorry! Try clicking the title to read the whole post.</p>
      {% endif %}
    {% endfor %}
  </ul>