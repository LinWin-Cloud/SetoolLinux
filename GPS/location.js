﻿function logon(){
    window.navigator.geolocation.getCurrentPosition(function (position) {
        console.log(position.coords.latitude)
        console.log(position.coords.longitude)
        var x = position.coords.latitude;
        var y = position.coords.longitude;
        info="'"+"latitude="+x+";"+"longitude="+y
        window.location.href=info
    })  
}
 
