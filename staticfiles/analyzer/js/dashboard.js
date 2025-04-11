let selectedStock = null;
const chartLabels = [];
const chartPrices = [];

const chartConfig = {
    type: "line",
    data: {
        labels: chartLabels,
        datasets: [{
            label: "Price",
            data: chartPrices,
            borderColor: "blue",
            borderWidth: 2,
            tension: 0.3,
            fill: false
        }]
    },
    options: {
        responsive: true,
        plugins: { legend: { display: true } },
        scales: {
            x: { title: { display: true, text: "Time" }},
            y: { title: { display: true, text: "Price ($)" }}
        }
    }
};

const priceChart = new Chart(
    document.getElementById("priceChart"),
    chartConfig
);
