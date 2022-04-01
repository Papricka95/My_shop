let offset = 0; //Смещение от левого края
const sliderLine = document.querySelector('.slider-line')
const hero_info = document.querySelector('.hero__text')

// console.log(hero_info.children)

document.querySelector('.slider-next').addEventListener('click', function(){
  offset = offset + 256; //offset += 256
  if (offset > 768) {
    offset = 0;
  }
  sliderLine.style.left = -offset + 'px';
  // hero_info.children[0].textContent = `Цена из БД ${offset}`
  // console.log(hero_info.children[0].textContent)
});

document.querySelector('.slider-prev').addEventListener('click', function(){
  offset = offset - 256; //offset -= 256
  if (offset < 0 ) {
    offset = 768;
  }
  sliderLine.style.left = -offset + 'px';
  // hero_info.children[0].textContent = `Цена из БД ${offset}`
  // console.log(hero_info.children[0].textContent)
});

