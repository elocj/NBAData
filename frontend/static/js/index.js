$(document).ready(function(){
    $.get("http://127.0.0.1:5000/getPlayerKeys", function(data, status){
        data = JSON.parse(data);
        // alert(JSON.stringify(data));
        for(let i = 0; i < data.length; i++) {
            let val = JSON.stringify(data[i].name);
            var opt = document.createElement("option");
                opt.value = val;
                document.getElementById("names").appendChild(opt);
        }
    });
    // $('#go').submit(function() {
    let num = 10;
    if(document.getElementById('num').value) {
        num = document.getElementById('num').value;
        // alert(document.getElementById('num').value);
        // alert(document.getElementById('num').value);
    }
    $.get("http://127.0.0.1:5000/get_users", function(data, status){
        data = JSON.parse(data);
        // alert(JSON.stringify(data));
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
                    // alert(new Date(date[i][0], date[i][1], date[i][2]));
                    // alert(arr[i]);
                }
                dataPoints.sort(function(a,b){
                  return new Date(a.x) - new Date(b.x)
                });
                dataPoints = dataPoints.slice(dataPoints.length - num, dataPoints.length);
                let avg = 0;
                for(let i = 0; i < dataPoints.length; i++) {
                    avg += dataPoints[i].y;
                }
                avg /= dataPoints.length;
                var chart = new CanvasJS.Chart(val,
                    {
                        title:{
                            text: "(" + id + ") " + name +  " with the shot boy"
                        },
                        // theme: "dark1",
                        axisY: {
                            title: "Fantasy Score",
                            // valueFormatString: "#0,,.",
                            // suffix: "mn",
                            stripLines: [{
                                value: avg,
                                label: "Average"
                            }]
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
    // });
});