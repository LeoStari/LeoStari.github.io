---
layout: default
title: Home
---

<section id="about">
  <h2>About Me</h2>
  <div class="about-container">
    <div class="profile-pic-container">
      <img src="/assets/images/profile.JPG" alt="Leonardo Stari" class="profile-pic">
    </div>
    <div class="bio-container">
      <p>
        <strong>Hi, I am Leonardo Stari.</strong> I am currently an Assistant Professor (Research) at Tohoku University, contributing to the "Digital Biosphere" project funded by MEXT. My research bridges the gap between experimental microbiology and computational modeling, with a focus on bioremediation and microbial community dynamics.
      </p>
      <p>
        Originally from Santiago, Chile, I moved to Sendai, Japan, in 2016. I hold a PhD in Environmental Chemistry and possess a diverse professional background that spans from IT project engineering to wet-lab research.
      </p>
      
      <div class="profile-links">
        <a href="https://orcid.org/0000-0002-8194-4630" target="_blank" rel="noopener">ORCID</a>
        <a href="https://www.researchgate.net/profile/Leonardo-Stari" target="_blank" rel="noopener">ResearchGate</a>
        <a href="https://www.linkedin.com/in/lstari" target="_blank" rel="noopener">LinkedIn</a>
        <a href="/assets/files/CV_LeonardoStari.pdf">Download CV</a>
      </div>
    </div>
  </div>
</section>

<section id="skills">
  <h2>Skills & Languages</h2>
  <div class="skills-container">
    <div class="skills-col">
      <strong>Languages</strong>
      <ul>
        <li>English (Native/Advanced)</li>
        <li>Spanish (Native)</li>
        <li>Japanese (Advanced)</li>
        <li>French (Intermediate)</li>
      </ul>
    </div>
    <div class="skills-col">
      <strong>Technical</strong>
      <ul>
        <li>Java, Python (LSTM/Deep Learning), Matlab</li>
        <li>Genomic Analysis & Bioinformatics</li>
        <li>Experimental Design & Bioreactors</li>
      </ul>
    </div>
  </div>
</section>

<section id="research">
  <h2>Research Interests</h2>
  <p>
    My work combines wet-lab experimentation with data-driven modeling to solve environmental challenges.
  </p>
  
  <h3>Bioremediation & Genomics</h3>
  <p>
    I focus on the biodegradation of persistent organic pollutants. A key achievement was the isolation of <em>Pseudomonas sp. Stari2</em>, a novel strain capable of degrading Carbon Tetrachloride (CT) under <strong>aerobic conditions</strong>. I utilized joint Illumina/Nanopore sequencing to identify specific dehalogenase enzymes.
  </p>

  <h3>Microbial Ecology & Deep Learning</h3>
  <p>
    I apply deep learning techniques—specifically <strong>LSTM</strong> and <strong>BiLSTM</strong> neural networks—to predict community succession. Using high-resolution time-series data, my models have achieved over 90% accuracy in forecasting OTU profiles, revealing how the "Rare Biosphere" follows distinct successional trajectories.
  </p>
</section>

<section id="metrics">
  <h2>Research Metrics</h2>
  <!-- This reads directly from _data/metrics.json -->
  <div class="metrics-card">
    <div class="metric-box">
      <span class="metric-label">Citations</span>
      <span class="metric-value">{{ site.data.metrics.citations | default: "—" }}</span>
    </div>
    <div class="metric-box">
      <span class="metric-label">h-index</span>
      <span class="metric-value">{{ site.data.metrics.hindex | default: "—" }}</span>
    </div>
    <div class="metric-box">
      <span class="metric-label">Publications</span>
      <span class="metric-value">{{ site.data.metrics.pubs | default: "—" }}</span>
    </div>
  </div>
  <p class="metrics-note">Metrics updated manually from Scopus/Google Scholar.</p>
</section>

<section id="publications">
  <h2>Publications</h2>
  <ul id="publications-list">
    <!-- Loading animation placeholder -->
    <li>Loading publications from ORCID...</li>
  </ul>
  <p id="publications-fallback" style="display: none;">
    Full list available on <a href="https://orcid.org/0000-0002-8194-4630" target="_blank">ORCID</a>.
  </p>
  
  <!-- This script fetches live data from ORCID -->
  <script>
    fetch('https://pub.orcid.org/v3.0/0000-0002-8194-4630/works', {
      headers: { 'Accept': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
      const list = document.getElementById('publications-list');
      list.innerHTML = ''; // Clear placeholder
      if (data.group && data.group.length > 0) {
        data.group.forEach(group => {
          const work = group['work-summary'][0];
          const title = work.title.title.value;
          const year = work['publication-date'] ? work['publication-date'].year.value : '';
          
          // Try to find DOI
          let doi = null;
          if (work['external-ids'] && work['external-ids']['external-id']) {
             const doiObj = work['external-ids']['external-id'].find(id => id['external-id-type'] === 'doi');
             if(doiObj) doi = doiObj['external-id-value'];
          }

          const li = document.createElement('li');
          li.innerHTML = `<strong>${title}</strong> (${year}) ${doi ? `<a href="https://doi.org/${doi}" target="_blank" style="font-size:0.8em; margin-left:5px;">[DOI]</a>` : ''}`;
          list.appendChild(li);
        });
      } else {
        document.getElementById('publications-fallback').style.display = 'block';
      }
    })
    .catch(error => {
      console.error('Error fetching publications:', error);
      document.getElementById('publications-list').style.display = 'none';
      document.getElementById('publications-fallback').style.display = 'block';
    });
  </script>
</section>

<section id="contact">
  <h2>Contact</h2>
  <p>
    You can reach me at: <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a><br>
    Alternatively: <a href="mailto:leonardostari@gmail.com">leonardostari@gmail.com</a>
  </p>
</section>