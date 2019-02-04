document.addEventListener('DOMContentLoaded', () => {

    const province_element = document.querySelector('#province');
    const city_element = document.querySelector('#city');

    province_element.onchange = () => {

        if (province_element.value != 0) {

            const request = new XMLHttpRequest();
            const province_id = document.querySelector('#province').value;

            request.open('POST', '/province');
            const data = new FormData();
            data.append('province_id', province_id)
            request.send(data);

            request.onload = () => {
                const data = JSON.parse(request.responseText);
                const cities = data.cities;
                var optionHTML = '<option value="0">' +
                    'Select City' + '</option>';

                for (var city of cities) {
                    optionHTML +=
                        '<option value="' + city.id + '">' +
                        city.name + '</option>';
                }

                city_element.innerHTML = optionHTML;
            }
        }

        else {
            city_element.innerHTML = '<option value="0">Select Province First</option>';

        }
    }

    city_element.onchange = () => {

        const request = new XMLHttpRequest();

        const city_id = city_element.value;

        if (city_id != 0) {
            const city_name =
                city_element.selectedOptions[0].text;

            request.open('POST', '/city/' + city_id);
            request.send();

            request.onload = () => {
                const data = JSON.parse(request.responseText);
                const population = data.population;

                document.querySelector('#pop_label').innerHTML =
                    `${city_name} population is ${population}.`;
            }
        }

    }
});