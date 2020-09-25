// Increase and decrease size of balloon. If it gets above a fixed size, it explodes.

<p style="font-size:20px;">🎈</p>

<script>
  // Your code here
  let balon = document.querySelector("p");
  let fntval = window.getComputedStyle(balon);
  let nummer = parseInt(fntval.getPropertyValue('font-size'));
  window.addEventListener("keydown", event => {
    if (event.key == "g") {
      nummer = (nummer + (nummer/10));
      balon.style.fontSize = nummer + "px";
      event.preventDefault();
    }
    if (event.key == "v") {
      nummer = (nummer - (nummer/10))
      balon.style.fontSize = nummer + "px";
      event.preventDefault();
    }   
  });
</script>