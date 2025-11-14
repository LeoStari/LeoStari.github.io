---
layout: default
title: Home
---

<div class="home">

  <section id="about">
    <h2>About Me</h2>
    <div class="about-container">
      <div class="profile-pic-container">
        <!-- Place your chosen image at /assets/images/profile.JPG -->
        <img src="/assets/images/profile.JPG" alt="Leonardo Stari" class="profile-pic">
      </div>
      <div class="bio-container">
        <p>
          Leonardo (Leo) Stari is an Assistant Professor in the Graduate School of Life Sciences at Tohoku University, working in the Microbial Genetics and Evolution / Molecular & Chemical Life Sciences groups. His research combines experimental microbiology and genomics to study microbial community dynamics and the biodegradation of persistent organic pollutants, with a particular focus on carbon tetrachloride degradation by novel Pseudomonas strains.
        </p>
        <p>
          Stari completed an engineering degree at the University of Chile, worked as a project engineer, and joined Tohoku University in 2016 on a MEXT scholarship to pursue graduate studies. He lives in Sendai and enjoys video games and walking his Akita dog in his free time.
        </p>

        <div class="profile-links">
          <a href="https://orcid.org/0000-0002-8194-4630" target="_blank" rel="noopener">ORCID</a>
          <a href="https://www.researchgate.net/profile/Leonardo-Stari" target="_blank" rel="noopener">ResearchGate</a>
          <a href="https://www.scopus.com/authid/detail.uri?authorId=58094418800" target="_blank" rel="noopener">Scopus</a>
        </div>

      </div>
    </div>
  </section>

  <section id="research">
    <h2>Research</h2>
    <p>
      My work focuses on microbial community formation and function, genome-based functional inference, and biodegradation. Recent projects include characterizing microbial consortia and isolating Pseudomonas strains capable of aerobic degradation of carbon tetrachloride, and assembling and analyzing complete genomes for these strains to investigate the genetic basis of degradation pathways.
    </p>
  </section>

  <section id="metrics">
    <h2>Research metrics</h2>
    <div class="metrics-card">
      <div><strong>Citations</strong><div class="metric-value" id="metric-citations">—</div></div>
      <div><strong>h-index</strong><div class="metric-value" id="metric-hindex">—</div></div>
      <div><strong>Publications</strong><div class="metric-value" id="metric-pubs">—</div></div>
    </div>
    <p class="metrics-note">Metrics are loaded from <code>/assets/data/metrics.json</code> or from your repository's scheduled update script.</p>
  </section>

  <section id="publications">
    <h2>Selected recent publications</h2>
    <ul>
      <li>
        Stari L., Chien M.-F., Inoue C., et al. <em>A microbial consortium led by a novel Pseudomonas strain enables degradation of carbon tetrachloride under aerobic conditions.</em> <strong>Chemosphere</strong> 2023. (Research article / consortium study).  
        [article page] — ScienceDirect. :contentReference[oaicite:1]{index=1}
      </li>

      <li>
        Stari L., Jittayasotorn T., Inoue C., Chien M.-F. <em>Complete genome sequence of a carbon tetrachloride–degrading Pseudomonas sp. strain Stari2.</em> <strong>Microbiology Resource Announcements</strong> (ASM) 2025. (Genome announcement; full text available on PMC). :contentReference[oaicite:2]{index=2}
      </li>

      <li>
        Deng W., Takada Y., Nanasato Y., Kishida K., Stari L., Ohtsubo Y., et al. <em>Transgenic Arabidopsis thaliana plants expressing bacterial γ-HCH dehydrochlorinase LinA</em>. <strong>BMC Biotechnology</strong> 2024. (Co-author). :contentReference[oaicite:3]{index=3}
      </li>
    </ul>

    <p class="small">For a complete and up-to-date list see: <a href="https://orcid.org/0000-0002-8194-4630" target="_blank" rel="noopener">ORCID profile</a> or your ResearchGate / Scopus records. :contentReference[oaicite:4]{index=4}</p>
  </section>

  <section id="contact">
    <h2>Contact</h2>
    <p>
      You can reach me at: <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a>
    </p>
  </section>
</div>

<script>
(function(){
  const elC = document.getElementById('metric-citations');
  const elH = document.getElementById('metric-hindex');
  const elP = document.getElementById('metric-pubs');

  fetch('/assets/data/metrics.json', {cache: 'no-store'})
    .then(r => r.ok ? r.json() : Promise.reject('no metrics'))
    .then(j => {
      if (elC) elC.textContent = j.citations ?? '—';
      if (elH) elH.textContent = j.hindex ?? '—';
      if (elP) elP.textContent = j.pubs ?? '—';
    })
    .catch(()=>{
      const conf = {{ site.data.metrics | jsonify }};
      if (elC) elC.textContent = conf.citations || '—';
      if (elH) elH.textContent = conf.hindex || '—';
      if (elP) elP.textContent = conf.pubs || '—';
    });
})();
</script>
