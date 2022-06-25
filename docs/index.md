---
template: pyscript.html
---

## 

```html
<head>
  <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
  <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>
```

##  `<py-script>`

=== "Le code :"
    ```html
    <py-script>
    "Demat d'an holl !"
    </py-script>
    ```
=== "Produit :"
    <py-script>
    "Demat d'an holl !"
    </py-script>

***

=== "Le code :"
    ```html
    <py-script src="./pyscripts/toto.py"></py-script>
    ```
=== "Produit :"
    <py-script src="./pyscripts/toto.py"></py-script>
=== "Avec dans le fichier `toto.py` :"
    ```python
    print('Toto est dans la place !')
    ```
***

=== "Le code :"
    ```html
    <p><strong>Aujourd'hui nous sommes le <label id='date'></label></strong></p>
    <py-script>
    import time
    pyscript.write('date', time.strftime('%d/%m/%Y %H:%M:%S'))
    </py-script>
    ```
=== "Produit :"
    <p><strong>Aujourd'hui nous sommes le <label id='date'></label></strong></p>
    <py-script>
    import time
    pyscript.write('date', time.strftime('%d/%m/%Y %H:%M:%S'))
    </py-script>
***


## `<py-repl>`

=== "Le code :"
    ```html
    <py-repl id="my-repl" auto-generate=true></py-repl>
    ```
=== "Produit :"
    <<py-repl id="my-repl" auto-generate=true></py-repl>

> Saisir une instruction Python dans la cellule REPL puis l'exécuter avec la combinaison de touches ++"⇑ Maj."+"Entrée ↵"++...

***

=== "Le code :"
    ```html
    <div>
    <py-repl>
    def inverse_chaine(chaine):
        chaine_inverse = ''
        for caractere in chaine:
            chaine_inverse = caractere + chaine_inverse
        return chaine_inverse
    def est_palindrome(chaine):
        chaine_inverse = inverse_chaine(chaine)
        if chaine.lower() == "kayak" :
            print("'kayak' est un faux ami, à l'envers il fait 'glouglou' !")
        else :
            return chaine == chaine_inverse
    </py-repl>
    <py-repl>
        # test 1 : doit renvoyer 'NSI'
    inverse_chaine('ISN')
    </py-repl>
    <py-repl>
        # test 2 : doit renyoyer False
    est_palindrome('NSI')
    </py-repl>
    <py-repl>
        # tests 3 : doit renyoyer True
    est_palindrome('ISN-NSI')
    </py-repl>
    <py-repl>
        # tests 4 : ???
    est_palindrome('kayak')
    </py-repl>
    <py-repl id="my-repl" auto-generate=true>
        # Réaliser vos propres tests :
    ...
    </py-repl>
    </div>
    ```
=== "Produit :"
    <div>
    <py-repl>
    def inverse_chaine(chaine):
        chaine_inverse = ''
        for caractere in chaine:
            chaine_inverse = caractere + chaine_inverse
        return chaine_inverse
    def est_palindrome(chaine):
        chaine_inverse = inverse_chaine(chaine)
        if chaine.lower() == "kayak" :
            print("'kayak' est un faux ami, à l'envers il fait 'glouglou' !")
        else :
            return chaine == chaine_inverse
    </py-repl>
    <py-repl>
        # test 1 : doit renvoyer 'NSI'
    inverse_chaine('ISN')
    </py-repl>
    <py-repl>
        # test 2 : doit renyoyer False
    est_palindrome('NSI')
    </py-repl>
    <py-repl>
        # tests 3 : doit renyoyer True
    est_palindrome('ISN-NSI')
    </py-repl>
    <py-repl>
        # tests 4 : ???
    est_palindrome('kayak')
    </py-repl>
    <py-repl id="my-repl" auto-generate=true>
        # Réaliser vos propres tests :
    ...
    </py-repl>
    </div>



***

=== "Le code :"
    ```html
    <py-repl>
    def indice_min(nombres : list) -> int :
        indice = 0
        minimum = nombres[0]
        for i in range(len(nombres)) :
            if minimum > nombres[i] :
                minimum = nombres[i]
                indice = i
            return indice
    </py-repl>
    <py-repl>
        # test 1 : doit renvoyer 2
    indice_min([2, 4, 1, 1]) == 2
    </py-repl>
    <py-repl>
        # test 2 : doit renyoyer True
    indice_min([5]) == 0
    </py-repl>
    <py-repl>
        # tests 3 : ne doit pas renvoyer de message d'erreur
    assert indice_min([2, 4, 1, 1]) == 2
    </py-repl>
    <py-repl id="my-repl" auto-generate=true>
        # Réaliser vos propres tests :
    indice_min(...)
    </py-repl>
    ```
=== "Produit un bug, `>` devient `&gt;` :"
    <py-repl>
    def indice_min(nombres : list) -> int :
        indice = 0
        minimum = nombres[0]
        for i in range(len(nombres)) :
            if minimum > nombres[i] :
                minimum = nombres[i]
                indice = i
            return indice
    </py-repl>
    <py-repl>
        # test 1 : doit renvoyer 2
    indice_min([2, 4, 1, 1]) == 2
    </py-repl>
    <py-repl>
        # test 2 : doit renyoyer True
    indice_min([5]) == 0
    </py-repl>
    <py-repl>
        # tests 3 : ne doit pas renvoyer de message d'erreur
    assert indice_min([2, 4, 1, 1]) == 2
    </py-repl>
    <py-repl id="my-repl" auto-generate=true>
        # Réaliser vos propres tests :
    indice_min(...)
    </py-repl>        
=== "Bientôt résolue :"

    [fix: < and > are parsed with HTML escape symbols](https://github.com/pyscript/pyscript/pull/481){target=_blank)}
    


***

## `<py-env>`

=== "Le code :"
    ```html
    <py-env>
    - paths:
      - ./pyscripts/mes_fonctions.py
    </py-env>
    <py-script>  
    from mes_fonctions import calcul_pi
    print("Calculons π :")      
    pi = calcul_pi(100000)
    s = f"π vaut approximativement {pi:.4f}"
    print(s)
    </py-script>
    ```
=== "Produit :"
    <py-env>
    - paths:
      - ./pyscripts/mes_fonctions.py
    </py-env>
    <py-script>  
    from mes_fonctions import calcul_pi
    print("Calculons π :")      
    pi = calcul_pi(100000)
    s = f"π vaut approximativement {pi:.4f}"
    print(s)
    </py-script>


## `<py-inputbox>`

## `<py-box>`

## `<py-button>`

## `<py-title>`

## `<py-config>`
