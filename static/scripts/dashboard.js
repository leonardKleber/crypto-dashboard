var chart = new Chart(
    document.getElementById('chart'),
    config.chart.year
);
var doughnut_chart = new Chart(
    document.getElementById('doughnut_chart'),
    config.doughnut
);
function configure_dashboard(timeframe_id) {
    var chart_config;
    if(timeframe_id == 0) chart_config = config.chart.total;
    if(timeframe_id == 1) chart_config = config.chart.week;
    if(timeframe_id == 2) chart_config = config.chart.month;
    if(timeframe_id == 3) chart_config = config.chart.year;
    if(timeframe_id == 4) chart_config = config.chart.three_years;
    if(timeframe_id == 5) chart_config = config.chart.five_years;

    var existing_chart = Chart.getChart('chart').destroy();

    var chart = new Chart(
        document.getElementById('chart'),
        chart_config
    );
}