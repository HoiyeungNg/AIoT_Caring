let heartRates = [];
let temperatures = [];
let bodyStatuses = [];
let updateTimes = [];

function setStatusAlert() {
  const statusIndicator = document.querySelector('#status-indicator');
  statusIndicator.textContent = 'Alert';
  statusIndicator.classList.add('alert');
}

function setStatusNormal() {
  const statusIndicator = document.querySelector('#status-indicator');
  statusIndicator.textContent = 'Normal';
  statusIndicator.classList.remove('alert');
}

// function poll(url, interval) {
//   setInterval(() => {
//     axios.get(url)
//       .then(response => {
//         // handle success
//         console.log(response.data);
//       })
//       .catch(error => {
//         // handle error
//         console.log(error);
//       });
//   }, interval);
// }

// start polling
// poll('http://127.0.0.1:8000/mycare/body', 1000);

axios.all([
  axios.get('http://127.0.0.1:8000/mycare/heart_rate'),
  axios.get('http://127.0.0.1:8000/mycare/temperature'),
  axios.get('http://127.0.0.1:8000/mycare/body')
])
.then(axios.spread((heartRateResponse, temperatureResponse, bodyStatusResponse) => {
  // handle success
  heartRates = heartRateResponse.data.map(item => parseFloat(item.heart_rate));
  console.log(heartRates);

  temperatures = temperatureResponse.data.map(item => parseFloat(item.temperature));
  console.log(temperatures);

  bodyStatuses = bodyStatusResponse.data.map(item => item.body_status);
  console.log(bodyStatuses);

  updateTimes = heartRateResponse.data.map(item => item.update_time);
  console.log(heartRates);
  console.log(updateTimes);

  let count = 0;
  let tableBody = document.querySelector('#heart-rate-data tbody');
  for (let i = 0; i < heartRates.length; i++) {
    if (heartRates[i] > 100) {
      count++;
      // add update time to table
      let newRow = tableBody.insertRow();
      newRow.insertCell().textContent = updateTimes[i];
    }
  }
  console.log(`Heart rate exceeded 100 ${count} times.`);
  }))
.catch(error => {
  // handle error
  console.log(error);
});