$(document).ready(function(){
    $.get("http://127.0.0.1:5000/get_data", function(data, status){
        data = JSON.parse(data);
        alert("Data: " + JSON.stringify(data.date) + "\nStatus: " + status);
        date = data.date;
        arr = data.arr;
        var dataPoints = [];
        for (var i = 0; i < date.length; i++) {
            dataPoints.push({
                x: new Date(date[i][0], date[i][1], date[i][2]),
                y: arr[i]
            });
        }
        var chart = new CanvasJS.Chart("chartContainer",
            {
                title:{
                    text: "Steph Curry with the shot boy"
                },
                data: [{
                    type: "line",
                    dataPoints: dataPoints
                }
            ]
        });
        chart.render();
    });
});