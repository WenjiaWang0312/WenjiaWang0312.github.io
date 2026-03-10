---
layout: single
title: "SIMS (Preview)"
permalink: /projects/sims_copy/
author_profile: false
classes: wide
published: false
---

<div class="project-preview">

<div class="project-meta">
  <h2 class="project-meta__title">SIMS: Simulating Stylized Human-Scene Interactions with Retrieval-Augmented Script Generation</h2>
  <p class="project-meta__venue">ICCV 2025 Poster</p>
  <p class="project-meta__authors">
    <a href="https://wenjiawang0312.github.io/">Wenjia Wang</a><sup>1</sup>
    <span>·</span>
    <a href="https://liangpan99.github.io/">Liang Pan</a><sup>1,2</sup>
    <span>·</span>
    <a href="https://frank-zy-dou.github.io/">Zhiyang Dou</a><sup>1</sup>
    <span>·</span>
    <a href="https://blusque.github.io/">Jidong Mei</a><sup>1</sup>
    <span>·</span>
    <a href="https://zycliao.com/">Zhouyingcheng Liao</a><sup>1</sup>
    <span>·</span>
    <a href="https://thorin666.github.io/">Yuke Lou</a><sup>1</sup>
    <span>·</span>
    <a href="https://littlecobber.github.io/">Yifan Wu</a><sup>1</sup>
    <span>·</span>
    <a href="http://yanglei.me/">Lei Yang</a><sup>2</sup>
    <span>·</span>
    <a href="https://wangjingbo1219.github.io/">Jingbo Wang</a><sup>2</sup>
    <span>·</span>
    <a href="https://i.cs.hku.hk/~taku/">Taku Komura</a><sup>1</sup>
  </p>
  <p class="project-meta__affiliations">
    <span><sup>1</sup>The University of Hong Kong</span>
    <span><sup>2</sup>Shanghai AI Laboratory</span>
  </p>
</div>

<div class="project-hero project-hero--teaser">
  <img class="project-hero__image" src="/projects/sims/sims_teaser.png" alt="SIMS teaser" />
</div>

<div class="project-actions project-actions--centered project-actions--brand">
  <a class="btn project-btn project-btn--arxiv" href="https://arxiv.org/abs/2411.19921"><i class="ai ai-arxiv"></i><span>arXiv</span></a>
  <a class="btn project-btn project-btn--github" href="https://github.com/WenjiaWang0312/sims-stylized_hsi"><i class="fab fa-github"></i><span>Code</span></a>
  <a class="btn project-btn project-btn--data" href="https://github.com/WenjiaWang0312/sims-stylized_hsi"><i class="far fa-images"></i><span>Data</span></a>
</div>

<h2 class="project-section-title">Abstract</h2>

<p class="project-abstract">
  Simulating stylized human-scene interactions (HSI) in physical environments is a challenging yet fascinating task. Prior works emphasize long-term execution but fall short in achieving both diverse style and physical plausibility. To tackle this challenge, we introduce a novel hierarchical framework named SIMS that seamlessly bridges high-level script-driven intent with a low-level control policy, enabling more expressive and diverse human-scene interactions. Specifically, we employ Large Language Models with Retrieval-Augmented Generation (RAG) to generate coherent and diverse long-form scripts, providing a rich foundation for motion planning. A versatile multi-condition physics-based control policy is also developed, which leverages text embeddings from the generated scripts to encode stylistic cues, simultaneously perceiving environmental geometries and accomplishing task goals. By integrating the retrieval-augmented script generation with the multi-condition controller, our approach provides a unified solution for generating stylized HSI motions. We further introduce a comprehensive planning dataset produced by RAG and a stylized motion dataset featuring diverse locomotions and interactions. Extensive experiments demonstrate SIMS's effectiveness in executing various tasks and generalizing across different scenarios, significantly outperforming previous methods.
</p>

<h2 class="project-section-title">Video</h2>

<div class="project-media-grid">
  <div class="project-media-card project-media-card--video">
    <iframe src="https://www.youtube.com/embed/qfQ8TSjpJ7I" title="SIMS video" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
</div>

<h2 class="project-section-title">Demo Gallery</h2>

<div class="project-media-grid project-media-grid--three">
  <div class="project-media-card">
    <h3 class="project-card-title">Demo 1</h3>
    <video controls preload="metadata" playsinline poster="/projects/sims/covers/demo1.png">
      <source src="/projects/sims/demos/demo1.mp4" type="video/mp4">
    </video>
    <div class="project-video-fallback"><a href="/projects/sims/demos/demo1.mp4">Open video</a></div>
  </div>
  <div class="project-media-card">
    <h3 class="project-card-title">Demo 2</h3>
    <video controls preload="metadata" playsinline poster="/projects/sims/covers/demo2.png">
      <source src="/projects/sims/demos/demo2.mp4" type="video/mp4">
    </video>
    <div class="project-video-fallback"><a href="/projects/sims/demos/demo2.mp4">Open video</a></div>
  </div>
  <div class="project-media-card">
    <h3 class="project-card-title">Demo 3</h3>
    <video controls preload="metadata" playsinline poster="/projects/sims/covers/demo3.png">
      <source src="/projects/sims/demos/demo3.mp4" type="video/mp4">
    </video>
    <div class="project-video-fallback"><a href="/projects/sims/demos/demo3.mp4">Open video</a></div>
  </div>
  <div class="project-media-card">
    <h3 class="project-card-title">Demo 4</h3>
    <video controls preload="metadata" playsinline poster="/projects/sims/covers/demo4.png">
      <source src="/projects/sims/demos/demo4.mp4" type="video/mp4">
    </video>
    <div class="project-video-fallback"><a href="/projects/sims/demos/demo4.mp4">Open video</a></div>
  </div>
  <div class="project-media-card">
    <h3 class="project-card-title">Demo 5</h3>
    <video controls preload="metadata" playsinline poster="/projects/sims/covers/demo5.png">
      <source src="/projects/sims/demos/demo5.mp4" type="video/mp4">
    </video>
    <div class="project-video-fallback"><a href="/projects/sims/demos/demo5.mp4">Open video</a></div>
  </div>
  <div class="project-media-card">
    <h3 class="project-card-title">Demo 6</h3>
    <video controls preload="metadata" playsinline poster="/projects/sims/covers/demo6.png">
      <source src="/projects/sims/demos/demo6.mp4" type="video/mp4">
    </video>
    <div class="project-video-fallback"><a href="/projects/sims/demos/demo6.mp4">Open video</a></div>
  </div>
  <div class="project-media-card">
    <h3 class="project-card-title">Demo 7</h3>
    <video controls preload="metadata" playsinline poster="/projects/sims/covers/demo7.png">
      <source src="/projects/sims/demos/demo7.mp4" type="video/mp4">
    </video>
    <div class="project-video-fallback"><a href="/projects/sims/demos/demo7.mp4">Open video</a></div>
  </div>
</div>

<h2 class="project-section-title">Skills</h2>

<div class="project-skill-grid">
  <div>
    <video controls muted loop playsinline preload="metadata" poster="/projects/sims/skill_posters/carry.jpg">
      <source src="/projects/sims/skills/carry.mp4" type="video/mp4">
    </video>
    <div class="project-caption">Carry</div>
  </div>
  <div>
    <video controls muted loop playsinline preload="metadata" poster="/projects/sims/skill_posters/idle.jpg">
      <source src="/projects/sims/skills/idle.mp4" type="video/mp4">
    </video>
    <div class="project-caption">Idle</div>
  </div>
  <div>
    <video controls muted loop playsinline preload="metadata" poster="/projects/sims/skill_posters/walk.jpg">
      <source src="/projects/sims/skills/walk.mp4" type="video/mp4">
    </video>
    <div class="project-caption">Walk</div>
  </div>
  <div>
    <video controls muted loop playsinline preload="metadata" poster="/projects/sims/skill_posters/sit.jpg">
      <source src="/projects/sims/skills/sit.mp4" type="video/mp4">
    </video>
    <div class="project-caption">Sit</div>
  </div>
  <div>
    <video controls muted loop playsinline preload="metadata" poster="/projects/sims/skill_posters/lie.jpg">
      <source src="/projects/sims/skills/lie.mp4" type="video/mp4">
    </video>
    <div class="project-caption">Lie</div>
  </div>
</div>

<h2 class="project-section-title">Pipeline</h2>

<div class="project-hero">
  <img class="project-hero__image" src="/projects/sims/pipeline.png" alt="SIMS pipeline" />
</div>

<h2 class="project-section-title">BibTeX</h2>

<div class="project-bibtex">
<pre><code>@inproceedings{wang2025sims,
  title={SIMS: Simulating Stylized Human-Scene Interactions with Retrieval-Augmented Script Generation},
  author={Wang, Wenjia and Pan, Liang and Dou, Zhiyang and Mei, Jidong and Liao, Zhouyingcheng and Lou, Yuke and Wu, Yifan and Yang, Lei and Wang, Jingbo and Komura, Taku},
  booktitle={ICCV},
  year={2025}
}</code></pre>
</div>

</div>


<script>
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.project-preview .fluid-width-video-wrapper').forEach((wrapper) => {
      const parent = wrapper.parentNode;
      while (wrapper.firstChild) {
        parent.insertBefore(wrapper.firstChild, wrapper);
      }
      parent.removeChild(wrapper);
    });

    document.querySelectorAll('.project-preview video').forEach((video) => {
      video.style.pointerEvents = 'auto';
    });

    document.querySelectorAll('.project-preview .project-skill-grid video').forEach((video) => {
      video.muted = true;
      video.defaultMuted = true;
      video.loop = true;
      video.autoplay = true;
      video.playsInline = true;
      const tryPlay = () => {
        const playPromise = video.play();
        if (playPromise && typeof playPromise.catch === 'function') {
          playPromise.catch(() => {
            video.setAttribute('controls', 'controls');
            video.removeAttribute('autoplay');
          });
        }
      };
      if (video.readyState >= 2) {
        tryPlay();
      } else {
        video.addEventListener('loadeddata', tryPlay, { once: true });
      }
    });
  });
</script>

