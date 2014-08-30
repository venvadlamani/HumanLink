	<script type="text/javascript" src="https://www.google.com/jsapi"></script>
	<script>
	  google.load('visualization', '1', {'packages': ['table', 'map', 'corechart']});
      google.setOnLoadCallback(initialize);

      function initialize() {
        // The URL of the spreadsheet to source data from.
        var query = new google.visualization.Query(
            'https://spreadsheets.google.com/pub?key=pCQbetd-CptF0r8qmCOlZGg');
        query.send(draw);
      }

      function draw(response) {
        if (response.isError()) {
          alert('Error in query');
        }
        
        // draw a Column Chart
        var ticketsData = response.getDataTable();
        var chart = new google.visualization.ColumnChart(
            document.getElementById('chart_div'));
        chart.draw(ticketsData, {'isStacked': true, 'legend': 'bottom',
            'vAxis': {'title': 'Number of tickets'}});
            
        //geo Coded Location Map
          var data = google.visualization.arrayToDataTable([
		    ['Lat', 'Long', 'Name'],
		    [37.4232, -122.0853, 'Work'],
		    [37.4289, -122.1697, 'University'],
		    [37.6153, -122.3900, 'Airport'],
		    [37.4422, -122.1731, 'Shopping']
		  ]);		  
		  var options = { showTip: true };
    	  var map = new google.visualization.Map(document.getElementById('geoCodedLocation_div'));
			map.draw(data, options);
                  	
      }   
      </script>