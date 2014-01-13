---
layout: default
section: writing
title: Writing
---
<h1>All Recent Posts</h1>
<ul class="posts">
  {% for post in site.posts %}
      <li><a class="posttitle" href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a><br>
      {% if post.categories[0] == 'personal' %}
      <span>Posted in <a class="category" href="{{ post.categories[0] | prepend:"/writing/" | append:"/" }}">{{ post.categories[0] | capitalize | append:" Writing" }}</a> on {{ post.date | date_to_string }} </span>
      {% else %}
      <span>Posted in <a class="category" href="{{ post.categories[0] | prepend:"/writing/" | append:"/" }}">Research Revealed!</a> on {{ post.date | date_to_string }} </span>
      {% endif %}
      {% if post.excerpt %}
          {{ post.excerpt | markdownify }}
      {% else %}
          <p>No excerpt, sorry! Try clicking the title to read the whole post.</p>
      {% endif %}
      </li>
  {% endfor %}
</ul>