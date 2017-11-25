// Cleaning data
function dataClean(){
  for(i=0;i<dataSet.length; i++){
    dataSet[i].country.toUpperCase();
    dataSet[i].state.toUpperCase();
  }
};
           
dataClean();

// All buttons & inputs
var $tbody = document.querySelector("tbody");
var $entries = document.querySelector("#pages");
var $nextBtn = document.querySelector("#next");
var $prevBtn = document.querySelector("#previous");

// initial variables
var dataSetFilter = dataSet.reverse();
var dataLength = dataSetFilter.length;
var startIdx = 0;
var endIdx = +$entries.value;

// Initial rendering of table
function renderTable() {
  $tbody.innerHTML = "";
  var alienSubset = dataSetFilter.slice(startIdx, endIdx);
  
  for (var i = 0; i < alienSubset.length; i++) {
    var aliencurrent = alienSubset[i];
    var alienrow = Object.keys(aliencurrent);

    var $row = $tbody.insertRow(i);
    for (var j = 0; j < alienrow.length; j++) {
      
      var alienpoint = alienrow[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = aliencurrent[alienpoint];
    }
  }
}
renderTable();

// Entries per page handler
$entries.addEventListener("change",function(){
  startIdx = 0;
  endIdx = +$entries.value
  renderTable();
})

// Next & Previous page button config
$nextBtn.addEventListener("click", function(event){
  event.preventDefault();
  startIdx += +$entries.value;
  endIdx += +$entries.value;

  if (dataLength <= endIdx){
    endIdx = dataLength;
    $nextBtn.classList.add('disabled');
  }
  else if (startIdx > $entries.value){
    $prevBtn.classList.remove('disabled');
  }
  renderTable();
});

$prevBtn.addEventListener("click", function(event){
  event.preventDefault();
  startIdx -= +$entries.value;
  endIdx -= +$entries.value;

  if (startIdx == 0){
    $prevBtn.classList.add('disabled');
  }
  renderTable();
});

// Filter
var $filterBtn =  document.querySelector("#filter");
$filterBtn.addEventListener("click", searchFilter)
function searchFilter() {
  // var filterDate = $dateInput.value.trim().toLowerCase();
  var filterCity = document.querySelector("#city").value.trim().toLowerCase();
  var filterState = document.querySelector("#state").value.trim().toLowerCase();
  var filterCountry = document.querySelector("#country").value.trim().toLowerCase();
  var filterShape = document.querySelector("#shape").value.trim().toLowerCase();

  dataSetFilter = dataSet.filter(function(dataTemp) {
    // var filterDateTemp = dataTemp.city.substring(0, filterDate.length).toLowerCase();
    var filterCityTemp = dataTemp.city.substring(0, filterCity.length).toLowerCase();
    var filterStateTemp = dataTemp.state.substring(0, filterState.length).toLowerCase();
    var filterCountryTemp = dataTemp.country.substring(0, filterCountry.length).toLowerCase();
    var filterShapeTemp = dataTemp.shape.substring(0, filterShape.length).toLowerCase();
    
    if (filterCityTemp === filterCity && filterStateTemp === filterState && filterCountryTemp === filterCountry && filterShapeTemp === filterShape) {
      return true;
    }
    return false;
  });
  renderTable();
};
