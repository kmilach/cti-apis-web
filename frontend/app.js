const apiNameMap = {
  apiKeyPulsedive: 'pulsedive',
  apiKeyVirusTotal: 'virustotal',
};

// API request
function makeRequestToBackendApi(api, query, key) {
  const url = `http://localhost:5000/api?api=${encodeURIComponent(api)}&query=${encodeURIComponent(query)}&key=${encodeURIComponent(key)}`;
  const options = {
      method: 'GET',
      headers: {
          accept: 'application/json',
      }
  };
  
  //request to ThreatIntel API
  fetch(url, options)
  .then(response => response.json()) //parse with json() function
  .then(response => console.log(response)) //data to be displayed
  .catch(err => console.error(err)); //error handling
}

//event listener to the forms
const errorMessage = document.getElementById('error');
const form = document.getElementById('queryForm');

form.addEventListener('submit', function(event) {
  event.preventDefault(); //this prevents the form from submitting and refreshing the page
  
  const query = document.getElementById('query').value;
  const keys = document.getElementsByClassName('api-key');

  for (const key of keys) {
    if (key.value != '') {
      makeRequestToBackendApi(apiNameMap[key.id], query, key.value);
    }
  };
})