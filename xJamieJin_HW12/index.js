// All buttons & inputs
var $tbody = document.querySelector("tbody");
var $entries = document.querySelector("#pages");
var $nextBtn = document.querySelector("#next");
var $prevBtn = document.querySelector("#previous");
var $dateInput = document.querySelector("#date");
var $cityInput = document.querySelector("#city");
var $stateInput = document.querySelector("#state");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shapeInput");
var $filterBtn =  document.querySelector("#filter");

// initial variables
var dataSetFilter = dataSet.reverse();
var dataLength = dataSet.length;
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

// entries per page handler
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
$filterBtn.addEventListener("click", searchFilter)
function searchFilter() {
  var filterCity = $cityInput.value.trim().toLowerCase();
  var filterState = $stateInput.value.trim().toLowerCase();
  var filterCountry = $countryInput.value.trim().toLowerCase();
  var filterShape = $shapeInput.value.trim().toLowerCase();

  dataSetFilter = dataSet.filter(function(data) {
    var filterCityTemp = data.city.substring(0, filterCity.length).toLowerCase();
    var filterStateTemp = data.state.substring(0, filterState.length).toLowerCase();
    var filterCountryTemp = data.city.substring(0, filterCountry.length).toLowerCase();
    var filterShapeTemp = data.state.substring(0, filterShape.length).toLowerCase();
    
    if (filterCityTemp === filterCity 
      && filterStateTemp === filterState 
      && filterCountryTemp === filterCountry 
      && filterShapeTemp === filterShape) {
      return true;
    }
    return false;
  });
  renderTable();
}