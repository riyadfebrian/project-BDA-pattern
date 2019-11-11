# Pattern Project BDA
konsepnya <b>Konversi dari .ipynb ke file .py trus dijalanin di backend views.py django.</b>
dengan cara ini, menurut saya lebih cepat dalam konversi koding dan lebih mudah dalam me-maintain atau melakukan debugging ketika ada error. walaupun saya ga tau ini bagus apa nggak untuk performansi. but, its work !!!


## Setelah konversi, coba cek dulu di terminal
<p align="center">
  <img src="https://github.com/riyadfebrian/project-BDA-pattern/blob/master/media/run_via_terminal.png">
</p>

## Upload ke direktori yang ada di django
<p align="center">
  <img  src="https://github.com/riyadfebrian/project-BDA-pattern/blob/master/media/pyfilestructure.png">
</p>

## Kodingan pada views.py
<p align="center">
  <img src="https://github.com/riyadfebrian/project-BDA-pattern/blob/master/media/apiviews.png">
</p>
return bisa dalam bentuk response atau render. terserah. tapi saya pake return JSONresponse agar mudah dalam komunikasi mobile

