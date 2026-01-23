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
          <strong>Hi, I am Leonardo Stari.</strong> I am currently an Assistant Professor (Research) at Tohoku University, contributing to the "Digital Biosphere" project funded by MEXT. My research bridges the gap between experimental microbiology and computational modeling, with a focus on bioremediation, microbial community dynamics, and data-driven ecosystem analysis.
        </p>
        <p>
          Originally from Santiago, Chile, I moved to Sendai, Japan, in 2016. My academic journey began with a focus on biotechnology and renewable energy (bioethanol), evolving into environmental chemistry and microbial ecology. I hold a PhD in Environmental Chemistry and possess a diverse professional background that spans from IT project engineering to wet-lab research.
        </p>
        <p>
          My goal is to elucidate and harness microbial processes for environmental benefit—from optimizing single-strain biodegradation to predicting complex community succession using deep learning.
        </p>
        <p>
          Outside of the lab, I enjoy walking, swimming, and immersing myself in novels and manga. I am also an avid gamer, enjoying titles like <em>World of Warcraft</em> and <em>Pokémon</em>.
        </p>

        <h3>Career Timeline</h3>
        <ul>
          <li><strong>April 2022–Present</strong>: Assistant Professor (Research), Tohoku University (Digital Biosphere Project)</li>
          <li><strong>2018–2022</strong>: PhD in Environmental Chemistry, Tohoku University (MEXT Scholar)</li>
          <li><strong>2016–2018</strong>: Master of Science in Environmental Science, Tohoku University</li>
          <li><strong>2013–2016</strong>: IT Project Engineer, Novakem (Santiago, Chile)</li>
          <li><strong>2011</strong>: Researcher, La Pintana Municipality Environmental Dept.</li>
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
    <div class="skills-container" style="display: flex; gap: 2rem; flex-wrap: wrap;">
      <div>
        <strong>Languages:</strong>
        <ul>
          <li>English (Native/Advanced)</li>
          <li>Spanish (Native)</li>
          <li>Japanese (Advanced)</li>
          <li>French (Intermediate)</li>
        </ul>
      </div>
      <div>
        <strong>Technical:</strong>
        <ul>
          <li>Java, Python (Deep Learning/LSTM), Matlab</li>
          <li>Genomic Analysis & Bioinformatics</li>
          <li>Experimental Design & Bioreactors</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="research">
    <h2>Research Interests</h2>
    <p>
      My work combines wet-lab experimentation with data-driven modeling to solve environmental challenges. Recently, I have focused on the mechanisms of community assembly—specifically trait selection, metabolic filtering, and stress response.
    </p>
    
    <h3>Bioremediation & Genomics</h3>
    <p>
      I focus on the biodegradation of persistent organic pollutants. A key achievement of my doctoral work was the isolation of <em>Pseudomonas sp. Stari2</em>, a novel strain capable of degrading Carbon Tetrachloride (CT) under <strong>aerobic conditions</strong>. 
    </p>
    <p>
      I successfully established a stable consortium able to degrade 30 μM CT within one week and demonstrated that <em>Stari2</em> can tolerate CT concentrations up to 5 mM. Utilizing joint Illumina/Nanopore sequencing, I identified specific dehalogenase enzymes and metabolic pathways essential for these bioremediation strategies.
    </p>

    <h3>Microbial Ecology & Deep Learning</h3>
    <p>
      I am deeply interested in how microbial populations assemble and evolve. In the "Digital Biosphere" project, I apply deep learning techniques—specifically <strong>LSTM (Long Short-Term Memory)</strong> and <strong>BiLSTM</strong> neural networks—to predict community succession.
    </p>
    <p>
      Using high-resolution time-series data (over 500 samples), my models have achieved over <strong>90% accuracy</strong> in forecasting OTU profiles. My research has revealed that carbon sources act as deterministic filters and that the "Rare Biosphere" (<0.1% abundance) follows distinct, hyper-sensitive successional trajectories compared to abundant taxa.
    </p>

    <h3>Biotechnological Foundations</h3>
    <p>
      My background also includes optimizing renewable energy production. During my earlier studies, I worked on enhancing bioethanol yields from lignocellulosic biomass, optimizing ionic liquid pretreatments to achieve ethanol yields of 313 L per metric ton—approaching theoretical maximums.
    </p>
  </section>

  <section id="metrics">
    <h2>Research metrics</h2>
    <div class="metrics-card">
      <div><strong>Citations</strong><div class="metric-value" id="metric-citations">—</div></div>
      <div><strong>h-index</strong><div class="metric-value" id="metric-hindex">—</div></div>
      <div><strong>Publications</strong><div class="metric-value" id="metric-pubs">—</div></div>
    </div>
    <p class="metrics-note">Metrics are loaded from <code>/assets/data/metrics.json</code>.</p>
  </section>

  <section id="publications">
    <h2>Publications</h2>
    <p>Below is a list of my works fetched from ORCID. A full list including conference presentations is available on my CV.</p>
    <ul id="publications-list"></ul>
    <p id="publications-fallback" style="display: none;">Full list available on <a href="https://orcid.org/0000-0002-8194-4630" target="_blank">ORCID</a>.</p>
    <script>
      fetch('https://pub.orcid.org/v3.0/0000-0002-8194-4630/works', {
        headers: { 'Accept': 'application/json' }
      })
      .then(response => response.json())
      .then(data => {
        const list = document.getElementById('publications-list');
        if (data.group && data.group.length > 0) {
          data.group.forEach(group => {
            const work = group['work-summary'][0];
            const title = work.title.title.value;
            const year = work['publication-date'] ? work['publication-date'].year.value : 'N/A';
            const doi = work['external-ids'] && work['external-ids']['external-id'].find(id => id['external-id-type'] === 'doi') ? work['external-ids']['external-id'].find(id => id['external-id-type'] === 'doi')['external-id-value'] : null;
            const li = document.createElement('li');
            li.innerHTML = `<strong>${title}</strong> (${year})${doi ? ` <a href="https://doi.org/${doi}" target="_blank">[DOI]</a>` : ''}`;
            list.appendChild(li);
          });
        } else {
          document.getElementById('publications-fallback').style.display = 'block';
        }
      })
      .catch(error => {
        console.error('Error fetching publications:', error);
        document.getElementById('publications-fallback').style.display = 'block';
      });
    </script>
  </section>
  
  <section id="contact">
    <h2>Contact</h2>
    <p>
      You can reach me at: <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a><br>
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