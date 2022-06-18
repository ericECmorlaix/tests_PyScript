---
template: pyscript.html
---

##



## Tests de PyScript

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

=== "Le code :"
```html
<py-env>
- bokeh
- numpy
- paths:
  - /utils.py
</py-env>
```