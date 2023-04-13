import { useState, useEffect } from 'react';

function HomePage() {
  const [ipInfo, setIpInfo] = useState({});
  const [reverseGeoCode, setReverseGeoCode] = useState({});
  const [buttonDisabled, setButtonDisabled] = useState(true);

  useEffect(() => {
    const fetchIpInfo = async () => {
      const response = await fetch('https://ipinfo.io/json?token=c2aec1583cf4d1');
      const data = await response.json();
      setIpInfo(data);
      setButtonDisabled(false);
      localStorage.setItem('country', data.country);
    };

    fetchIpInfo();
  }, []);

  async function fetchReverseGeoCode() {
    const response = await fetch(`https://api.opencagedata.com/geocode/v1/json?key=a02f38298198484c92e1343a5f1ee8fa&q=${ipInfo.loc}&pretty=1&no_annotations=1`);
    const data = await response.json();
    
    const formattedData = {
      city: data.results[0].components.city,
      country: data.results[0].components.country,
      countryCode: data.results[0].components["ISO_3166-1_alpha-2"],
      state: data.results[0].components.state,
      postcode: data.results[0].components.postcode
    };
  
    localStorage.setItem('country', formattedData.countryCode);
  
    // create table with formatted data
    const table = document.createElement('table');
    for (const key in formattedData) {
      const row = table.insertRow();
      const cell1 = row.insertCell();
      const cell2 = row.insertCell();
      cell1.innerText = key;
      cell2.innerText = formattedData[key];
    }
  
    document.body.appendChild(table);
  }
  
  
  return (
    <div>
      <h1>IP Info</h1>
      {/* <p>IP Address: {ipInfo.ip}</p>
      <h2>Hostname: {ipInfo.hostname}</h2>
      City: {ipInfo.city}
      Region:{ipInfo.region}
      Country:{ipInfo.country}
      Postal Code:{ipInfo.postal} */}

      <table>
        <tbody>
          <tr>
            <td>IP Address:</td>
            <td>{ipInfo.ip}</td>
          </tr>
          <tr>
            <td>Hostname:</td>
            <td>{ipInfo.hostname}</td>
          </tr>
          <tr>
            <td>City:</td>
            <td>{ipInfo.city}</td>
          </tr>
          <tr>
            <td>Region:</td>
            <td>{ipInfo.region}</td>
          </tr>
          <tr>
            <td>Country:</td>
            <td>{ipInfo.country}</td>
          </tr>
          <tr>
            <td>Postal Code:</td>
            <td>{ipInfo.postal}</td>
          </tr>
          <tr>
            <td>Timezone:</td>
            <td>{ipInfo.timezone}</td>
          </tr>
        </tbody>
      </table>
      <button onClick={fetchReverseGeoCode} disabled={buttonDisabled}>
        Reverse GeoCode Location
      </button>
      {Object.keys(reverseGeoCode).length > 0 && (
        <table>
          <tbody>
            <tr>
              <td>Formatted:</td>
              <td>{reverseGeoCode.formatted}</td>
            </tr>
            <tr>
              <td>City:</td>
              <td>{reverseGeoCode.components.city}</td>
            </tr>
            <tr>
              <td>State:</td>
              <td>{reverseGeoCode.components.state}</td>
            </tr>
            <tr>
              <td>Country:</td>
              <td>{reverseGeoCode.components.country}</td>
            </tr>
          </tbody>
        </table>
      )}
    </div>
  );
}
export default HomePage;
