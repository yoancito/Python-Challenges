import sympy as sy
import numpy as np

def inverso_n(a,n):
  "Calcula el inverso de a módulo n"
  if np.gcd(a,n) == 1:
      for i in range(1,n):
        if (a*i % n) == 1:
          return i
  else:
    return "{} No tiene inverso módulo {}".format(a,n)

def key_gen(P,Q,N,PHIN):
  for e in range(2,phin):
    if np.gcd(e,phin) == 1:
      d = inverso_n(e,phin)
      return d,e  #Tambien podria devolver p,q pero no es necesario


def cifrado(texto,abc,clave1,clave2):
  longitud = len(texto)
  longitudAbc = len(abc)
  newlist = []
  for i in range(0,longitud):
    for m in range(0,longitudAbc):
      if texto[i] == abc[m]:
        s = m**clave1 % clave2
        newlist.append(s)
  return newlist

def decrypt(pos, privkey, N):
    decipher = [];
    for x in range(len(pos)):
      temp = (pos[x] ** privkey) % N;
      decipher.append(temp);
    return decipher

def traducirMensaje(desi,lista):
  longitud = len(desi)
  longitudAbc = len(lista)
  listaNue = []
  for i in range(0,longitud):
    for m in range(0,longitudAbc):
      if desi[i] == m:
        s = lista[m]
        listaNue.append(s)
  cadena = "".join(listaNue)
  return  cadena

'''1.   Forme la lista L con los caracteres que va a utilizar para cifrar y/o descifrar mensajes.'''

Lista = ['a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, á, é, í, ó, ú, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, Á, É, Í, Ó, Ú, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, +, -, *, /, ^, %, #, $, @, SP, ,, ;, ., :, ¿, ?, ¡, !, (, ), [, ], {, }, \ , =, ¬, ñ, Ñ, ü, Ü,  ']
Lista = Lista[0].split(', ')
print(Lista)

'''2.   Ingrese 2 números primos arbitrarios diferentes que, a partir de este momento se llamarán p, 
q tales que, tengan al menos 2 cifras.'''

p = 197
q = 97
print('p,q =',p,q)

'''3.   Calcule le valor de n, el cual será la base Zn (de enteros no negativos menores n) 
como el producto de p y qñ es decir n=p*q.'''

13289, 5
n = 13289 #p*q
print('n =',n)

'''4.   Calcule la función cociente de Euler phi(n) que corresponde a la cantidad de enteros 
entre 1 y n que son primos relativos de n, el cual nos interesa en el sistema RSA para n=p*q,
 siendo p y q números primos diferentes. Veamos, 
phi(n)= phi(p.q)=p.q-p-q+1=(p-1).(q-1)'''

phin = (p-1)*(q-1)
print('phin =',phin)

'''5.   Genere las claves (pública y privada).
Clave pública (e): es un número aleatorio primo relativo entre 1 y phi(n)
Seleccione, de manera aleatoria, un número entre 1 y phi(n), tal que mcd(e, phi(n))=1. 
Dicho valor corresponderá a la clave publica “e”.
Clave privada (d): corresponde al número phi(n) del módulo del producto de los números enteros 
entre 1 y phi por la clave publica “e”, con phi(n). Es decir, d(phi(n))=(e*phi(n)) MOD phi(n)=1 '''

key = key_gen(p,q,n,phin)
d,e = key


'''6.   Envíe clave pública al EMISOR que corresponde a los parámetros n y e, la cual pueden ver todos.
 Entre el EMISOR y el RECEPTOR envían de manera oculta la clave privada n y d.'''

pub_key = (n,e)
print('clave publica = ',pub_key)
pri_key = d
print('clave pribada = ',pri_key)

'''7.   Cifrado: envíe el mensaje que corresponde a la lista M de las posiciones de cada carácter.  
Ahora forme una lista C con los caracteres cifrados. Efectivamente, forme una lista C con los módulos n 
de la potencia cada posición de la lista M, elevada a la clave pública. Dicha lista resultante corresponderá al 
mensaje encriptado. Ahora, muestre el mensaje cifrado; basta con concatenar, según la lista C, 
los caracteres de la lista L. '''

mensaje = input('Ingrese el mensaje: ')
list_mensaje = list(mensaje)
print('La lista de el mensaje es: ',list_mensaje)
cifrar = cifrado(list_mensaje,Lista,e,n)
print('El mensaje cifrado es: ',cifrar)

'''8.   Descifrado: Tome los módulos n de la potencia cada posición de la lista C, elevada a la clave privada.
Dicha lista resultante corresponderá al mensaje encriptado. Para mostrar el mensaje descifrado, concatene los 
caracteres de la lista L, según las posiciones de dichos caracteres. '''
                        
#pri_ke
decifrado = decrypt(cifrar,pri_key,n)
decifrador = traducirMensaje(decifrado,Lista)

print('El mensaje desifrado es: ',decifrado,' y lo que traduce es:',decifrador)
