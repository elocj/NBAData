$(document).ready(function(){
    $.get("http://127.0.0.1:5000/get_users", function(data, status){
        data = JSON.parse(data);
        alert(JSON.stringify(data));
        for(let i = 0; i < data.length; i++) {
            let val = JSON.stringify(data[i].userID);
            $.get("http://127.0.0.1:5000/get_data/" + val, function(data, status){
                data = JSON.parse(data);
                // alert("Data: " + JSON.stringify(data.date) + "\nStatus: " + status);
                date = data.date;
                arr = data.arr;
                name = data.name;
                id = data.id;
                var div = document.createElement("div");
                div.style.width = "100%";
                div.id = val;
                div.style.height = "300px";
                document.body.appendChild(div);

                var dataPoints = [];
                for (var i = 0; i < date.length; i++) {
                    dataPoints.push({
                        x: new Date(date[i][0], date[i][1], date[i][2]),
                        y: arr[i]
                    });
                }
                var chart = new CanvasJS.Chart(val,
                    {
                        title:{
                            text: "(" + id + ") " + name +  " with the shot boy"
                        },
                        data: [{
                            type: "line",
                            dataPoints: dataPoints
                        }
                    ]
                });
                chart.render();
            });
        }
    });
});