
    google.load('visualization', '1', {'packages': ['geochart', 'corechart', 'gauge']});
    google.setOnLoadCallback(drawRegionsMap);
    google.setOnLoadCallback(drawUsageChart);
    google.setOnLoadCallback(drawSentimentChart);

    
    
      function drawRegionsMap() {
        var data = google.visualization.arrayToDataTable([
          ['Province', 'Usage'],
          ['AR', 500],
          ['TX', 600],
          ['NY', 300],
          ['MO', 200],
          ['FL', 300]
        ]);

        var options = {region: 'US', displayMode: 'regions', resolution: 'provinces' };

        var chart = new google.visualization.GeoChart(document.getElementById('chart_usage'));
        chart.draw(data, options);
    };


    function drawUsageChart() {
      var data = google.visualization.arrayToDataTable([
        ['Month', '$mm Spend'],
        [new Date(2013, 1),  1000],
        [new Date(2013, 2),  1170],
        [new Date(2013, 3),  660],
        [new Date(2013, 4),  1030],
        [new Date(2013, 5),  400],
        [new Date(2013, 6),  200],
        [new Date(2013, 7),  350],
        [new Date(2013, 8),  3542],
        [new Date(2013, 9),  345],
        [new Date(2013, 10),  3245],
        [new Date(2013, 11),  879],
        [new Date(2013, 12),  374],
        [new Date(2014, 1),  3245],
        [new Date(2014, 2),  1170],
        [new Date(2014, 3),  660],
        [new Date(2014, 4),  1030],
      ]);

      var options = {
        title: 'Caregiver services',
        curveType: 'function',
        is3D: true
      };

      var chart = new google.visualization.AreaChart(document.getElementById('chart_monthly'));
      chart.draw(data, options);
    }
    
    
    function drawSentimentChart() {
        var data = google.visualization.arrayToDataTable([
          ['Label', 'Value'],
          ['Affordable', 80],
          ['Reliable', 55],
          ['Very Helpful', 68]
        ]);

        var options = {
          width: 1100, height: 420,
          redFrom: 90, redTo: 100,
          yellowFrom:75, yellowTo: 90,
          minorTicks: 5
        };

        var chart = new google.visualization.Gauge(document.getElementById('chart_sentiment'));
        chart.draw(data, options);
      }