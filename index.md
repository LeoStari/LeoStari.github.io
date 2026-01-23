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
        <strong>Hi, I am Leonardo (Leo) Stari.</strong> I am currently an Assistant Professor (Research) at Tohoku University, contributing to the "Digital Biosphere" project funded by MEXT. My research bridges the gap between experimental microbiology and computational modeling, with a focus on bioremediation and microbial community dynamics.
      </p>
      <p>
        Originally from Santiago, Chile, I moved to Sendai, Japan, in 2016. I hold a PhD in Environmental Chemistry and possess a diverse professional background that spans from IT project engineering to wet-lab research.
      </p>
      <p>
        Outside of the lab, I enjoy walking, swimming, and reading novels and manga. I am also an avid gamer, enjoying titles like <em>World of Warcraft</em> and <em>Pokémon</em>.
      </p>

      <h3>Career Timeline</h3>
      <ul>
        <li><strong>April 2022–Present</strong>: Assistant Professor (Research), Tohoku University (Digital Biosphere Project)</li>
        <li><strong>2018–2022</strong>: PhD in Environmental Chemistry, Tohoku University (MEXT Scholar)</li>
        <li><strong>2016–2018</strong>: Master of Science in Environmental Science, Tohoku University</li>
        <li><strong>2013–2016</strong>: IT Project Engineer, Novakem (Santiago, Chile)</li>
        <li><strong>2004–2010</strong>: Professional Degree in Biotechnology, University of Chile</li>
      </ul>

      <div class="profile-links">
        <a href="https://orcid.org/0000-0002-8194-4630" target="_blank" rel="noopener">ORCID</a>
        <a href="https://www.researchgate.net/profile/Leonardo-Stari" target="_blank" rel="noopener">ResearchGate</a>
        <a href="https://www.scopus.com/authid/detail.uri?authorId=58094418800" target="_blank" rel="noopener">Scopus</a>
        <a href="https://www.linkedin.com/in/lstari" target="_blank" rel="noopener">LinkedIn</a>
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
        <li>Java, Python (Deep Learning/LSTM), Matlab</li>
        <li>Genomic Analysis & Bioinformatics</li>
        <li>Experimental Design & Bioreactors</li>
        <li>Hardware & PC Assembly</li>
      </ul>
    </div>
  </div>
</section>

<section id="research">
  <h2>Research Interests</h2>
  <p>
    My academic path is driven by a goal to elucidate and harness microbial processes for environmental benefit. My work combines wet-lab experimentation with data-driven modeling.
  </p>
  
  <h3>Bioremediation & Genomics</h3>
  <p>
    I focus on the biodegradation of persistent organic pollutants. A key achievement of my doctoral work was the isolation of <em>Pseudomonas sp. Stari2</em>, a novel strain capable of degrading Carbon Tetrachloride (CT) under <strong>aerobic conditions</strong>.
  </p>
  <p>
    I successfully enriched a consortium capable of degrading 30 μM CT within one week and demonstrated that <em>Stari2</em> tolerates CT concentrations up to 5 mM. Utilizing joint Illumina/Nanopore sequencing, I identified specific dehalogenase enzymes and metabolic pathways essential for these strategies.
  </p>

  <h3>Microbial Ecology & Deep Learning</h3>
  <p>
    To bridge the gap between isolate characterization and ecosystem function, I study how microbial populations assemble. In the "Digital Biosphere" project, I apply deep learning techniques—specifically <strong>LSTM (Long Short-Term Memory)</strong> networks—to predict community succession.
  </p>
  <p>
    Using high-resolution time-series data (522 samples), our models have achieved over <strong>90% accuracy</strong> in forecasting OTU profiles. We discovered that carbon sources act as deterministic filters and that the "Rare Biosphere" follows distinct successional trajectories compared to abundant taxa.
  </p>
</section>

<section id="metrics">
  <h2>Research Metrics</h2>
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
  <p class="metrics-note">Metrics based on Scopus/Google Scholar data.</p>
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
  
  <script>
    fetch('https://pub.orcid.org/v3.0/0000-0002-8194-4630/works', {
      headers: { 'Accept': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
      const list = document.getElementById('publications-list');
      list.innerHTML = ''; 
      if (data.group && data.group.length > 0) {
        data.group.forEach(group => {
          const work = group['work-summary'][0];
          const title = work.title.title.value;
          const year = work['publication-date'] ? work['publication-date'].year.value : '';
          
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