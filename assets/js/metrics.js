// loads /assets/data/metrics.json and fills elements with ids metric-citations, metric-hindex, metric-pubs
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
      // If metrics file not present yet, use site config values (if provided)
      try {
        const conf = {{ site.data.metrics | jsonify }};
        if (elC) elC.textContent = conf.citations || '—';
        if (elH) elH.textContent = conf.hindex || '—';
        if (elP) elP.textContent = conf.pubs || '—';
      } catch(e) {
        // no-op
      }
    });
})();