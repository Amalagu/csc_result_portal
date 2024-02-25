export function barChart(data) {
    const ctx = document.getElementById('bar-chart');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['500 LVL', '400 LVL', '300 LVL', '200 LVL', '100 LVL'],
            datasets: [
                {
                    label: 'CGPA',
                    data: data,
                    borderWidth: 1,
                    backgroundColor: [
                        '#A2DF92',
                        '#F9C394',
                        '#EED792',
                        '#FF9E95',
                        '#91A48C',
                    ]
                }
            ],
        },
        options: {
            indexAxis: 'y',
            scales: {
                y: {
                beginAtZero: true
                }
            }
        }
    })
}

export function lineChart(data) {
    const ctx2 = document.getElementById('line-chart');
    new Chart(ctx2, {
        type: 'line',
        data: {
            labels: ['100 LVL', '200 LVL', '300 LVL', '400 LVL', '500 LVL'],
            datasets: [
                {
                    label: 'CGPA',
                    data: data.reverse(),
                    borderWidth: 1,
                    backgroundColor: [
                        '#A2DF92',
                        '#F9C394',
                        '#EED792',
                        '#FF9E95',
                        '#91A48C',
                    ]
                }
            ],
        },
        options: {
            scales: {
                y: {
                beginAtZero: true
                }
            }
        }
    })
}