---
layout: default
title: Home
---
<div class="home">
  <nav class="main-nav">
    <ul>
      <li><a href="#about">About Me</a></li>
      <li><a href="#research">Research</a></li>
      <li><a href="#metrics">Research Metrics</a></li>
      <li><a href="#publications">Publications</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </nav>

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
        <h3>Career Timeline</h3>
        <ul>
          <li><strong>August 2022–Present</strong>: Assistant Professor, Graduate School of Life Sciences, Tohoku University</li>
          <li><strong>April–July 2022</strong>: Specially Appointed Research Fellow, Tohoku University</li>
          <li><strong>2018–2022</strong>: PhD in Environmental Studies, Tohoku University (MEXT Scholarship)</li>
          <li><strong>Pre-2016</strong>: Engineering Degree and Project Engineer, University of Chile</li>
        </ul>
        <div class="profile-links">
          <a href="https://orcid.org/0000-0002-8194-4630" target="_blank" rel="noopener">ORCID</a>
          <a href="https://www.researchgate.net/profile/Leonardo-Stari" target="_blank" rel="noopener">ResearchGate</a>
          <a href="https://www.scopus.com/authid/detail.uri?authorId=58094418800" target="_blank" rel="noopener">Scopus</a>
          <a href="https://www.linkedin.com/in/leonardo-stari-661b7110b/" target="_blank" rel="noopener">LinkedIn</a>
        </div>
      </div>
    </div>
  </section>

  <section id="research">
    <h2>Research</h2>
    <p>
      My work focuses on microbial community formation and function, genome-based functional inference, and biodegradation. Recent projects include characterizing microbial consortia and isolating Pseudomonas strains capable of aerobic degradation of carbon tetrachloride, and assembling and analyzing complete genomes for these strains to investigate the genetic basis of degradation pathways. Key areas involve bacterial conjugation, plasmid partitioning, haloalkane dehalogenases (HLDs), and degradation of chlorinated compounds such as γ-hexachlorocyclohexane (γ-HCH), 1,1,1-trichloro-2,2-bis(4-chlorophenyl)ethane (DDT), and carbon tetrachloride (CCl4).
    </p>
  </section>

  <section id="metrics">
    <h2>Research Metrics</h2>
    <div class="metrics-card">
      <div><strong>Citations</strong><div class="metric-value" id="metric-citations">—</div></div>
      <div><strong>h-index</strong><div class="metric-value" id="metric-hindex">—</div></div>
      <div><strong>Publications</strong><div class="metric-value" id="metric-pubs">—</div></div>
    </div>
    <p class="metrics-note">Metrics are loaded from <code>/assets/data/metrics.json</code> or from your repository's scheduled update script. As of November 2025, based on available sources: ~12 citations, h-index ~2, ~11 publications (update the JSON file with latest values from Scopus or ResearchGate for accuracy).</p>
  </section>

  <section id="publications">
    <h2>Publications</h2>
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
            li.innerHTML = `${title} (${year})${doi ? ` <a href="https://doi.org/${doi}" target="_blank">[DOI]</a>` : ''}`;
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

<footer>
  <p>&copy; 2025 Leonardo Stari. Last updated: November 2025.</p>
</footer>