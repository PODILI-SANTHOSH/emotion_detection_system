const ctx = document.getElementById("chart");
const emotionText = document.getElementById("emotion");
const confidenceText = document.getElementById("confidence");

let labels = [];
let data = [];

const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'Confidence %',
            data: data,
            borderColor: '#00ffd5',
            tension: 0.4
        }]
    }
});

function updateStatus() {
    fetch("/status")
        .then(res => res.json())
        .then(d => {
            emotionText.innerText = "Emotion: " + d.emotion;
            confidenceText.innerText = "Confidence: " + d.confidence + "%";

            if (labels.length > 10) {
                labels.shift();
                data.shift();
            }

            labels.push(d.emotion);
            data.push(d.confidence);
            chart.update();
        });
}

function toggleDetect() {
    fetch("/toggle");
}

setInterval(updateStatus, 1000);
