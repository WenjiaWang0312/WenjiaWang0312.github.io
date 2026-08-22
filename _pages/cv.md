---
layout: archive
title: ""
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

{% include cv-template.html %}

<div class="cv-download-links">
  <a id="cv-download" href="{{ base_path }}/files/cv.pdf" class="btn btn--primary" download>Download CV as PDF</a>
  <span>Password hint: cellphone number</span>
</div>

<script>
  document.getElementById('cv-download').addEventListener('click', function (event) {
    const password = window.prompt('Enter password:');
    if (password !== '18930515152') {
      event.preventDefault();
      if (password !== null) {
        window.alert('Incorrect password.');
      }
    }
  });
</script>
