document.querySelector('button').addEventListener('click', _ => {
  
  const om = document.querySelector('#sucs')
  var stat = document.querySelector('#status')
  var inputs = document.getElementsByClassName("form-control")
  if ((inputs[0].value == '') || (inputs[1].value == '')){
    stat.innerHTML = 'Не все поля заполнены'
    om.style.display = 'block'
    om.style.color = 'red'
    return
  }

  om.style.display = 'block'
  om.style.color = 'green'
  stat.innerHTML = 'Ваша заявка успешно отправлена. Мы скоро с вами свяжемся!'
  inputs[0].value = ''
  inputs[1].value = ''
  //om.addEventListener('click', _ => {
  //  om.style.display = 'none'
  //}, {once: true})
})