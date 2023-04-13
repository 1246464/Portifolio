function updateClock() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();
  
    // Adiciona um zero à esquerda dos números menores que 10
    if (hours < 10) {
      hours = "0" + hours;
    }
    if (minutes < 10) {
      minutes = "0" + minutes;
    }
    if (seconds < 10) {
      seconds = "0" + seconds;
    }
  
    // Atualiza o relógio
    var clock = document.getElementById("clock");
    clock.textContent = hours + ":" + minutes + ":" + seconds;
  }
  
  // Chama a função updateClock a cada segundo
  setInterval(updateClock, 1000);
  