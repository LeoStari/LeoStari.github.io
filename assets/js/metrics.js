// Safe metrics.js — pure JavaScript, no Jekyll/Liquid inside
(function(){
  const elC = document.getElementById('metric-citations');
  const elH = document.getElementById('metric-hindex');
  const elP = document.getElementById('metric-pubs');

  function setPlaceholders() {
    if (elC) elC.textContent = '—';
    if (elH) elH.textContent = '—';
    if (elP) elP.textContent = '—';
  }

  function applyMetrics(j) {
    if (elC) elC.textContent = (j && (j.citations !== undefined && j.citations !== null)) ? j.citations : '—';
    if (elH) elH.textContent = (j && (j.hindex !== undefined && j.hindex !== null)) ? j.hindex : '—';
    if (elP) elP.textContent = (j && (j.pubs !== undefined && j.pubs !== null)) ? j.pubs : '—';
  }

  // Try to fetch the JSON metrics file
  fetch('/assets/data/metrics.json', { cache: 'no-store' })
    .then(function(response) {
      if (!response.ok) throw new Error('no metrics');
      return response.json();
    })
    .then(function(j) {
      applyMetrics(j);
    })
    .catch(function() {
      // If fetch fails, try to read window.siteMetrics (if embedded inline by Jekyll)
      try {
        if (window && window.siteMetrics) {
          applyMetrics(window.siteMetrics);
        } else {
          setPlaceholders();
        }
      } catch (e) {
        setPlaceholders();
      }
    });
})();