# Usamos kwargs para pasar parametros poe nombre y no por posicion

def saludo(**kwargs):
    print('Hola {} de {}'.format(kwargs['nombre'], kwargs['empresa']))


saludo(empresa='Cuemby', nombre='Luis')
saludo(nombre='Luis', empresa='Cuemby')

# Podemos extraer llaves y valores de kwargs como de diccionarios


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myFun(nombre='Fernando', empresa='Cuemby', ciudad='CDMX')
