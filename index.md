---
layout: default
title: Home
---

<!-- About Section -->
<section id="about" class="fade-in">
  <h2>About Me</h2>
  <div class="about-card">
    <div class="about-image">
      <img src="{{ '/assets/images/profile.jpg' | relative_url }}" alt="Leonardo Stari">
    </div>
    <div class="about-text">
      <h3>Hi, I am Leonardo (Leo) Stari</h3>
      <p>
        I am currently an <strong>Assistant Professor (Research)</strong> at 
        <a href="https://www.tohoku.ac.jp/" target="_blank" rel="noopener">Tohoku University</a>, 
        contributing to the <em>"Digital Biosphere"</em> project funded by MEXT. My research bridges 
        the gap between experimental microbiology and computational modeling, with a focus on 
        <strong>bioremediation</strong> and <strong>microbial community dynamics</strong>.
      </p>
      <p>
        Originally from Santiago, Chile, I moved to Sendai, Japan, in 2016. I hold a PhD in 
        Environmental Chemistry and possess a diverse professional background that spans from 
        IT project engineering to wet-lab research.
      </p>
      <p>
        Outside of the lab, I enjoy walking, swimming, and reading novels and manga. 
        I am also an avid gamer, enjoying titles like <em>World of Warcraft</em> and 
        <em>Pokémon</em>.
      </p>

      <h3 style="margin-top: var(--space-lg);">Career Timeline</h3>
      <div class="timeline">
        <div class="timeline-item">
          <div class="timeline-date">April 2022 – Present</div>
          <div class="timeline-title">Assistant Professor (Research)</div>
          <div class="timeline-desc">Tohoku University, Digital Biosphere Project</div>
        </div>
        <div class="timeline-item">
          <div class="timeline-date">2018 – 2022</div>
          <div class="timeline-title">PhD in Environmental Chemistry</div>
          <div class="timeline-desc">Tohoku University (MEXT Scholar)</div>
        </div>
        <div class="timeline-item">
          <div class="timeline-date">2016 – 2018</div>
          <div class="timeline-title">Master of Science in Environmental Science</div>
          <div class="timeline-desc">Tohoku University</div>
        </div>
        <div class="timeline-item">
          <div class="timeline-date">2013 – 2016</div>
          <div class="timeline-title">IT Project Engineer</div>
          <div class="timeline-desc">Novakem, Santiago, Chile</div>
        </div>
        <div class="timeline-item">
          <div class="timeline-date">2004 – 2010</div>
          <div class="timeline-title">Professional Degree in Biotechnology</div>
          <div class="timeline-desc">University of Chile</div>
        </div>
      </div>

      <div style="margin-top: var(--space-lg); display: flex; gap: var(--space-xs); flex-wrap: wrap;">
        <a href="https://orcid.org/0000-0002-8194-4630" target="_blank" rel="noopener" style="padding: 8px 16px; background: var(--accent); color: white; border-radius: var(--radius-sm); font-size: 0.9rem;">ORCID</a>
        <a href="https://www.researchgate.net/profile/Leonardo-Stari" target="_blank" rel="noopener" style="padding: 8px 16px; background: var(--text-muted); color: white; border-radius: var(--radius-sm); font-size: 0.9rem;">ResearchGate</a>
        <a href="https://www.linkedin.com/in/lstari" target="_blank" rel="noopener" style="padding: 8px 16px; background: #0077b5; color: white; border-radius: var(--radius-sm); font-size: 0.9rem;">LinkedIn</a>
      </div>
    </div>
  </div>
</section>

<!-- Skills Section -->
<section id="skills" class="fade-in">
  <h2>Skills & Languages</h2>
  <div class="skills-grid">
    <div class="skill-card">
      <h3>🌐 Languages</h3>
      <ul class="skill-list">
        <li>🇪🇸 Spanish (Native)</li>
        <li>🇬🇧 English (Advanced)</li>
        <li>🇯🇵 Japanese (Advanced)</li>
        <li>🇫🇷 French (Intermediate)</li>
      </ul>
    </div>
    <div class="skill-card">
      <h3>💻 Technical Skills</h3>
      <ul class="skill-list">
        <li>Python (Deep Learning / LSTM)</li>
        <li>Genomic Analysis & Bioinformatics</li>
        <li>Java, Matlab</li>
        <li>Experimental Design & Bioreactors</li>
        <li>Illumina & Nanopore Sequencing</li>
      </ul>
    </div>
  </div>
</section>

<!-- Research Section -->
<section id="research" class="fade-in">
  <h2>Research Interests</h2>
  <p style="font-size: 1.05rem; color: var(--text-secondary); margin-bottom: var(--space-lg);">
    My academic path is driven by a goal to elucidate and harness microbial processes for environmental benefit. 
    My work combines wet-lab experimentation with data-driven modeling.
  </p>

  <div class="research-section">
    <h3>
      <svg class="research-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 3H5a2 2 0 0 0-2 2v4m6-6h10a2 2 0 0 1 2 2v4M9 3v18m0 0h10a2 2 0 0 0 2-2V9M9 21H5a2 2 0 0 1-2-2V9m0 0h18"/></svg>
      Bioremediation & Genomics
    </h3>
    <p>
      I focus on the biodegradation of persistent organic pollutants. A key achievement of my doctoral work 
      was the isolation of <em><strong>Pseudomonas sp. Stari2</strong></em>, a novel strain capable of 
      degrading Carbon Tetrachloride (CT) under <span class="stat-highlight">aerobic conditions</span>.
    </p>
    <div class="highlight-text">
      I successfully enriched a consortium capable of degrading 30 μM CT within one week and demonstrated 
      that <em>Stari2</em> tolerates CT concentrations up to 5 mM. Utilizing joint Illumina/Nanopore sequencing, 
      I identified specific dehalogenase enzymes and metabolic pathways essential for these strategies.
    </div>
  </div>

  <div class="research-section">
    <h3>
      <svg class="research-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8z"/><path d="M12 6v6l4 2"/></svg>
      Microbial Ecology & Deep Learning
    </h3>
    <p>
      To bridge the gap between isolate characterization and ecosystem function, I study how microbial 
      populations assemble. In the "Digital Biosphere" project, I apply deep learning techniques—specifically 
      <span class="stat-highlight">LSTM (Long Short-Term Memory)</span> networks—to predict community succession.
    </p>
    <div class="highlight-text">
      Using high-resolution time-series data (<strong>522 samples</strong>), our models have achieved over 
      <span class="stat-highlight">90% accuracy</span> in forecasting OTU profiles. We discovered that carbon 
      sources act as deterministic filters and that the "Rare Biosphere" follows distinct successional trajectories 
      compared to abundant taxa.
    </div>
  </div>
</section>

<!-- Metrics Section - Using Jekyll Liquid template to read from _data/metrics.json -->
<section id="metrics" class="fade-in">
  <h2>Research Metrics</h2>
  <div class="metrics-grid">
    <div class="metric-card">
      <div class="metric-label">Citations</div>
      <div class="metric-value">{{ site.data.metrics.citations | default: "—" }}</div>
    </div>
    <div class="metric-card">
      <div class="metric-label">h-index</div>
      <div class="metric-value">{{ site.data.metrics.hindex | default: "—" }}</div>
    </div>
    <div class="metric-card">
      <div class="metric-label">Publications</div>
      <div class="metric-value">{{ site.data.metrics.pubs | default: "—" }}</div>
    </div>
  </div>
  <p class="metrics-note">Metrics based on Scopus / Google Scholar data. Updated via Python script.</p>
</section>

<!-- Publications Section -->
<section id="publications" class="fade-in">
  <h2>Publications</h2>
  <ul class="publications-list" id="publications-list">
    <li>Loading publications from ORCID... <span class="loading"></span></li>
  </ul>
  <p id="publications-fallback" style="display: none; text-align: center; color: var(--text-muted); margin-top: var(--space-md);">
    Full list available on <a href="https://orcid.org/0000-0002-8194-4630" target="_blank" rel="noopener">ORCID</a>.
  </p>
  
  <script>
    fetch('https://pub.orcid.org/v3.0/0000-0002-8194-4630/works', {
      headers: { 'Accept': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
      const list = document.getElementById('publications-list');
      list.innerHTML = ''; 
      let count = 1;
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
          li.innerHTML = `
            <span class="pub-number">${count}</span>
            <div class="pub-title">${title}</div>
            <div class="pub-year">
              ${year} 
              ${doi ? `<span class="pub-doi"><a href="https://doi.org/${doi}" target="_blank" rel="noopener">DOI</a></span>` : ''}
            </div>
          `;
          list.appendChild(li);
          count++;
        });
      } else {
        document.getElementById('publications-fallback').style.display = 'block';
      }
    })
    .catch(error => {
      console.error('Error fetching publications:', error);
      document.getElementById('publications-list').innerHTML = '<li>Unable to load publications. View them directly on <a href="https://orcid.org/0000-0002-8194-4630" target="_blank">ORCID</a>.</li>';
    });
  </script>
</section>

<!-- Contact Section -->
<section id="contact" class="fade-in">
  <h2>Contact</h2>
  <div class="contact-card">
    <p style="color: rgba(255,255,255,0.9); margin-bottom: var(--space-sm);">
      Feel free to reach out for collaborations or inquiries!
    </p>
    <a href="mailto:{{ site.author.email }}" class="contact-email">{{ site.author.email }}</a>
    <br><br>
    <a href="mailto:leonardostari@gmail.com" style="color: rgba(255,255,255,0.7); font-size: 0.9rem; text-decoration: underline;">Alternative Email</a>
  </div>
</section>
