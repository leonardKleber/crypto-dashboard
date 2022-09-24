const chart_config = {
    type: 'line',
    data: {
        labels: [0,0],
        datasets: [{
            backgroundColor: 'rgb(255,0,0)',
            borderColor: 'rgb(255,0,0)',
            data: [0,0]
        }]
    },
    options: {
        scales: {
            xAxis: {
                display: false
            },
            yAxis: {
                display: false
            }
        },
        elements: {
            point: {
                radius: 0
            }
        },
        plugins: {
            legend: {
                display: false
            }
        }
    }
}
var chart = new Chart(
    document.getElementById('chart'),
    chart_config
);