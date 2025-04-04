# kriptoloji-cryptology
şifreli mesajın çözümü.
İlk aşama, şifreyi çözebilmek için doğru asal sayıyı bulmak. Bu asal sayı, 50000 ile 100000 arasındaki bir sayıdır.
Bu asal sayılar her şifreleme işlemi için farklı olacaktır.
İkinci aşama, algoritm = (((B**E1 % M1)**E2 % M2)**E3 % M3) 
B: İlk adımda bulunan asal sayıdır. 
E₁, E₂ ve E₃: Her modüler üs alma işlemi için kullanılan üslere, E₁, E₂, ve E₃'ün doğru seçilmesi gerekir. 
Bu üsler 3 ile 11 arasındaki tek sayılar arasından seçilecektir. 
M₁, M₂ ve M₃: birbirinden farklı sabit modül değerleridir. Bu modüller şifreyi çözebilmek için doğru hesaplamalar 
yapmanız gereken değerlerdir, ancak bu değerler bilinmemektedir. Bu değerler 1000 ile 8000 arasında bir sayı alacaktır.  
Bu şifreleme işleminde, her bir modüler üs alma adımı bağımsız bir işlem olduğu için, doğru üs ve modül değerleriyle 
hesaplamalar yapılmalıdır. 
Son aşama ise, [72 105 115 115 32 109 97 121 98 101 111 100 101 111 110] şifresinin çözümüdür. Mesaj sayısal bir değer çıkacaktır.
