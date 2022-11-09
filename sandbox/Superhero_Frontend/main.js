data = [];

function callTheAPI() {
    console.log("Button has been clicked.");
    axios.get('https://8000-rdmullins-djangosandbox-2im0hh8gjgr.ws-us75.gitpod.io/herolist/')
    .then(function (response) {
    // handle success
    console.log(response);
    data = response;
    showTheData();
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
}

function showTheData() {
    console.log(data);
    let d = document.getElementById("testResults");
    let arrayOfAPI = data.data;
    console.log(arrayOfAPI);
    let divTextString = "";
    for (let i=0; i<arrayOfAPI.data.length; i++) {
        divTextString = divTextString + "\n" + arrayOfAPI.data[i].name + "\n\t" + arrayOfAPI.data[i].about + "\n\t" + arrayOfAPI.data[i].bio + "\n\n";
    };
    d.innerText = divTextString;
    //usableData = JSON.parse(data);
    //console.log(usableData);
}