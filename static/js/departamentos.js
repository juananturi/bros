
const apiInfo = document.getElementById("apiInfo");
const selectDepartment = document.getElementById("selectDepartment");
const selectCity = document.getElementById("selectCity");
let departmentsId = [];

let url = "https://www.datos.gov.co/resource/xdk5-pm3f.json";

const apiDepartment = () => {
  destination = fetch(url)
    .then((res) => res.json())
    .then((data) => {
      data.forEach((smallData) => {
        if (!departmentsId.includes(smallData.c_digo_dane_del_departamento)) {
          departmentsId.push(smallData.c_digo_dane_del_departamento);
          selectDepartment.innerHTML += `<option value="${smallData.c_digo_dane_del_departamento}">${smallData.departamento}</option>`;
        }
      });
    });
};
apiDepartment();

selectDepartment.addEventListener("change", function updateDepartment() {
    selectCity.innerHTML = '';

  idD = selectDepartment.value;
  let cities = url + "?c_digo_dane_del_departamento=" + idD;
  console.log(cities);
  fetch(cities)
    .then((res) => res.json())
    .then((data) => {
        data.forEach((smallData) => {
            
        selectCity.innerHTML += `<option value="${smallData}">${smallData.municipio}</option>`;
        console.log(smallData.municipio)
      });
      
    });
});