document.addEventListener('DOMContentLoaded', () => {
    const lineCtx = document.getElementById('lineChart');
    const pieCtx = document.getElementById('pieChart');
    const barCtx = document.getElementById('barChart');

    if (lineCtx) {
        new Chart(lineCtx, {
            type: 'line',
            data: {
                labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
                datasets: [{
                    label: 'Clientes activos',
                    data: [30, 50, 40, 60, 55, 70],
                    borderColor: '#21eac6',
                    backgroundColor: 'rgba(33,234,198,0.1)',
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                plugins: {legend: {display: false}}
            }
        });
    }

    if (pieCtx) {
        new Chart(pieCtx, {
            type: 'pie',
            data: {
                labels: ['Leales', 'En riesgo', 'Fuga'],
                datasets: [{
                    data: [60, 25, 15],
                    backgroundColor: ['#b888ff', '#21eac6', '#007bff']
                }]
            },
            options: {responsive: true}
        });
    }

    if (barCtx) {
        new Chart(barCtx, {
            type: 'bar',
            data: {
                labels: ['Producto A', 'Producto B', 'Producto C'],
                datasets: [{
                    label: 'Ventas',
                    data: [150, 200, 100],
                    backgroundColor: '#007bff'
                }]
            },
            options: {responsive: true,
                plugins: {legend: {display: false}}}
        });
    }
});
