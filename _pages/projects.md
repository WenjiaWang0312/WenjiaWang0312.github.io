---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

## Codebases

<div class="projects-list">
  <article class="project-card">
    <a class="project-card__media-link" href="https://github.com/open-mmlab/mmhuman3d">
      <img class="project-card__media" src="/assets/mmhuman3d.gif" alt="MMHuman3D preview" />
    </a>
    <div class="project-card__content">
      {% assign mmhuman3d_stats = site.data.github_stats.mmhuman3d %}
      <h3 class="project-card__title"><a href="https://github.com/open-mmlab/mmhuman3d">MMHuman3D</a></h3>
      {% if mmhuman3d_stats.stars %}
        <p class="project-card__meta">
          <a href="https://github.com/open-mmlab/mmhuman3d/stargazers" target="_blank" rel="noopener noreferrer">
            <i class="fas fa-star" aria-hidden="true"></i>{{ mmhuman3d_stats.stars }} stars
          </a>
        </p>
      {% endif %}
      <p class="project-card__description">
        MMHuman3D is an open source PyTorch-based codebase for working with 3D human parametric models as part of the OpenMMLab project.
      </p>
      <ul class="project-card__highlights">
        <li>Reproducing popular methods with a modular framework</li>
        <li>Supporting various datasets with a unified data convention</li>
        <li>Versatile visualization toolbox</li>
      </ul>
    </div>
  </article>
</div>
