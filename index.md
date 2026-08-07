---
layout: default
title: Home
---

<!-- About Section -->
<section id="about" class="fade-in">
  <h2>About Me</h2>
  <div class="about-card">
    <div class="about-image">
      <img src="{{ '/assets/images/profile.JPG' | absolute_url }}" alt="Leonardo Stari" onerror="this.parentElement.style.background='var(--accent)'; this.style.display='none';">
    </div>
    <div class="about-text">
      <h3>Hi, I am Leonardo (Leo) Stari</h3>
      <p>
        I am currently a <strong>Specially Appointed Research Fellow</strong> at 
        <a href="https://www.tohoku.ac.jp/" target="_blank" rel="noopener">Tohoku University</a>, 
        conducting research in the <strong>Mei Lab</strong> (Graduate School of Environmental Studies). 
        My work bridges experimental microbiology and computational modeling, focusing on the 
        <strong>bioremediation of water and air pollutants</strong>, as well as <strong>predictive microbial ecology</strong>. 
        By combining wet-lab isolation of novel degraders with next-generation AI architectures, I aim to transform 
        how we understand and utilize microbial communities for environmental restoration.
      </p>
      <p>
        Originally from Santiago, Chile, I moved to Sendai, Japan, in 2016. I hold a PhD in 
        Environmental Chemistry and possess a diverse professional background that spans from 
        IT project engineering to high-performance computing and wet-lab research.
      </p>
      <p>
        Outside of the lab, I enjoy walking, swimming, and reading novels and manga. 
        I am also an avid gamer, enjoying titles like <em>World of Warcraft</em> and 
        <em>Pokémon</em>.
      </p>

      <h3 style="margin-top: var(--space-lg);">Career Timeline</h3>
      <div class="timeline">
        <div class="timeline-item">
          <div class="timeline-date">2026 – Present</div>
          <div class="timeline-title">Specially Appointed Research Fellow (特任研究員)</div>
          <div class="timeline-desc">Tohoku University, Mei Lab (環境科学研究科) · <a href="https://web.tohoku.ac.jp/eco-remediation/" target="_blank" rel="noopener" style="color: var(--accent); text-decoration: underline;">Visit Lab Website →</a></div>
        </div>
        <div class="timeline-item">
          <div class="timeline-date">April 2022 – March 2026</div>
          <div class="timeline-title">Assistant Professor (Research)</div>
          <div class="timeline-desc">Tohoku University, Digital Biosphere Project</div>
        </div>
        <div class="timeline-item">
          <div class="timeline-date">2018 – Mar 2022</div>
          <div class="timeline-title">Ph.D., Environmental Studies</div>
          <div class="timeline-desc">Tohoku University</div>
        </div>
        <div class="timeline-item">
          <div class="timeline-date">2016 – 2018</div>
          <div class="timeline-title">Master's degree, Environmental Engineering Technology / Environmental Technology</div>
          <div class="timeline-desc">Tohoku University<br><em>Bioremediation of chlorinated methanes</em></div>
        </div>
        <div class="timeline-item">
          <div class="timeline-date">2013 – 2016</div>
          <div class="timeline-title">IT Project Engineer</div>
          <div class="timeline-desc">Novakem, Santiago, Chile</div>
        </div>
        <div class="timeline-item">
          <div class="timeline-date">2006 – 2012</div>
          <div class="timeline-title">Engineer's degree, Biotechnology</div>
          <div class="timeline-desc">Universidad de Chile<br><small>Seishin, Renewable Energies Lab. (2006-2009) | Intro. Japanese course & assistant teacher (2007-2009) | Summer school teacher | Thesis in biofuels</small></div>
        </div>
        <div class="timeline-item">
          <div class="timeline-date">2004 – 2005</div>
          <div class="timeline-title">Bachelor, Science</div>
          <div class="timeline-desc">Universidad de Chile<br><small>Bachelor degree, thesis in bioethics</small></div>
        </div>
      </div>

      <div style="margin-top: var(--space-lg); display: flex; gap: var(--space-xs); flex-wrap: wrap;">
        <a href="https://orcid.org/0000-0002-8194-4630" target="_blank" rel="noopener" style="padding: 8px 16px; background: #A6CE39; color: white; border-radius: var(--radius-sm); font-size: 0.9rem;">ORCID</a>
        <a href="https://www.researchgate.net/profile/Leonardo-Stari" target="_blank" rel="noopener" style="padding: 8px 16px; background: #00CCBB; color: white; border-radius: var(--radius-sm); font-size: 0.9rem;">ResearchGate</a>
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
      <h3>🧪 Wet Lab Techniques</h3>
      <ul class="skill-list">
        <li>Microbial Isolation & Enrichment Cultures</li>
        <li>Bioreactor Design & Scale-up</li>
        <li>ICP-MS Quantitative Analysis</li>
        <li>Plant Physiology & Field Work</li>
      </ul>
    </div>
    <div class="skill-card">
      <h3>💻 Dry Lab & Computational Techniques</h3>
      <ul class="skill-list">
        <li>Deep Learning & AI (LSTM, JEPA, xLSTM)</li>
        <li>Metagenomics & Bioinformatics Pipelines (HPC)</li>
        <li>Illumina & Nanopore Sequencing Analysis</li>
        <li>Python, MATLAB & Java Scripting</li>
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
      <svg class="research-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
      Bioremediation of Water & Air Pollutants
    </h3>
    <p>
      I focus on harnessing microbial processes to degrade persistent organic pollutants and heavy metals from 
      contaminated water and air. My work spans the isolation of novel degraders, functional genomics, and 
      bioreactor-scale bioaugmentation strategies. Key examples include the isolation of <em>Pseudomonas</em> sp. 
      Stari2 for aerobic carbon tetrachloride degradation, and current efforts targeting selenate-reducing 
      consortia for mine wastewater treatment.
    </p>
    <div class="highlight-text">
      See: <em>Stari et al. (PhD Thesis, 2022)</em> on CT-degrading consortia, and ongoing selenium bioremediation projects at Mei Lab.
    </div>
  </div>

  <div class="research-section">
    <h3>
      <svg class="research-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8z"/><path d="M12 6v6l4 2"/></svg>
      Microbial Ecology & Predictive AI
    </h3>
    <p>
      To bridge the gap between isolate characterization and ecosystem function, I study how microbial 
      communities assemble and respond to environmental shifts. Leveraging functional shotgun metagenomics 
      and high-resolution time-series data, I apply next-generation AI architectures (LSTM, JEPA, xLSTM) 
      to transform microbial ecology into a predictive science.
    </p>
    <div class="highlight-text">
      See: <em>Stari et al. (2026), ISME Communications</em> — "Carbon Source Acts as a Deterministic Filter Shaping Microbial Succession..."
    </div>
  </div>
</section>

<!-- Latest Publication Highlight -->
<section id="latest-publication" class="fade-in">
  <h2>Latest Publication</h2>
  <div class="research-section" style="border-left: 4px solid var(--accent);">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: var(--space-sm);">
      <div>
        <span style="background: #38a169; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600;">📢 NEW</span>
        <h3 style="margin-top: var(--space-sm);">Carbon Source Acts as a Deterministic Filter Shaping Microbial Succession and Rare-Abundant Decoupling in Soil Bacterial Communities</h3>
      </div>
      <a href="https://doi.org/10.1093/ismeco/ycag108" target="_blank" rel="noopener" style="background: var(--accent); color: white; padding: 8px 16px; border-radius: var(--radius-sm); font-size: 0.9rem; text-decoration: none;">View Paper →</a>
    </div>
    <p style="margin-top: var(--space-sm);">
      <em>ISME Communications</em> | Published: April 20, 2026 | DOI: <a href="https://doi.org/10.1093/ismeco/ycag108" target="_blank" rel="noopener">10.1093/ismeco/ycag108</a>
    </p>
    <div class="highlight-text">
      We investigated how chemically diverse carbon sources act as ecological filters shaping soil bacterial communities. Null model analysis confirmed the carbon source as the primary deterministic filter, enforcing high reproducibility (homogeneous selection governing ~74% of assembly among replicates) and overriding stochastic effects. Crucially, abundant (>1%) and rare (<0.1%) taxa exhibited decoupled assembly mechanisms — while abundant taxa were driven by dispersal limitation (~59%) and variable selection, the rare biosphere displayed a temporal regime shift, transitioning from stochastic isolation to strong deterministic selection (~50%) during later successional stages. This reframes the rare biosphere as a "latent responder" reservoir recruited by metabolic byproducts rather than the primary substrate.
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

<!-- Current Projects Section -->
<section id="projects" class="fade-in">
  <h2>Current Projects</h2>

  <div class="research-section" style="border-left: 4px solid var(--accent);">
    <h3>🧪 Biological Selenium Removal from Mine Wastewater</h3>
    <p>
      Targeting the underexplored selenate (Se⁶⁺) reduction pathway, this project isolates and characterizes 
      selenate-reducing bacterial consortia from selenium-affected mine wastewater. The approach combines 
      strain isolation with bioaugmentation strategies, aiming to achieve selenium concentrations below 
      10 ppb in treated effluent through lab-scale and pilot reactor testing.
    </p>
  </div>

  <div class="research-section" style="border-left: 4px solid #38a169;">
    <h3>🤖 AI-Driven Prediction of Bacterial Communities</h3>
    <p>
      Leveraging functional shotgun metagenomic data and high-resolution time-series sequencing, this project 
      applies next-generation AI architectures (LSTM, JEPA, xLSTM) to predict microbial community dynamics 
      and succession patterns. The goal is to transform microbial ecology from an observation-heavy field 
      into a highly predictive science.
    </p>
  </div>

  <div class="research-section" style="border-left: 4px solid #805ad5;">
    <h3>💨 Bioremediation of Contaminated Air</h3>
    <p>
      Investigating microbial degradation of volatile organic compounds (VOCs) and persistent gaseous pollutants. 
      Building on previous work with carbon tetrachloride, this project explores biofilter and bioreactor 
      systems for treating industrial and environmental air emissions.
    </p>
  </div>
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

<!-- Selected Talks & Presentations Section -->
<section id="talks" class="fade-in">
  <h2>Selected Talks & Presentations</h2>

  <div class="talks-category">
    <h3>🎤 Conference Oral Presentations</h3>
    <ul class="talks-list">
      <li>
        <div class="talk-title">Deep Neural Networks for Predicting OTU Dynamics in Soil Bacterial Communities</div>
        <div class="talk-meta">
          <span class="talk-authors">Stari, L.; Kishida, K.; Ohtsubo, Y.; Nagata, Y.</span> ·
          <span class="talk-venue">JSBBA 2025 日本農芸化学会</span> ·
          <span class="talk-location">📍 Sapporo, Japan</span> ·
          <span class="talk-date">Mar 2025</span>
        </div>
      </li>
      <li>
        <div class="talk-title">Deterministic Shaping of Soil Bacterial Communities: Interplay of Rare Species and Environmental Selection</div>
        <div class="talk-meta">
          <span class="talk-authors">Stari, L.; Kato, H.; Ohtsubo, Y.; Nagata, Y.</span> ·
          <span class="talk-venue">JSBBA 2024 日本農芸化学会</span> ·
          <span class="talk-location">📍 Tokyo, Japan</span> ·
          <span class="talk-date">Mar 2024</span>
        </div>
      </li>
      <li>
        <div class="talk-title">The Succession of Taxonomic Structure and Metagenome Composition of Bacterial Community Cultured with Different Carbon Sources</div>
        <div class="talk-meta">
          <span class="talk-authors">Stari, L.; Kato, H.; Ohtsubo, Y.; Nagata, Y.</span> ·
          <span class="talk-venue">日本農芸化学会 2023</span> ·
          <span class="talk-location">📍 Hiroshima, Japan</span> ·
          <span class="talk-date">Mar 2023</span>
        </div>
      </li>
      <li>
        <div class="talk-title">Assessment of a Carbon Tetrachloride Degrading Consortia under Anaerobic Conditions</div>
        <div class="talk-meta">
          <span class="talk-authors">Stari, L.; Inoue, C.; Chien, M.</span> ·
          <span class="talk-venue">第13回 細菌学若手コロッセウム in みやぎ蔵王</span> ·
          <span class="talk-location">📍 Miyagi, Japan</span> ·
          <span class="talk-date">Aug 2019</span>
        </div>
      </li>
    </ul>
  </div>

  <div class="talks-category">
    <h3>🖼️ Conference Poster Presentations</h3>
    <ul class="talks-list">
      <li>
        <div class="talk-title">Assessment of Carbon Tetrachloride Degrading Consortia under Anaerobic Conditions</div>
        <div class="talk-meta">
          <span class="talk-authors">Stari, L.; Inoue, C.; Chien, M.</span> ·
          <span class="talk-venue">ASM Microbe 2019</span> ·
          <span class="talk-location">📍 California, USA</span> ·
          <span class="talk-date">Jun 2019</span>
        </div>
      </li>
    </ul>
  </div>
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

  <div class="contact-map">
    <iframe
      src="https://maps.google.com/maps?q=6-6-20+Aoba,+Aoba-ku,+Sendai,+Miyagi+980-8579,+Japan&z=15&output=embed"
      width="100%"
      height="300"
      style="border:0; border-radius: var(--radius-lg);"
      allowfullscreen=""
      loading="lazy"
      referrerpolicy="no-referrer-when-downgrade">
    </iframe>
    <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: var(--space-sm); text-align: center;">
      📍 〒980-8579 宮城県仙台市青葉区荒巻字青葉6-6-20<br>
      東北大学大学院 環境科学研究科研究棟 4F (Mei Lab)
    </p>
  </div>
</section>
