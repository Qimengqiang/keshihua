fetch('/api/accidents/')
    .then(response => response.json())
    .then(data => {
        data.forEach(item => {
            var point = new BMap.Point(item.lng, item.lat);
            var marker = new BMap.Marker(point);
            map.addOverlay(marker);
        });
    });