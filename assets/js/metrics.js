// loads /assets/data/metrics.json and fills elements with ids metric-citations, metric-hindex, metric-pubs
(function(){
  const elC = document.getElementById('metric-citations');
  const elH = document.getElementById('metric-hindex');
  const elP = document.getElementById('metric-pubs');

  function setPlaceholders() {
    if (elC) elC.textContent = '—';
    if (elH) elH.textContent = '—';
    if (elP) elP.textContent = '—';
  }

  fetch('/assets/data/metrics.json', { cache: 'no-store' })
    .then(function(response) {
      if (!response.ok) throw new Error('no metrics');
      return response.json();
    })
    .then(function(j) {
      if (elC) elC.textContent = (j && j.citations != null) ? j.citations : '—';
      if (elH) elH.textContent = (j && j.hindex != null) ? j.hindex : '—';
      if (elP) elP.textContent = (j && j.pubs != null) ? j.pubs : '—';
    })
    .catch(function() {
      // Fallback: show neutral placeholders
      setPlaceholders();
    });
})();