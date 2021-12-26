let offset = 0; //Смещение от левого края
const sliderLine = document.querySelector('.slider-line')

document.querySelector('.slider-next').addEventListener('click', function(){
  offset = offset + 256; //offset += 256
  if (offset > 768) {
    offset = 0;
  }
  sliderLine.style.left = -offset + 'px';
});

document.querySelector('.slider-prev').addEventListener('click', function(){
  offset = offset - 256; //offset -= 256
  if (offset < 0 ) {
    offset = 768;
  }
  sliderLine.style.left = -offset + 'px';
});