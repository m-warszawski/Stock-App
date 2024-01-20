 function drawChart(chartName, chartColor, chartType, chartLegend){
    console.log(chartName)
       var chartData = convertToJSON(document.getElementById(chartName).innerHTML);
        if(chartData) {

            var chartLabels = [];
            var chartValues = [];

            for (let i = chartData.length - 1; i >= 0; i--) {
                chartLabels.push(chartData[i].date);
                chartValues.push(parseFloat(chartData[i].value));
            }

            chartLabels = chartLabels.slice(125, chartData.length);
            chartValues = chartValues.slice(125, chartData.length);

            console.log(chartData)
            console.log(chartLabels);
            console.log(chartValues);

            var ctx = document.getElementById(chartName).getContext('2d');

            var data = {
                labels: chartLabels,
                datasets: [{
                    label: chartLegend,
                    backgroundColor: chartColor,
                    borderColor: chartColor,
                    borderWidth: 2,
                    data: chartValues
                }]
            };

            var options = {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            };

            var commoditiesChart = new Chart(ctx, {
                type: chartType,
                data: data,
                options: options
            });
        }
}

function convertToJSON(dataString) {
    try {
        // Zamiana pojedynczych cudzysłowów na podwójne i usuwanie apostrofów
        const jsonString = dataString.replace(/'/g, "\"").replace(/(\w+:)|(\w+ :)/g, function(matchedStr) {
            return '"' + matchedStr.substring(0, matchedStr.length - 1) + '":';
        });

        // Parsowanie ciągu tekstowego jako JSON
        const jsonData = JSON.parse(jsonString);

        return jsonData;
    } catch (error) {
        console.error("Błąd podczas konwersji:", error.message);
        return null;
    }
}

 document.addEventListener('DOMContentLoaded', function () {
     drawChart("indicatorsFirstChart", "rgb(242, 56, 90)", "bar", "-");
     drawChart("indicatorsSecondChart", "rgb(242, 56, 90)", "bar", "-");
     drawChart("indicatorsFourthChart", "rgb(242, 56, 90)", "bar", "-");

     drawChart("commoditiesZeroChart", "#218fa6", "line", "-");
     drawChart("commoditiesFirstChart", "#218fa6", "line", "-");
     drawChart("commoditiesSecondChart", "#218fa6", "line", "-");
     drawChart("commoditiesThirdChart", "#218fa6", "line", "-");

 });