var caret = document.querySelector(".caret-parent .caret");
document.querySelectorAll("nav .nav-item").forEach(function (item) {
  item.addEventListener("mouseover", function (e) {
    e.stopPropagation();
    caret.style.width = e.currentTarget.offsetWidth - 16 + "px";
    caret.style.left = e.currentTarget.offsetLeft + 8 + "px";
  });
});

// if there is an element with class .splide
// then initialize the slider
if (document.querySelector(".splide")) {
  new Splide(".splide").mount();
}

function randomString(length) {
  let result = "";
  const characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  const charactersLength = characters.length;
  for (let i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
}

// Draw a random captcha string on the canvas
function drawCaptcha(canvas, captcha) {
  const ctx = canvas.getContext("2d");
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.font = "bold 30px Arial";
  ctx.fillText(captcha, canvas.width / 2 - 50, canvas.height / 2 + 10);
  ctx.fontColor = "black";
}

// Generate a new captcha
function generateCaptcha(canvas) {
  const captcha = randomString(5);
  drawCaptcha(canvas, captcha);
  return captcha;
}

const canvas = document.getElementById("captchaCanvas");
if (canvas) {
  generateCaptcha(canvas);
  canvas.setAttribute("data-captcha", captcha);
}