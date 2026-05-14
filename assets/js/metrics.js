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

  // Try multiple fetch locations for metrics data
  const possiblePaths = [
    '/data/metrics.json',      // Jekyll copies _data/ to root
    '/assets/data/metrics.json',
    '/_data/metrics.json'
  ];

  function tryFetch(paths, index) {
    if (index >= paths.length) {
      // All paths failed, use fallback
      try {
        if (window && window.siteMetrics) {
          applyMetrics(window.siteMetrics);
        } else {
          setPlaceholders();
        }
      } catch (e) {
        setPlaceholders();
      }
      return;
    }

    fetch(paths[index], { cache: 'no-store' })
      .then(function(response) {
        if (!response.ok) throw new Error('not found');
        return response.json();
      })
      .then(function(j) {
        applyMetrics(j);
      })
      .catch(function() {
        tryFetch(paths, index + 1);
      });
  }

  tryFetch(possiblePaths, 0);
})();
