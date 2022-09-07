function updateTimer() {
    var counter = 0;
    setInterval(function() {
        if(counter == 60) return;
        counter = counter + 1;
        var minutes = 60 - counter
        if(minutes > 9) {
            minutes_string = minutes.toString();
            var string = '00:' + minutes_string;
            document.querySelector('#time').innerHTML = string;

        } else {
            minutes_string = minutes.toString();
            var string = '00:0' + minutes_string;
            document.querySelector('#time').innerHTML = string;
        }
    }, 1500)
}
updateTimer()